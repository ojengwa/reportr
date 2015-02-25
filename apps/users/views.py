from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def profile(request, username):
    return HttpResponse('Welcome, ' + username)
    # return render(request, 'users/index.html', locals())


def dashboard(request):
    pass


@login_required
def success(request):
    print request.user
    return render(request, 'users/index.html', locals())