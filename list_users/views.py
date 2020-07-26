from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User


class ListView(generic.ListView):
    template_name = 'list_users/index.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()
