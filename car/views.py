from django.shortcuts import render
from .models import Cars

# Create your views here.
def home(request):
    return render(request,'car/index.html')

def cars(request):
    vehicles = Cars.objects.all()
    context = {'vehicles':vehicles}
    return render(request, 'car/cars.html',context)

def about(request):
    return render(request, 'car/about.html')

def contact(request):
    return render(request, 'car/contact.html')

def details(request,pk):
    vehicle = Cars.objects.get(id=pk)
    print(vehicle)
    context = {'vehicle':vehicle}
    return render(request,'car/details.html',context)