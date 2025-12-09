from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Testimonial(models.Model):
    RATING_CHOICES = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]
    
    client_name = models.CharField(max_length=100)
    client_role = models.CharField(max_length=100, blank=True)
    client_company = models.CharField(max_length=100, blank=True)
    client_avatar = models.ImageField(upload_to='testimonials/', blank=True)
    content = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=5,
                                validators=[MinValueValidator(1), MaxValueValidator(5)])
    project = models.CharField(max_length=200, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Testimonial from {self.client_name}"