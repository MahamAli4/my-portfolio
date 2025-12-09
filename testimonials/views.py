from django.shortcuts import render
from .models import Testimonial

def testimonials(request):
    """Display all approved testimonials"""
    testimonials = Testimonial.objects.filter(approved=True)
    
    # Separate featured testimonials
    featured = testimonials.filter(is_featured=True)
    regular = testimonials.filter(is_featured=False)
    
    context = {
        'featured_testimonials': featured,
        'regular_testimonials': regular,
    }
    return render(request, 'testimonials/testimonials.html', context)