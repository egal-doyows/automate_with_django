from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help='Inserts data to the database'
    def handle(self, *args, **options):
        #add one data
        dataset=[
            {'roll_no':1005, 'name': 'Abdi', 'age':24},
            {'roll_no':1003, 'name': 'mumin', 'age':25},
            {'roll_no':1006, 'name': 'Yalax', 'age':22},
        ]
        for data in dataset:
            roll_no=data['roll_no']
            existing_record=Student.objects.filter(roll_no=roll_no).exists()
            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'],name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f"Student with roll number {roll_no} already exists"))
            
            


            
            

       
        self.stdout.write(self.style.SUCCESS("data inserted successfully"))
        