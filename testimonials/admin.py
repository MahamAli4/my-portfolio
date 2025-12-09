from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_role', 'rating', 'is_featured', 'approved', 'created_at']
    list_filter = ['is_featured', 'approved', 'rating', 'created_at']
    search_fields = ['client_name', 'content']
    list_editable = ['is_featured', 'approved']
    readonly_fields = ['created_at']