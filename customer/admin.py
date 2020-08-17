from django.contrib import admin
from customer.models import *
from .models import *

admin.site.register(Address)
admin.site.register(Reservation)
admin.site.register(Add_to_cart)
