from django.shortcuts import render,redirect, get_object_or_404
from .models import Student, Course
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

@login_required
def add_student(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST.get('age')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        course_id = request.POST.get('course')
        course = Course.objects.get(id=course_id) 
        print(course)
        Student.objects.create(
            name= name,
            age=age,
            course=course,
            email = email,
            image = image
        )
        return redirect('student_list')
    return render(request,'add_student.html',{'courses':courses})

def student_list(request):
    if request.user.is_authenticated:
        
        search = request.GET.get('search')
        course_id = request.GET.get('course')
        
        students = Student.objects.all()
        # if search:
        #     students = students.filter(name__icontains=search)
        if course_id:
            course = Course.objects.get(id= course_id)
            students = students.filter(course=course)
            # students1 = course.students.all()
            # print(students1)
        # courses = Student.objects.values_list('course',flat=True).distinct()
        courses = Course.objects.all()
        return render(request, 'student_list.html',{'students':students,'courses':courses})
    else:
        return redirect(login_view)
    
@login_required
def edit_student(request,id):
    # student = Student.objects.get(id=id)
    student = get_object_or_404(Student,id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')
        student.course = request.POST.get('course')
        student.save()
        return redirect('student_list')
    return render(request, 'edit_student.html',{'student':student})

def register(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('password')
        cpassword= request.POST.get('cpassword')
        if password == cpassword:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect(login_view)
        else:
            return render(request, 'register.html',{"error":'Passwords does not match!!'})
        
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username = username,password=password)
            if user is not None:
                login(request,user)
                return redirect('student_list')
            else:
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect(login_view)