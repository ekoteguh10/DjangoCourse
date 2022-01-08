from django.urls import path
from . import views

urlpatterns = [
    # add your URLs
    path('', views.articles),
    path('categories/<str:name>', views.categories),
]