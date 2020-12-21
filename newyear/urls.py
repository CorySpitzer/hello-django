from django.urls import path

from . import views #. means import from current package
# from . import views #. means import from current package

urlpatterns = [
    path("", views.index, name="index")

]
