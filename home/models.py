from typing import ClassVar
from django.db import models
from django.contrib.auth.models import User

status_choices = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending')
]

class Todo(models.Model):
    title = models.CharField(max_length = 1000)
    status = models.CharField(max_length = 10, choices = status_choices)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.title} | By:- {self.user}"