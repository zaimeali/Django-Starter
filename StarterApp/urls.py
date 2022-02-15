from django.urls import path

from . import views

urlpatterns = [
    path("", views.hello_world, name="hello_world"),
    path("more", views.more_message, name="Hello POC"),
    path("more/<str:message>", views.moreWord, name="Hello Message")
]
