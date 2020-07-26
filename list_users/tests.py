from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from io import StringIO
from django.core.management import call_command
from unittest.mock import patch
from django.core.management import CommandError
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class TestListView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_empty(self):
        '''test view without added users'''
        User.objects.all().delete()
        html = str(self.client.get('/list_users/').content)
        self.assertTrue('No users were added.' in html)
    
    def test_users_added(self):
        '''test view with several users in db'''
        User.objects.create_user('test_user1', password='pass1')
        User.objects.create_user('test_user2', password='pass2')
        html = str(self.client.get('/list_users/').content)
        self.assertTrue('test_user1' in html)
        self.assertTrue('test_user2' in html)


class TestAddUserCommand(TestCase):
    def test_without_username(self):
        '''run command without required argument'''
        with self.assertRaises(CommandError):
            call_command('add_user')

    # не удалось запустить данный тест(return_value принимает значение test_pass)
    # def test_without_password(self):
    #     with patch('getpass.getpass', return_value=''):
    #         call_command('add_user', 'test_user')
    #         self.assertFalse(bool(User.objects.filter(username='test_user')))

    def test_correct(self):
        '''run command with correct username and password'''
        with patch('getpass.getpass', return_value='test_pass'):
            call_command('add_user', 'test_user')
            self.assertTrue(bool(User.objects.filter(username='test_user')))
