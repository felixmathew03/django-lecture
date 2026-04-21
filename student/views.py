from django.shortcuts import render,redirect, get_object_or_404
from .models import Student, Course

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