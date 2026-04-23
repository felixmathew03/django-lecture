from django.urls import path
from . import views

urlpatterns = [
    path('',views.student_list, name='student_list'),
    path('add/',views.add_student,name='add_student'),
    path('edit_student/<int:id>',views.edit_student,name='edit_student'),
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
]