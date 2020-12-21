from django.urls import path
from . import views #. is same dir

urlpatterns = [
    path("", views.index, name="index"),
    path("cory", views.cory, name="cory"),
    path("<str:name>", views.greet, name="greet")

]
