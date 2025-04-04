import csv
from django.core.management.base import BaseCommand
from tracker.models import Food

class Command(BaseCommand):
    help = 'Import food dataset from CSV'

    def handle(self, *args, **kwargs):
        with open('tracker/food_data.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Food.objects.get_or_create(
                    name=row['name'],
                    calories=row['calories'],
                    carbs=row['carbs'],
                    fats=row['fats'],
                    proteins=row['proteins']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported food dataset!'))
