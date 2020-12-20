from django.urls import path
from . import views #. is same dir

urlpatterns = [
    path("", views.index, name="index"),
    path("cory", views.cory, name="cory")

]
