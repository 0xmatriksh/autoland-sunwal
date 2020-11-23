from django.shortcuts import render
from .models import Cars
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    vehicles = Cars.objects.all()[:3]
    context = {'vehicles':vehicles}
    return render(request,'car/index.html',context)

def cars(request):
    vehicles = Cars.objects.all()
    paginator = Paginator(vehicles,3)
    page = request.GET.get('page')
    vehicles = paginator.get_page(page)
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