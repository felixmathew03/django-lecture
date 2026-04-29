from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm
from django.core.mail import send_mail

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password =form.cleaned_data['password']
            
            user = User(username=username)
            user.set_password(password)
            user.save()
            return redirect(login_view)
    else :
        form = UserForm()
    return render(request, 'manualauth/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user  =  User.objects.get(username=username)
        if user.is_valid_password(password):
            request.session['user_id'] = user.id
            return redirect(dashboard)
        else:
            return (request, 'manualauth/login.html')
    
    return render(request, 'manualauth/login.html')

def dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect(login_view)
    user = User.objects.get(id = user_id)
    print(user)
    return HttpResponse(f'Welcome, {user.username} to user dashboard')

def logout_view(request):
    request.session.flush()
    return redirect(login_view)

def greet(request):
    send_mail(
        subject='Welcome message',
        message='Welcome to our django app',
        from_email='felixmathewtt@gmail.com',
        recipient_list=['adiadithyaajayan@gmail.com'],
        fail_silently=False
    )
    return HttpResponse('Email sent successfully')