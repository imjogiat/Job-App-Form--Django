from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about")
    #add about path for the about html file- to render it on the web app
]