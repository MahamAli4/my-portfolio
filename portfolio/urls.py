from django.urls import path
from . import views

urlpatterns = [
    path('skills/', views.skills, name='skills'),
    path('', views.portfolio, name='portfolio'),
]