
from django.db import models
from django.urls import reverse

class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    birth_date = models.DateTimeField()

class Student(models.Model):

    stu_name=models.CharField(max_length=100)
    stu_email=models.EmailField(max_length=50)
    stu_phone_no=models.CharField(max_length=40)
    stu_dob=models.DateField()

    def get_absolute_url(self):
        return reverse('edu:student_details')



