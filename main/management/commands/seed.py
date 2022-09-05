from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

MODE_POPULATE = 'populate'
MODE_DELETE = 'delete'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')

def delete_users():
    u1 = User.objects.get(username='piriwin')
    u1.delete()

def set_users():
    u1 = User.objects.create_user('user1','user1@gmail.com','clavejeje')

def run_seed(self, mode):
    if mode == MODE_DELETE:
        delete_users()
    else:
        set_users()