from django.urls import path
from . import views
from customer.views import *

urlpatterns = [
    path('reservation/',Reservation,name='reservation'),
    path('account/',views.account,name='account'),
    path('logout/',Logout,name='logout'),
    path('address/',Address,name='address'),
    path('cart/',Cart,name='cart'),
    path('deleteOrder/<int:Oid>',deleteOrder,name='dOrder')

]
