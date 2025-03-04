from django.core.management.base import BaseCommand, CommandError
from dataentry.models import Student
import csv
from django.apps import apps

class Command(BaseCommand):
    help="imports large data into model"
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='path to CSV') 
        parser.add_argument('model_name', type=str, help='model name') 
        
    

    def handle(self, *args, **kwargs):
        file_path=kwargs['file_path']
        model_name=kwargs['model_name'].capitalize()

        #searching models in all the installed apps
        model=None
        for app_config in apps.get_app_configs():
            #Try to search for the model
            try:
                model=apps.get_model(app_config.label,model_name)
                break #stop search once model is found
            except LookupError:
                continue # models not found in app, continue to the next app
        
        if not model:
            raise CommandError(f'Model "{model_name}" not found')


        with open(file_path, 'r') as file:
            reader=csv.DictReader(file)
            for row in reader:
                # roll_no=row['roll_no']
                # existing_record=Student.objects.filter(roll_no=roll_no).exists()
                # if not existing_record:
                    #Student.objects.create(roll_no=roll_no, name=row['name'], age=row['age'])
                    #The above statemnt is correct but not suitable when the columns are many
                    model.objects.create(**row)
                    self.stdout.write(self.style.SUCCESS("data inserted successfully"))
                # else:
                #     self.stdout.write(self.style.WARNING(f"Student with Roll No {roll_no} already exists"))

        

        

