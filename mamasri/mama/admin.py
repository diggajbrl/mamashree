from django.contrib import admin
from django.db.models import fields
from django.urls import reverse
from django.contrib.sites.models import Site
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
    
admin.site.unregister(Site)
@admin.register(Site)
class SafeSiteAdmin(SingletonAdminMixin, admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    
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

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')
    search_fields = ('email', 'date')
    list_filter = ('date',)
    actions = ['export_emails_txt']
    
    @admin.action(description="Download Subscriber")
    def export_emails_txt(self, request, queryset):
        if not queryset.exists():
            self.message_user(request, "No emails selected", level='warning')
            return
        
        emails = list(queryset.values_list('email', flat=True))
        content = f"Total: {len(emails)} emails\n\n" + '\n'.join(emails)
        
        response = HttpResponse(content, content_type='text/plain; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="Subscriber.txt"'
        return response

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phoneNumber', 'collegeName', 'status', 'createdDate', 'updatedDate')
    search_fields = ('name', 'email', 'phoneNumber', 'status', 'collegeName')
    list_filter = ('status', 'collegeName', 'createdDate')
    date_hierarchy = 'createdDate'
    ordering = ('-createdDate',)
    readonly_fields = ('cunselor', 'createdDate', 'updatedDate')

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'email', 'phoneNumber', 'collegeName')
        }),
        ('Additional Information', {
            'fields': ('status', 'note'),
            'classes': ('collapse',)
        }),
        ('Read-only Fields', {
            'fields': ('cunselor', 'createdDate', 'updatedDate'),
            'classes': ('collapse',)
        }),
    )

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     # Display fields in list view
#     list_display = ('name', 'email', 'phoneNumber', 'collegeName', 'status', 'createdDate')
    
#     # Enable filtering by these fields
#     list_filter = ('status', 'createdDate', 'collegeName')
    
#     # Search functionality for these fields
#     search_fields = ('name', 'email', 'phoneNumber', 'collegeName')
    
#     # Fields to display in edit/create form
#     fieldsets = (
#         ('Basic Information', {
#             'fields': ('name', 'email', 'phoneNumber', 'collegeName')
#         }),
#         ('Additional Information', {
#             'fields': ('status', 'note'),
#             'classes': ('collapse',)  # Makes this section collapsible
#         }),
#         ('Read-only Fields', {
#             'fields': ('cunselor', 'createdDate', 'updatedDate'),
#             'classes': ('collapse',)
#         }),
#     )
    
#     # Make these fields read-only
#     readonly_fields = ('cunselor', 'createdDate', 'updatedDate')
    
#     # Enable date-based drilldown navigation
#     date_hierarchy = 'createdDate'
    
#     # Default ordering
#     ordering = ('-createdDate',)  # newest first
    
#     # Add quick edit for status in list view
#     list_editable = ('status',)
    
#     # Number of items per page
#     list_per_page = 25
    
#     # Custom admin actions
#     actions = ['mark_as_active', 'mark_as_inactive']
    
#     def mark_as_active(self, request, queryset):
#         queryset.update(status='Active')
#     mark_as_active.short_description = "Mark selected students as Active"
    
#     def mark_as_inactive(self, request, queryset):
#         queryset.update(status='Inactive')
#     mark_as_inactive.short_description = "Mark selected students as Inactive"
    
#     # Customize how fields are displayed in admin
#     def get_readonly_fields(self, request, obj=None):
#         # Make all fields read-only for view-only users
#         if request.user.is_superuser:
#             return self.readonly_fields
#         return self.readonly_fields + ('name', 'email', 'phoneNumber', 'collegeName')