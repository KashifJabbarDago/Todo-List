from django.db import models

# Create your models here.
class todo_data(models.Model):
    text = models.TextField(max_length=25)
    def __str__(self):
        return self.text