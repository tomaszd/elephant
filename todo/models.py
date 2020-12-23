# todo/models.py


from django.db import models

# Create your models here.
from django.utils import timezone

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
    category = models.TextField(null=True, blank=True)
    priority = models.TextField(choices=PRIORITY_CHOICES, default="Low")
    created = models.DateTimeField(editable=False, default=timezone.now())
    modified = models.DateTimeField(default=timezone.now())

    readonly_fields = ("created", "modified",)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Todo, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
