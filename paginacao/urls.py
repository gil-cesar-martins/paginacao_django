from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]

admin.AdminSite.site_header = 'Sistema de Paginação'
admin.AdminSite.site_title = 'Paginação'
admin.AdminSite.index_title = 'Consoles Retro'