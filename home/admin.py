from django.contrib import admin
from .models import SiteSettings, VisitorCount

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'contact_email']
    
    def has_add_permission(self, request):
        # Allow only one instance
        if SiteSettings.objects.count() >= 1:
            return False
        return True

@admin.register(VisitorCount)
class VisitorCountAdmin(admin.ModelAdmin):
    list_display = ['date', 'count']
    readonly_fields = ['date', 'count']
    list_filter = ['date']