from datetime import datetime, date
from django.db import models
from django.forms import CharField
from django.utils import timezone
from django.urls import reverse

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)
    

class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    creationDate = timezone.now()
    # dueDate = date()

    def __str__(self):
        return self.title

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse(
            "employee-update", args=[str(self.employee_list.id), str(self.id)]
        )

    def __str__(self):
        return self.first_name + " " + self.last_name

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    creationDate = timezone.now()
    tags = models.ManyToManyField(Tag)
    # dueDate = date()

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]

class Phases(models.Model):
    pass

