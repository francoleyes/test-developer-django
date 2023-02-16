from .models import BikeSantiago, Project
from .models import get_bike_santiago_data, load_data_from_json
from django.shortcuts import render
from django.core.paginator import Paginator

def bike_santiago_view(request):
    get_bike_santiago_data()
    bikes_santiago = BikeSantiago.objects.all()

    paginator = Paginator(bikes_santiago, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'core/bikesantiago.html', {'bikes_santiago': bikes_santiago, 'page_obj': page_obj})

def projects_view(request):
    load_data_from_json()
    
    projects = Project.objects.all()

    paginator = Paginator(projects, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'core/projects.html', {'projects': projects, 'page_obj': page_obj})