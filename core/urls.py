from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.sitemaps import TestimonialSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'maps':TestimonialSitemap
}




urlpatterns = [
    path('trademgmt/', admin.site.urls),
    path('',include('pages.urls')),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
    path('tinymce/', include('tinymce.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 

