from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Scheme, Scholarship, Article, Storage

class ScholarshipSitemap(Sitemap):
    changefreq = "weekly"
    priority = "0.8"

    def items(self):
        return Scholarship.objects.filter(active=True)
    
    def lastmod(self, obj):
        return obj.updatedDate
    
class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = "0.7"

    def items(self):
        return Article.objects.filter(active=True)
    
    def lastmod(self, obj):
        return obj.updatedDate
    
class StorageSitemap(Sitemap):
    changefreq = "weekly"
    priority = "0.7"

    def items(self):
        return Storage.objects.filter(active=True)

    def lastmod(self, obj):
        return obj.uploadDate