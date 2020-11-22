from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'car/index.html')

def cars(request):
    return render(request, 'car/cars.html')

def about(request):
    return render(request, 'car/about.html')

def contact(request):
    return render(request, 'car/contact.html')