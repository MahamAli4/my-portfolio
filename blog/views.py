from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import BlogPost, BlogCategory

def blog_list(request):
    """List all blog posts with pagination"""
    posts_list = BlogPost.objects.filter(status='published')
    
    # Search functionality
    query = request.GET.get('q')
    if query:
        posts_list = posts_list.filter(
            Q(title__icontains=query) |
            Q(excerpt__icontains=query) |
            Q(content__icontains=query)
        )
    
    # Category filter
    category_slug = request.GET.get('category')
    if category_slug:
        posts_list = posts_list.filter(category__slug=category_slug)
    
    # Pagination
    paginator = Paginator(posts_list, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    # Get categories
    categories = BlogCategory.objects.all()
    
    # Recent posts
    recent_posts = BlogPost.objects.filter(status='published')[:5]
    
    context = {
        'posts': posts,
        'categories': categories,
        'recent_posts': recent_posts,
        'query': query,
        'selected_category': category_slug,
    }
    return render(request, 'blog/blog_list.html', context)

def post_detail(request, slug):
    """Blog post detail view"""
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    post.increment_views()
    
    # Related posts
    related_posts = BlogPost.objects.filter(
        category=post.category,
        status='published'
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog/post_detail.html', context)