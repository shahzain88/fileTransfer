from django.urls import path
from . import views


urlpatterns = [
    path('', views.contact_create_list, name="create_contact_list")
    ]
