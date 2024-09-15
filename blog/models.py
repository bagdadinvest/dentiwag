from __future__ import unicode_literals

from django.contrib import messages
from django.db import models
from django.shortcuts import redirect, render
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import Tag, TaggedItemBase
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.fields import StreamField
from wagtail.models import Orderable, Page
from wagtail.search import index
from wagtail.admin.panels import FieldPanel, InlinePanel, MultipleChooserPanel

from bakerydemo.base.blocks import BaseStreamBlock


# BlogPersonRelationship model: Manages the relationship between BlogPage and Person.
class BlogPersonRelationship(Orderable, models.Model):
    page = ParentalKey("BlogPage", related_name="blog_person_relationship", on_delete=models.CASCADE)
    person = models.ForeignKey("base.Person", related_name="person_blog_relationship", on_delete=models.CASCADE)

    panels = [FieldPanel("person")]


# BlogPageTag model: Handles the tagging relationship for BlogPage.
class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey("BlogPage", related_name="tagged_items", on_delete=models.CASCADE)


# BlogPage model: Represents individual blog posts.
class BlogPage(Page):
    introduction = models.TextField(help_text="Text to describe the page", blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only; horizontal width between 1000px and 3000px."
    )
    body = StreamField(BaseStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True)
    subtitle = models.CharField(blank=True, max_length=255)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    date_published = models.DateField("Date article published", blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("introduction"),
        FieldPanel("image"),  # Use FieldPanel for the image chooser
        FieldPanel("body"),
        FieldPanel("date_published"),
        InlinePanel("blog_person_relationship", label="Authors"),  # For managing authors (people)
        InlinePanel("gallery_images", label="Gallery Images"),  # For managing related images
        FieldPanel("tags"),
    ]

    search_fields = Page.search_fields + [index.SearchField("body")]

    # Returns related authors for the blog post
    def authors(self):
        return [
            n.person for n in self.blog_person_relationship.filter(person__live=True).select_related("person")
        ]

    # Property to get tags with URLs
    @property
    def get_tags(self):
        tags = self.tags.all()
        base_url = self.get_parent().url
        for tag in tags:
            tag.url = f"{base_url}tags/{tag.slug}/"
        return tags

    parent_page_types = ["BlogIndexPage"]  # Defines parent pages
    subpage_types = []  # No child pages allowed


# BlogIndexPage model: Serves as an index page for listing blog posts.
class BlogIndexPage(RoutablePageMixin, Page):
    introduction = models.TextField(help_text="Text to describe the page", blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only; horizontal width between 1000px and 3000px."
    )

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("image"),
    ]

    subpage_types = ["BlogPage"]  # Only BlogPage can live under this index page

    # Returns all child BlogPage objects
    def children(self):
        return self.get_children().specific().live()

    # Overrides context to return blog posts ordered by the date they were published
    def get_context(self, request):
        context = super().get_context(request)
        context["posts"] = BlogPage.objects.descendant_of(self).live().order_by("-date_published")
        return context

    # Custom route for displaying posts by tags
    @route(r"^tags/$", name="tag_archive")
    @route(r"^tags/([\w-]+)/$", name="tag_archive")
    def tag_archive(self, request, tag=None):
        try:
            tag = Tag.objects.get(slug=tag)
        except Tag.DoesNotExist:
            if tag:
                messages.add_message(request, messages.INFO, f'There are no blog posts tagged with "{tag}"')
            return redirect(self.url)

        posts = self.get_posts(tag=tag)
        context = {"self": self, "tag": tag, "posts": posts}
        return render(request, "blog/blog_index_page.html", context)

    # Required for preview functionality
    def serve_preview(self, request, mode_name):
        return self.serve(request)

    # Returns filtered BlogPage objects by tag if provided
    def get_posts(self, tag=None):
        posts = BlogPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    # Returns unique list of tags for all child posts
    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        return sorted(set(tags))


# BlogGalleryImage model: Manages multiple gallery images for a blog post.
class BlogGalleryImage(Orderable):
    page = ParentalKey('BlogPage', on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),  # Use FieldPanel for the image chooser
        FieldPanel('caption'),
    ]
