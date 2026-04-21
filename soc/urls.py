from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔥 todas as rotas vão para a app SecurityOps
    path('', include('SecurityOps.urls')),
]

# 🔥 arquivos de mídia (uploads de imagens)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)