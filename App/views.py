import json
import re
import random

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
# from datetime import datetime, timedelta
import datetime

from .models import *

# random transaction id and account number
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

def index(request):
    return render(request, "App/index.html")

def allRooms(request):
    return render(request, "App/allRooms.html")

@login_required
def profile(request):
    customer = Customer.objects.filter(user=request.user)
    context = {'customer':customer}
    return render(request, "App/profile.html", context)

@csrf_exempt
def getCatg(request):
    if request.method == 'POST':
        categories = Category.objects.all()
        return JsonResponse([category.serialize() for category in categories], safe=False)
    return HttpResponseRedirect(reverse('index'))

@csrf_exempt
def getRooms(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        filter = data.get('filter')
        if filter == 'all':
            rooms = Room.objects.all().order_by('?')[:data.get('limit')]
            return JsonResponse([room.serialize() for room in rooms], safe=False)
        rooms = Room.objects.filter(catg_id=filter)
        return JsonResponse([room.serialize() for room in rooms], safe=False)
    return HttpResponseRedirect(reverse('index'))

@csrf_exempt
def booking(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        roomId = data.get('roomId')
        night = data.get('night')
        StartDate = data.get('date')
        date_1 = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
        end_date = date_1 + datetime.timedelta(days=int(night))
        adult = data.get('adult')
        children = data.get('children')
        car = data.get('car')
        pickUp = data.get('pickUp')
        dropOff = data.get('dropOff')
        
        price=''
        parking_charge=''
        room = Room.objects.filter(pk=roomId)
        for room in room:
          price = room.price
        hotel = HotelConfig.objects.all()
        for hotel in hotel:
          parking_charge = hotel.parking_charge
        total = (int(price)*int(night))+(int(parking_charge)*int(car))
        rrr = random_with_N_digits(15)
        driver1 = ''
        driver2 = ''

        driversList = []
        drivers = Driver.objects.all()
        for driver in drivers:
            if driver is not None:
                driversList.append(driver.tel)
            else:
                driversList.append('')
        try:
            driver1 = random.choice(driversList)
            driver2 = random.choice(driversList)
        except:
            driver1 = 'Not Available'
            driver2 = 'Not Available'
            
        customer = Customer.objects.filter(user=request.user)
        for c in customer:
            c.room_no = roomId
            c.lodgeIn = StartDate
            c.lodgeOut = end_date
            c.adult = adult
            c.children = children
            c.car = car
            c.night = night
            c.rrr = rrr
            c.price = total
            if pickUp == 'on':
                d1 = driver1
                c.pick_up_driver = Driver.objects.get(tel=d1)
            if dropOff == 'on':
                d2 = driver2
                c.drop_off_driver = Driver.objects.get(tel=d2)
            c.save()
            return JsonResponse({
                'msg':'success',
                'roomId':roomId,
                'StartDate':StartDate,
                'night':night,
                'rrr':rrr,
                'driver1':driver1,
                'driver2':driver2,
                'total':total,
                })
        
        return JsonResponse({'msg':'user not found'})
    
    if str(request.user) == "AnonymousUser":
        return HttpResponse('<a href="/" class="">Please Log In First</a>')
    account = ''
    acc = Account.objects.all()
    if acc is not None:
        account = acc
    roomId = request.GET['room']
    room = Room.objects.filter(pk=roomId)
    for room in room:
        price = room.price
        hotel = HotelConfig.objects.all()
        for hotel in hotel:
            parking_charge = hotel.parking_charge
            context = {'price':price,'parking_charge':parking_charge,'roomId':roomId,'account':account}
            return render(request, "App/booking.html", context)
    
    

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # Attempt to sign user in
        email = data.get('email')
        password = data.get("password")
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return JsonResponse({"msg":'success'})
        else:
            return JsonResponse({"msg":'User not found!'})
    else:
        return HttpResponseRedirect(reverse('index'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


@csrf_exempt
def register_view(request):
    if request.method == "POST":
        
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        username = request.POST["email"]
        dob = request.POST["dob"]
        tel = request.POST["tel"]
        address = request.POST["address"]
        meansOfId = request.POST["meansOfId"]
        idNumber = request.POST["idNumber"]
        password = request.POST["password"]
        date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

        # Attempt to create new user
        try:
            email = ''
            ruser = User.objects.create_user(username, email, password)
            ruser.save()

        except IntegrityError:
            return JsonResponse({"message": "Email address already taken."})
        
        user = User.objects.get(username=username)
        customer = Customer(user=user, fname=fname, lname=lname, dob=dob, tel=tel, address=address, meansOfId=meansOfId, idNumber=idNumber)
        customer.save()

        customer = Customer.objects.get(user=User.objects.get(username=username))
        history = f"Joined us on {date}"
        history = History(customer=customer,history=history)

        user = authenticate(request, username=username, password=password)
        login(request, user)

        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))
