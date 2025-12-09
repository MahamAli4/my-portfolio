from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'status', 'created_at']
    list_filter = ['category', 'featured', 'status', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['featured', 'status']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]