from django.core.management.base import BaseCommand


from ...functions import emitt_event


class Command(BaseCommand):
    def handle(self, *args, **options):
        emitt_event("test_entity", "test_key", "added")
