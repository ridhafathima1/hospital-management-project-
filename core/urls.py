from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('doctors/',views.doctors,name='doctors')
]