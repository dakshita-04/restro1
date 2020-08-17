from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login ,logout
from customer.models import *
from management.models import *
from management.models import Category as Ctg
from django.contrib.auth.models import User
from customer.states import *
from customer.models import Address as AddressModel
from customer.models import Reservation
import urllib3
import requests
import json


def error_404_view(request,exception):
   return render(request,'404.html')

def HeaderCart(usr):
    cartDish=Add_to_cart.objects.filter(user=usr)
    total=0
    for i in cartDish:
        total +=(i.dish.price)*(i.qty)
    return cartDish,total


def home(request):
    if request.user.is_staff:
        return redirect('AdminPanel')
    cat=Ctg.objects.all()
    dishes=Dish.objects.filter(avail=True)
    if request.user.is_anonymous:
      d={'cat':cat,'dishes':dishes}
    else:
       cartDish, total=HeaderCart(request.user)
       d={'cat':cat,'dishes':dishes,'cartDish':cartDish,'total':total}

    return render(request,'index.html',d)

def Reservation(request):
    msg=False
    if not request.user.is_authenticated:
        return redirect("account")
    if request.method == 'POST':
        data = request.POST
        date = data['date']
        time = data['time']
        guests = data['guests']
        name = request.user.username
        email = request.user.email
        mob = data["mob"]
        Reservation.objects.create(user = request.user,name = name, mob = mob, email = email, guest = guests, date = date, time = time,is_staff=True)
        msg=True
    if request.user.is_anonymous:
        d={'msg':msg}
    else:
        cartDish, total=HeaderCart(request.user)
        d={'msg':msg,'cartDish':cartDish,'total':total}
    return render(request,'reservation.html',d)




def account(request):
    errorL=False
    errorPass=False
    errorUser=False
    errorEmail=False
    if 'login' in request.POST:
        un=request.POST['un']
        pwd=request.POST['pwd']
        user=authenticate(username=un,password=pwd)
        if user:
            login(request,user)
            if request.user.is_staff:
                return redirect('AdminPanel')
            return redirect('home')
        else:
            errorL=True
    if 'signup' in request.POST:
        email=request.POST['e']
        ev=json.loads(requests.get('https://api.trumail.io/v2/lookups/json?email='+ email).text)
        print(ev)
        un=request.POST['un']
        pwd1=request.POST['pwd1']
        pwd2=request.POST['pwd2']
        check=User.objects.filter(username='un')
        if ev['deliverable'] is not True:
            errorEmail=True
        elif pwd1!=pwd2:
            errorPass=True
        elif check:
            errorUser=True
        else:
            User.objects.create_user(username= un,email= email,password= pwd1,is_staff=False)
            user=authenticate(username=un,password=pwd1)
            login(request,user)
            return redirect('home')
    d={'errorL':errorL,'errorPass':errorPass,'errorUser':errorUser,'errorEmail':errorEmail}
    return render(request,'account.html',d)

def Logout(request):
    logout(request)
    return redirect('home')


def Address(request):
    error = False
    StatesL = list()
    for i in States:
        StatesL.append(i[0])
    if "address" in request.POST:
        user = request.user
        hn = request.POST['hn']
        area = request.POST['area']
        pin = request.POST['pin']
        city = request.POST['city']
        state = request.POST['state']
        mob = request.POST['mob']
        http = urllib3.PoolManager()
        PinResult = requests.get('https://api.postalpincode.in/pincode/'+ str(pin))
        pintext = PinResult.text
        PinJson = json.loads(pintext)
        pinStatus = PinJson[0]['Status']
        noOfDiv = int(PinJson[0]['Message'][27:])
        t = 0
        names = ''
        print(pintext)
        for i in range(noOfDiv):
            if PinJson[0]['PostOffice'][i]['DeliveryStatus'] == "Delivery":
                t+=1
        if (pinStatus == "Success"  and t>0):
            dist = PinJson[0]['PostOffice'][i]['District']
            AddressModel.objects.create(user = request.user,HouseNum = hn, Area=area,City=city,District= dist,State = state, pin = pin,mobile = mob)
            return redirect('menu')
        else:
            error = True
            return render(request,'address.html',{'states':StatesL, 'error':error})

    return render(request,'address.html',{'states':StatesL, 'error':error})

def Cart(request):
    cartDish,total=HeaderCart(request.user)
    d={'cartDish':cartDish,'total':total}
    return render(request,'shop_cart.html',d)

def deleteOrder(request,Oid):
    Add_to_cart.objects.get(id=Oid).delete()
    return redirect('cart')
