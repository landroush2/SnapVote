from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index, checkIdentity

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('upload/', checkIdentity),
    path('api/election/', include('canditate.api.urls')),
    path('api/elector/', include('elector.api.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)