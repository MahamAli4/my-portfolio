from django.shortcuts import render
from django.db.models import Sum
from projects.models import Project
from portfolio.models import Skill, Statistic, Education, Experience
from testimonials.models import Testimonial
from .models import VisitorCount
from datetime import date

def index(request):
    """Home page view"""
    # Get featured projects
    featured_projects = Project.objects.filter(featured=True)[:3]
    
    # Get skills for preview
    skills_preview = Skill.objects.all()[:6]
    
    # Get featured testimonials
    testimonials = Testimonial.objects.filter(is_featured=True, approved=True)[:3]
    
    # Get statistics
    statistics = Statistic.objects.filter(is_active=True)[:4]
    
    # Update visitor count
    today = date.today()
    visitor, created = VisitorCount.objects.get_or_create(date=today)
    visitor.count += 1
    visitor.save()
    
    # Calculate total visitors
    total_visitors = VisitorCount.objects.aggregate(total=Sum('count'))['total'] or 0
    
    # Get education and experience
    education = Education.objects.all()
    experience = Experience.objects.all()

    context = {
        'featured_projects': featured_projects,
        'skills_preview': skills_preview,
        'testimonials': testimonials,
        'statistics': statistics,
        'total_visitors': total_visitors,
        'education': education,
        'experience': experience,
    }
    return render(request, 'home/index.html', context)

def about(request):
    """About page view"""
    skills = Skill.objects.all()
    statistics = Statistic.objects.filter(is_active=True)
    
    context = {
        'skills': skills,
        'statistics': statistics,
    }
    return render(request, 'home/about.html', context)

def skills(request):
    """Skills page view"""
    skills = Skill.objects.all()
    return render(request, 'home/skills.html', {'skills': skills})

def custom_404(request, exception):
    """Custom 404 page"""
    return render(request, '404.html', status=404)

def custom_500(request):
    """Custom 500 page"""
    return render(request, '500.html', status=500)