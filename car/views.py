from django.shortcuts import render
from .models import Cars,Customer,Book
import json,datetime
from django.http import JsonResponse
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    vehicles = Cars.objects.all()[:3]
    context = {'vehicles':vehicles}
    return render(request,'car/index.html',context)

def cars(request):
    
    all_vehicles = Cars.objects.all()
    paginator = Paginator(all_vehicles,3)
    page = request.GET.get('page')
    vehicles = paginator.get_page(page)
    print(vehicles)
    context = {
        'all_vehicles':all_vehicles,
        'vehicles':vehicles
        }
    return render(request, 'car/cars.html',context)

def about(request):
    return render(request, 'car/about.html')

def search(request):
    all_vehicles = Cars.objects.all()
    if request.method == 'POST':
        data = request.POST['name_car']
        print(data)
        vehicle = Cars.objects.get(name=data)
    context = {
        'all_vehicles':all_vehicles,
        'vehicle':vehicle
        }
    return render(request, 'car/search.html',context)

def contact(request):
    return render(request, 'car/contact.html')

def details(request,pk):
    vehicle = Cars.objects.get(id=pk)
    print(vehicle)
    context = {'vehicle':vehicle}
    return render(request,'car/details.html',context)

def book(request,pk):
    vehicle = Cars.objects.get(id=pk)
    context = {'vehicle':vehicle}
    return render(request,'car/book.html',context)

def bookCar(request):
    now = datetime.datetime.now()
    print(now)
    data = json.loads(request.body)
    print(data)
    customer,created = Customer.objects.get_or_create(email=data['userForm']['email'])
    customer.name = data['userForm']['name']
    customer.phone = data['userForm']['phone']
    customer.message = data['userForm']['message']
   
    customer.save()
    print(customer)
    print(type(customer))

    book = Book.objects.create(customer=customer,complete=False)
    carnum = data['userForm']['car']
    Cars.objects.get(id=carnum)
    book.carname = Cars.objects.get(id=carnum).name
    book.date_booked = now
    # print(customer)
    book.save()
    
    return JsonResponse("it was booked",safe=False)
    