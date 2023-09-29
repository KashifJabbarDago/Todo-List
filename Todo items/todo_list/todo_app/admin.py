from django.contrib import admin
# here imported class of data from todo_app models 
from todo_app.models import todo_data
# Register your models here.
admin.site.register(todo_data)
