from django.core.management.base import BaseCommand
from faker import Faker
from wagtail.models import Page
from bakerydemo.breads.models import ImplantPage, ImplantsIndexPage  # Adjust import based on your models

fake = Faker()

class Command(BaseCommand):
    help = "Generate fake data for the website"

    def handle(self, *args, **kwargs):
        # Fetch the ImplantsIndexPage to add child pages to
        try:
            implants_index = ImplantsIndexPage.objects.get(slug='implants')
        except ImplantsIndexPage.DoesNotExist:
            self.stdout.write(self.style.ERROR("Implants index page not found. Please create it first."))
            return

        # Generate fake implant pages
        for _ in range(10):  # Generate 10 fake pages
            implant_page = ImplantPage(
                title=fake.company(),  # Fake title
                introduction=fake.text(100),  # Fake introduction text
                body=[('paragraph', fake.text(500))],  # Example body content
            )
            
            # Add child and save the page
            implants_index.add_child(instance=implant_page)
            implant_page.save_revision().publish()
            
            self.stdout.write(self.style.SUCCESS(f"Created and published fake page: {implant_page.title}"))

        self.stdout.write(self.style.SUCCESS("Fake data generation complete."))
