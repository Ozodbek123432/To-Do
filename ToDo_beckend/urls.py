from django.urls import path,include
from .views import *


urlpatterns = [
    path('', include("accaounts.urls"),name = 'home'),
    path('home/', HomeView.as_view(),name = 'frontend'),
]

