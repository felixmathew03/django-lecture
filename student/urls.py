from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_student,name='add_student'),
    path('student_list/',views.student_list, name='student_list'),
    path('edit_student/<int:id>',views.edit_student,name='edit_student')
]