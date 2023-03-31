from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name = 'home'),
    path('<day_name>/',views.index,name = 'index')
]