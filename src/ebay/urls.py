from django.urls import path
from . import views

app_name = "ebay"


urlpatterns = [
    path("", views.get_data, name="home"),
]
