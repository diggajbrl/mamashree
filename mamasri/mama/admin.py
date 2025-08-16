from django.contrib import admin
from django.db.models import fields
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Setting, Advertisement, Basement, Scheme, Scholarship, Article, Counselor, Student, Subscriber, Storage

class SingletonAdminMixin:
    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def changelist_view(self, request, extra_context=None):
        qs = self.model.objects.all()
        if qs.exists():
            obj = qs.first()
            return HttpResponseRedirect(
                reverse(f'admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change', args=[obj.pk])
            )
        return super().changelist_view(request, extra_context)
    
@admin.register(Setting)
class SettingAdmin(SingletonAdminMixin, admin.ModelAdmin):
    pass

@admin.register(Advertisement)
class AdsAdmin(admin.ModelAdmin):
    list_display = ('adsImage', 'adsAlt', 'adsUploadDate', 'adsEndingDate')
    search_fields = ('adsAlt',)
    list_filter = ('adsUploadDate', 'adsEndingDate')


class BasementAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'updatedDate', 'list_advertisements')
    search_fields = ('title',)
    readonly_fields = ('createdDate', 'updatedDate')

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'strip'),
        }),
        ('SEO MetaData', {
            'fields': ('seo',),
        }),
        ('Advertisement', {
            'fields': ('advertisement',),
        }),
        ('None', {
            'fields': ('createdDate', 'updatedDate')
        })
    )

    def list_advertisements(self, obj):
        return ", ".join([ad.adsAlt for ad in obj.advertisement.all()])
    list_advertisements.short_description = "Advertisements"

@admin.register(Scheme)
class SchemeAdmin(SingletonAdminMixin, BasementAdmin):
    pass

@admin.register(Scholarship)
class ScholarshipAdmin(BasementAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(BasementAdmin):
    pass

@admin.register(Counselor)
class CounselorAdmin(SingletonAdminMixin, admin.ModelAdmin):
    pass

@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'uploadDate')