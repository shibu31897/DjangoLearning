from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import datetime
from django.contrib.auth.decorators import login_required

def home(request):
    # return HttpResponse('Hello, World !')
    return render(request, 'home/welcome.html', {})


@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {'currentTime': datetime.datetime.now()})
