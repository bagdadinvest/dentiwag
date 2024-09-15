from django.core.management.base import BaseCommand
from wagtail.models import Page

class Command(BaseCommand):
    help = "Publish all unpublished pages in the Wagtail site."

    def handle(self, *args, **kwargs):
        # Fetch all pages that are not live (drafts)
        unpublished_pages = Page.objects.filter(live=False)
        
        # If no unpublished pages are found
        if not unpublished_pages.exists():
            self.stdout.write(self.style.SUCCESS("No unpublished pages found."))
            return

        # Iterate over all unpublished pages and publish them
        for page in unpublished_pages:
            page.save_revision().publish()
            self.stdout.write(self.style.SUCCESS(f"Published page: {page.title}"))

        self.stdout.write(self.style.SUCCESS("All unpublished pages have been published."))
