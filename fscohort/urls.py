from django.urls import path
from .views import index, student_add, student_delete, student_list, student_update

urlpatterns = [
    path('', index, name='home'),
    path('students/', student_list, name='students'),
    path('students/add/', student_add, name='students_add'),
    path('students/update/<int:id>/', student_update, name='students_update'),
    path('students/delete/<int:id>/', student_delete, name='students_delete'),
]