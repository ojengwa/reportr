from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'home/index.html', locals())

def about(request):
    return render(request, 'home/about.html', locals())

def login(request):
    return render(request, 'home/login.html', locals())

@login_required
def success(request):
    print request.user
    return HttpResponse('success!')

def errors(request):
    print request.user
    return HttpResponse('error')

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')