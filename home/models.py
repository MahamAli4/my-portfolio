from django.db import models
from django.utils import timezone

class SiteSettings(models.Model):
    """Site-wide settings that can be changed from admin"""
    site_name = models.CharField(max_length=100, default='My Portfolio')
    site_description = models.TextField(default='Professional portfolio website')
    contact_email = models.EmailField(default='contact@example.com')
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    whatsapp_number = models.CharField(max_length=20, default='+1234567890')
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    
    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'
    
    def __str__(self):
        return self.site_name

class VisitorCount(models.Model):
    """Track website visitors"""
    date = models.DateField(default=timezone.now)
    count = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f"Visitors on {self.date}: {self.count}"