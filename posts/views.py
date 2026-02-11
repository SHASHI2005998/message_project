from django.shortcuts import render
from .models import Posts
from django.views.generic import ListView
# Create your views here.
class HomePageView(ListView):
    model=Posts
    template_name='home.html'
    context_object_name='all_posts_list'