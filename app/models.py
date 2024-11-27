from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    course = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age}, {self.course} курс"


class Todo(models.Model):
    title = models.CharField(max_length=255)
    completed= models.BooleanField()
    date_created = models.DateField(auto_now_add=True)
    date_edited = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
