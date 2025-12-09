from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    """List all projects with filtering"""
    projects = Project.objects.all()
    
    # Get filter parameters
    category = request.GET.get('category')
    status = request.GET.get('status')
    
    if category:
        projects = projects.filter(category=category)
    if status:
        projects = projects.filter(status=status)
    
    # Get categories for filter
    categories = Project.objects.values_list('category', flat=True).distinct()
    
    context = {
        'projects': projects,
        'categories': categories,
        'selected_category': category,
        'selected_status': status,
    }
    return render(request, 'projects/projects.html', context)

def project_detail(request, slug):
    """Project detail view"""
    project = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.filter(
        category=project.category
    ).exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'projects/project_detail.html', context)