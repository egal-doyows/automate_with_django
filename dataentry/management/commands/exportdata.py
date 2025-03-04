import csv
from django.core.management.base import BaseCommand
from django.apps import apps
import datetime


#proposed command = python manage.py exportdata\
class Command(BaseCommand):
    help='Exports data'
    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Model Name')

    def handle(self, *args, **kwargs):
        model_name=kwargs['model_name'].capitalize()

        #Searching the model from the apps
        model=None
        for app_config in apps.get_app_configs():
            try:
                model=apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                pass

        if not model:
            self.stderr.write(f'Model "{model_name}" not found')
            return

            
        #fetching data from DB
        data=model.objects.all()
       

        #Define CSV file name/path
        #Generate timestamp
        timestamp=datetime.datetime.now().strftime("%Y-%m-%d-%H-%S")

        file_path= f'exported_{model_name}_data_{timestamp}.csv'
        

        #open CSV file and write the data
        with open(file_path, 'w', newline='')as file:
            writer = csv.writer(file)

            #Write CSV Header
            #we want to print field names of the model
            writer.writerow([field.name for field in model._meta.fields])

            #write data rows
            for dt in data:
                writer.writerow([getattr(dt,field.name) for field in model._meta.fields])
        self.stdout.write(self.style.SUCCESS("Export Successfull"))

    


