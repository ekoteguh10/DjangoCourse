from django.urls import path
from . import views

urlpatterns = [
    # add your URLs
    path('', views.get_all_articles),
]