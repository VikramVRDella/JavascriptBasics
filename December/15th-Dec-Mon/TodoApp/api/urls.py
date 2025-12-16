from django.urls import path
from .views import TodoAPI

urlpatterns=[
    path("api/",TodoAPI.as_view()),
    path("api/<int:id>/",TodoAPI.as_view())
]