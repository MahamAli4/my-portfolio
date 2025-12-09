from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools'),
        ('soft', 'Soft Skills'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(help_text="Percentage from 1-100")
    icon = models.CharField(max_length=100, help_text="Font Awesome class name")
    image = models.ImageField(upload_to='skills/', blank=True, null=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name

class Statistic(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    count = models.PositiveIntegerField(default=0)
    suffix = models.CharField(max_length=10, default='+', blank=True)
    description = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.title}: {self.count}{self.suffix}"

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    image = models.ImageField(upload_to='education/', blank=True, null=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-order']
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    image = models.ImageField(upload_to='experience/', blank=True, null=True)
    description = models.TextField()
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-order']
    
    def __str__(self):
        return f"{self.position} at {self.company}"