from django.core.management.base import BaseCommand, CommandError
from shoestore.api.views import ManufacturerViewSet, ShoeTypeViewSet,ShoeColorViewSet, ShoeViewSet

from shoestore.models import Manufacturer, ShoeType, ShoeColor, Shoe, 

shoeTypes = [

    'sneaker',
    'boot',
    'sandal',
    'dress',
    'other'
    
]

shoeColors = [
    
    'Red',
    'Orange',
    'Yellow',
    'Green',
    'Blue',
    'Indigo',
    'Violet',
    'White',
    'Black'
    
]

class Command(BaseCommand):


    def add_arguments(self, parser):
        parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for poll_id in options['poll_id']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))