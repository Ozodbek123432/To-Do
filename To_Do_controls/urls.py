# # To_Do_controls/urls.py   (loyihaning asosiy urls.py)
# from django.contrib import admin
from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include("accaounts.urls")),
#     path("todo/", include("ToDo_beckend.urls")),
#     path('', home),
#
# ]
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("""
    <h1 style="text-align:center; margin-top:100px; color:green;">
        SAYT JONLI ISHLAYAPTI! 
    </h1>
    <p style="text-align:center; font-size:20px;">
        Railway’da muvaffaqiyatli deploy qilindi!<br><br>
        Admin panel: <a href="/admin">/admin</a><br><br>
        <a href="/todo">/</a><br><br>
        Keyingi qadamlar uchun tayyor!
    </p>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),   # asosiy sahifa – hech qanday app kerak emas
    path("todo/", include("ToDo_beckend.urls")),
]