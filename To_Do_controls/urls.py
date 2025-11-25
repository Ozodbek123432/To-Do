# To_Do_controls/urls.py   (loyihaning asosiy urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('ToDo_beckend.urls')),
]