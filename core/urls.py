from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView  # Importe a classe TemplateView para lidar com visualizações baseadas em modelo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfil/', include('perfil.urls')),
    path('extrato/', include('extrato.urls')),
    path('planejamento/', include('planejamento.urls')),
    path('contas/', include('contas.urls')),
    path('', lambda request: redirect('perfil/home')),
    # Adicione uma visualização de página não encontrada
    path('404/', TemplateView.as_view(template_name='404.html'), name='page_not_found'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
