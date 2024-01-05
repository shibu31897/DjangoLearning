from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'currentTime': datetime.datetime.now()}


# def home(request):
#     # return HttpResponse('Hello, World !')
#     return render(request, 'home/welcome.html', {})

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {'currentTime': datetime.datetime.now()})
