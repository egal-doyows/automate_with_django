from django.core.management.base import BaseCommand

#proposed output


class Command(BaseCommand):
    help = "Greets the users"
    def add_arguments(self, parser):
        parser.add_argument('name', type=str,help="specifies usernames")
        

    def handle(self , *args, **kwargs):
        name=kwargs['name']
        greeting=f'Hi, {name}, Good Evening'
        self.stdout.write(self.style.SUCCESS(greeting))