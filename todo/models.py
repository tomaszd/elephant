# todo/models.py

from django.db import models

# Create your models here.
PRIORITY_CHOICES = [
    ("Low", "Low"),
    ("Medium", "Medium"),
    ("High", "High"),
]


# add this
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.TextField(choices=PRIORITY_CHOICES, default="Low")

    def __str__(self):
        return self.title
