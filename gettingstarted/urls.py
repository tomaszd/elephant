from django.urls import path, include

from django.contrib import admin
from rest_framework import routers

import todo
from todo import views

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

router = routers.DefaultRouter()  # add this
router.register(r'todos', views.TodoView, 'todo')  # add this
router.register(r'todos_completed', views.TodoViewCompleted, 'todo')

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('api/', include(router.urls))  # add this
]
