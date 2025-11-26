from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"person", ToDoCrud)

urlpatterns = [
    path('todo/', include(router.urls),name = 'todos'),
]