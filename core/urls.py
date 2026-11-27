from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('doctors/',views.doctors,name='doctors'),
    path('departments/',views.departments,name='departments'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
]