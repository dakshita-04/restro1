from django.urls import path
from .import views
from management.views import *

urlpatterns = [
    path('about/',views.about,name='about'),
    path('menu_all/',views.menu_all,name='menu_all'),
    path('contact/',views.contact,name='contact'),
    path('dish/<int:dishid>',SinglePage,name='dish'),
    path('AdminPanel/',AdminPanel,name='AdminPanel'),
    path('editcat',EditCat,name='editcat'),
    path('editteam',EditTeam,name='editteam'),
    path('editdish',EditDish,name='editdish'),
]
