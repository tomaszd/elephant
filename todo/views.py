# todo/views.py

from rest_framework import viewsets, generics, mixins  # add this
from rest_framework.generics import DestroyAPIView

from .models import Todo  # add this
from .serializers import TodoSerializer  # add this


class TodoView(viewsets.ModelViewSet):  # add this
    serializer_class = TodoSerializer  # add this
    queryset = Todo.objects.all()  # add this


class TodoViewCompleted(viewsets.ModelViewSet):  # add this
    serializer_class = TodoSerializer  # add this
    queryset = Todo.objects.filter(completed=True)  # add this

    def create(self, request, *args, **kwargs):
        if request.query_params.get('delete_all'):
            print("Delete all finished tasks")
            self.queryset.delete()
            return self.list(request, *args, **kwargs)
        return super().create(request, *args, **kwargs)

# write custom code
