from django.contrib import admin
from flow_app.models import Employee, ToDoItem, ToDoList

admin.site.register(ToDoItem)
admin.site.register(ToDoList)
admin.site.register(Employee)

