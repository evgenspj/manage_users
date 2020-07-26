from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from getpass import getpass
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class Command(BaseCommand):
    help = 'Add new user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        username = options['username']
        try:
            password = getpass()
            u = User(username)
            validate_password(password, user=User(username=username))
            User.objects.create_user(username, password=password)
            print('user created')
        except ValidationError as e:
            print(str(e))
        except IntegrityError:
            print('user with that username already exists')