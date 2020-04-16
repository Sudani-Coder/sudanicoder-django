from django.urls import path
from contact import views

app_name = "contact"

urlpatterns = [
    path("", views.index, name = "index"),
    path("contact/", views.contact, name = "contact"),
]
