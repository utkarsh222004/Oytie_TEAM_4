from django.db import models

class Teacher(models.Model):
    name=models.CharField(max_length=20)
    username=models.CharField(max_length=50)
    address=models.CharField(max_length=80)
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length = 254)
    password=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)

class Batch(models.Model):
    batch_name=models.CharField(max_length=20)

class Student(models.Model):
    name=models.CharField(max_length=20)
    username=models.CharField(max_length=50)
    address=models.CharField(max_length=80)
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length = 254)
    batch=models.ForeignKey("Batch", on_delete=models.CASCADE)
    password=models.CharField(max_length=20)

class Assignment(models.Model):
    name=models.CharField(max_length=50)
    batch=models.ForeignKey("Batch", on_delete=models.CASCADE)
    teacher_id=models.ForeignKey("Teacher", on_delete=models.CASCADE)
    questions=models.TextField(max_length=200)
    deadline=models.DateField()

class Solution(models.Model):
    stud_id=models.ForeignKey("Student", on_delete=models.CASCADE)
    assign_id=models.ForeignKey("Assignment", on_delete=models.CASCADE)
    solution=models.TextField(max_length=500)
    points=models.CharField(max_length=20,null=True)
    comment=models.CharField(max_length=80,null=True)
    submission_date=models.DateField()

