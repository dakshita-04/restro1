from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from customer.models import *
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def about(request):
    team=Team.objects.all()
    d={'team':team}
    return render(request,'about.html',d)

def menu_all(request):
    cat=Category.objects.all()
    dish=Dish.objects.filter(avail=True)
    d={'cat':cat,'dish':dish}
    return render(request,'menu_all.html',d)

def contact(request):
    return render(request,'contact.html')

def SinglePage(request,dishid):
    dish=Dish.objects.filter(id=dishid).first()
    if request.POST:
        if not request.user.is_authenticated:
           return redirect('account')
        data=Add_to_cart.objects.filter(user=request.user,dish=dish)
        if data:
            data.update(qty=request.POST['qty'])
        else:
            Add_to_cart.objects.create(user=request.user,dish=dish,qty=request.POST['qty'])
    d={'dish':dish}
    return render(request,'itemsingle.html',d)

def AdminPanel(request):
    if not request.user.is_staff:
        return redirect('home')
    res=Reservation.objects.all()
    orders=Add_to_cart.objects.all()
    if 'delete' in request.POST:
        Reservation.objects.get(id=request.POST['delete']).delete()
    if 'confirm' in request.POST:
         Reservation.objects.filter(id=request.POST['confirm']).update(confirm=True)
         r=Reservation.objects.get(id=request.POST['confirm'])
         sub='reservation confirmed at tomato'
         from_mail=settings.EMAIL_HOST_USER
         data={'name':r.name,'guest':r.guest,'date':r.date,'time':r.time}
         html=get_template('mail.html').render(data)
         msg=EmailMultiAlternatives(sub,'',from_mail,[r.email])
         msg.attach_alternative(html,'text/html')
         msg.send()
    if 'deleteOrder' in request.POST:
        Add_to_cart.objects.filter(id=request.POST['deleteOrder']).delete()
    if 'confirmOrder' in request.POST:
        Add_to_cart.objects.filter(id=request.POST['confirmOrder']).update(confirm=True)
    d={'res':res,'orders':orders}
    return render(request,'index2.html',d)

def EditCat(request):
    cat=Category.objects.all()
    if 'delete' in request.POST:
        Category.objects.filter(id=request.POST['delete']).delete()
    if 'addcat' in request.POST:
        Category.objects.create(name=request.POST['name'])
    d={'cat':cat}
    return render(request,'editcat.html',d)

def EditTeam(request):
    team=Team.objects.all()
    if 'addteam' in request.POST:
        data=request.POST
        name=data['name']
        designation=data['designation']
        fb=data['fb']
        insta=data['insta']
        tu=data['tu']
        img=request.FILES['img']
        Team.objects.create(img = img, name = name, designation = designation, fb = fb, insta = insta, tu = tu)
    if 'delete' in request.POST:
        Team.objects.filter(id=request.POST['delete']).delete()
    d={'team':team}
    return render(request,'editteam.html',d)

def EditDish(request):
    dish=Dish.objects.all()
    cat=Category.objects.all()
    if 'avail' in request.POST:
        Dish.objects.filter(id=request.POST['avail']).update(avail=True)
    if 'unavail' in request.POST:
        Dish.objects.filter(id=request.POST['unavail']).update(avail=False)
    if 'adddish' in request.POST:
            data=request.POST
            c=Category.objects.get(id=data['cat'])
            title=data['title']
            mrp=data['mrp']
            price=data['price']
            dis=data['dis']
            img1=request.FILES['img1']
            img2=request.FILES['img2']
            img3=request.FILES['img3']
            Dish.objects.create(cat=c,title=title,mrp=mrp,price=price,dis=dis,img1=img1,img2=img2,img3=img3)
    if 'delete' in request.POST:
        Dish.objects.filter(id=request.POST['delete']).delete()
    d={'cat':cat,'dish':dish}
    return render(request,'editdish.html',d)









