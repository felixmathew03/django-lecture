from django.db import models

class Course(models.Model):
    name= models.CharField(max_length=20)
    duration = models.IntegerField()
    
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to='students')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='students')
    
    def __str__(self):
        return self.name