from django.shortcuts import render
from django.http import HttpResponse

from viz.models import Task

def index(request):
    qset=Task.objects.all()

    return render(request, 'viz/index.html')
