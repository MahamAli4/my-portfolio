from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from projects.models import Project
from blog.models import BlogPost

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return ['home', 'about', 'skills', 'project_list', 'blog_list', 'testimonials', 'contact']

    def location(self, item):
        return reverse(item)

class ProjectSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.created_at

class BlogSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return BlogPost.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.updated_at