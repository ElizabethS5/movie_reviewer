from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'populate mock movies'
    
    def handle(self, *args, **kwargs)