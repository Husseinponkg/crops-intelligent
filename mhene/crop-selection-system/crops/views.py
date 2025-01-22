from django.shortcuts import render
from .models import Crop

def home(request):
    return render(request, 'crops/home.html')

def dashboard(request):
    crops = Crop.objects.all()
    return render(request, 'crops/dashboard.html', {'crops': crops})

def dashboard_by_region(request, region):
    if region == "Arusha":
        crops = [
            {"name": "Maize", "region": "Arusha", "image": "crops/maize.jpg"},
            {"name": "Beans", "region": "Arusha", "image": "crops/beans.jpg"}
        ]
    elif region == "Dar es Salaam":
        crops = [
            {"name": "Rice", "region": "Dar es Salaam", "image": "crops/rice.jpg"},
            {"name": "Cassava", "region": "Dar es Salaam", "image": "crops/cassava.jpg"}
        ]
    elif region == "Dodoma":
        crops = [
            {"name": "Wheat", "region": "Dodoma", "image": "crops/wheat.jpg"},
            {"name": "Sorghum", "region": "Dodoma", "image": "crops/sorghum.jpg"}
        ]
    elif region == "Kilimanjaro":
        crops = [
            {"name": "Bananas", "region": "Kilimanjaro", "image": "crops/bananas.jpg"},
            {"name": "Coffee", "region": "Kilimanjaro", "image": "crops/coffee.jpg"}
        ]
    else:
        crops = []

    return render(request, 'crops/dashboard.html', {'crops': crops, 'region': region})

def crops_by_region(request, region):
    crops = Crop.objects.filter(region__exact=region)  # Use the exact lookup
    return render(request, 'crops/crops_by_region.html', {'crops': crops, 'region': region})