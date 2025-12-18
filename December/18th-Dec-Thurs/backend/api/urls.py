from django.urls import path
from .views  import StudentAPI

urlpatterns =[
    path('api/',StudentAPI.as_view()),
    path('api/<int:id>/',StudentAPI.as_view()),
]