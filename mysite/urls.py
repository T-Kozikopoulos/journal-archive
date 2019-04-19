from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('archive.urls')),
    path('user/', include('users.urls')),
]
