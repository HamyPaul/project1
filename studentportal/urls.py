from django.urls import path
from . import views

app_name= 'studentportal'
urlpatterns = [
    path(route='', view=views.hi, name='index'),

]