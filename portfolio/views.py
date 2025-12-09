from django.shortcuts import render
from .models import Skill, Statistic, Education, Experience

def skills(request):
    """Display all skills categorized"""
    skills = Skill.objects.filter(is_active=True).order_by('category', 'order')
    
    # Group skills by category
    skills_by_category = {}
    for skill in skills:
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)
    
    context = {
        'skills_by_category': skills_by_category,
    }
    return render(request, 'portfolio/skills.html', context)

def portfolio(request):
    """Complete portfolio page with education and experience"""
    skills = Skill.objects.filter(is_active=True)[:8]
    statistics = Statistic.objects.filter(is_active=True)
    education = Education.objects.all()
    experience = Experience.objects.all()
    
    context = {
        'skills': skills,
        'statistics': statistics,
        'education': education,
        'experience': experience,
    }
    return render(request, 'portfolio/portfolio.html', context)