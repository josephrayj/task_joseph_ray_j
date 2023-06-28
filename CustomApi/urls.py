from django.urls import path
from .views import create_employee, delete_employee, update_employee ,get_employee

urlpatterns = [
    path('employee_create', create_employee, name='create_person'),
    path('employee/<str:regid>', update_employee, name='update_employee'),
    path('employee_delete', delete_employee, name='delete_employee'),
    path('employees',get_employee,name='get_employee')
]
