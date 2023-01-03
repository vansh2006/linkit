from django.core.management.base import BaseCommand
from shortener.models import ShortURL

class Command(BaseCommand):
    help = 'Deletes all items in the ShortURL model'

    def handle(self, *args, **options):
        ShortURL.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all items in the ShortURL model'))
