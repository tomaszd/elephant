# todo/views.py

from rest_framework import viewsets  # add this

from .models import Todo  # add this
from .serializers import TodoSerializer  # add this


class TodoView(viewsets.ModelViewSet):  # add this
    serializer_class = TodoSerializer  # add this
    queryset = Todo.objects.all()  # add this
