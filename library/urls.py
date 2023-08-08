from django.urls import path

from . import views
app_name = "library"

urlpatterns = [
    path("", views.Front_look, name = "Front_look"),
    path("login_test/work/submit", views.Work_area, name = "Work_area"),
    path("login_test/work/check", views.Avalability, name = "Avalability"),
    ]