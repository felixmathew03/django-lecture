from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('sendmail/',views.greet),
    path('',views.dashboard),
]