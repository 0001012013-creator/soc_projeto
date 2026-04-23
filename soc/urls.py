from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rotas da aplicação
    path('', include('SecurityOps.urls')),
]

# 🔥 SERVIR ARQUIVOS EM DESENVOLVIMENTO
if settings.DEBUG:
    # arquivos de mídia (uploads)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # 🔥 ESSA LINHA QUE FALTAVA (CSS NÃO FUNCIONAVA POR ISSO)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'SecurityOps/static')