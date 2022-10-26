
from django.core.management.base import BaseCommand
from demo.models import Phone
import datetime

#yesterday = datetime.date(2017, 5, 2)

class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        import this
        f = open('phones.csv')
        for line in f:
            s = line.split(";")
            phone = Phone(name=s[1], image=s[2], price = s[3], release_date = s[4],lte_exists = bool(s[5]))
            phone.save()


