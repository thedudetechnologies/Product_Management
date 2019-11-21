from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
    path('products/', include('man_prod.urls')),
]
