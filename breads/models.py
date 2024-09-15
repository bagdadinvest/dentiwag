from django import forms
from django.contrib.contenttypes.fields import GenericRelation
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.models import DraftStateMixin, Page, RevisionMixin
from wagtail.search import index

from bakerydemo.base.blocks import BaseStreamBlock


class Country(models.Model):
    """
    A Django model to store set of countries of origin for implants or crowns.
    """

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "country of origin"
        verbose_name_plural = "countries of origin"


class ImplantMaterial(DraftStateMixin, RevisionMixin, models.Model):
    """
    A Django model to store a single material used in implants or crowns.
    """

    name = models.CharField(max_length=255)

    revisions = GenericRelation(
        "wagtailcore.Revision",
        content_type_field="base_content_type",
        object_id_field="object_id",
        related_query_name="implant_material",
        for_concrete_model=False,
    )

    panels = [
        FieldPanel("name"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "implant material"
        verbose_name_plural = "implant materials"


class ImplantType(RevisionMixin, models.Model):
    """
    A Django model to define the type of implant or crown.
    """

    title = models.CharField(max_length=255)

    revisions = GenericRelation(
        "wagtailcore.Revision",
        content_type_field="base_content_type",
        object_id_field="object_id",
        related_query_name="implant_type",
        for_concrete_model=False,
    )

    panels = [
        FieldPanel("title"),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "implant type"
        verbose_name_plural = "implant types"


class ImplantPage(Page):
    """
    Detail view for a specific implant or crown.
    """

    introduction = models.TextField(help_text="Brief description of the implant or crown", blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Image representing the implant or crown.",
    )
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True
    )
    origin = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Country of origin for the implant or crown."
    )

    implant_type = models.ForeignKey(
        "breads.ImplantType",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="The type of implant or crown (e.g., titanium, zirconia).",
    )
    materials = ParentalManyToManyField("ImplantMaterial", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("image"),
        FieldPanel("body"),
        FieldPanel("origin"),
        FieldPanel("implant_type"),
        MultiFieldPanel(
            [
                FieldPanel(
                    "materials",
                    widget=forms.CheckboxSelectMultiple,
                ),
            ],
            heading="Materials Used",
            classname="collapsed",
        ),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("body"),
    ]

    parent_page_types = ["ImplantsIndexPage"]


class ImplantsIndexPage(Page):
    """
    Index page for implants or crowns, with pagination.
    """

    introduction = models.TextField(help_text="Introduction to the implants or crowns section", blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Image representing the implants or crowns page.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("image"),
    ]

    # Can only have ImplantPage children
    subpage_types = ["ImplantPage"]

    def get_implants(self):
        return (
            ImplantPage.objects.live().descendant_of(self).order_by("-first_published_at")
        )

    def children(self):
        return self.get_children().specific().live()

    def paginate(self, request, *args):
        page = request.GET.get("page")
        paginator = Paginator(self.get_implants(), 12)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    def get_context(self, request):
        context = super(ImplantsIndexPage, self).get_context(request)
        implants = self.paginate(request, self.get_implants())
        context["implants"] = implants
        return context
