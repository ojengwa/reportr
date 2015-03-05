from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from apps.users.models import Staff
from django.shortcuts import get_object_or_404


# Create your views here.
@login_required
def profile(request, username):
    # return HttpResponse('Welcome, ' + username)
    user = get_object_or_404(Staff, username=username)
    return render(request, 'users/index.html', locals())

@login_required
def dashboard(request):
    obj = request.user
    user = get_object_or_404(Staff, username=obj.username)
    return render(request, 'users/index.html', locals())


@login_required
def success(request):
    print request.user
    return render(request, 'users/index.html', locals())


@login_required
def parapo(request):
    return render(request, 'users/parapo.html', locals())


def reports(request):
    return render(request, 'users/reports.html', locals())


def create_report(request):
    return render(request, 'users/create_report.html', locals())