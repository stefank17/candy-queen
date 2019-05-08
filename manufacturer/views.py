from django.shortcuts import render
from manufacturer.models import Manufacturer


def index(request):
    return render(request, 'manufacturer/index.html', {
        'manufacturers': Manufacturer.objects.all()
    })