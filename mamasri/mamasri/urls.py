from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from mama.sitemap import ScholarshipSitemap, ArticleSitemap, StorageSitemap
from mama.views import robots, index, scholarship, article

sitemaps = {
    'scholarships': ScholarshipSitemap(),
    'articles': ArticleSitemap(),
    'storage': StorageSitemap()
}

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path("robots.txt", robots, name='robots'),
    path('<slug:slug>/', article, name="article"),
    path('docs/<slug:slug>/', scholarship, name="docs"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
