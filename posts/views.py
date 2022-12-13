from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView  
from django.urls import reverse_lazy 
from .models import Post

class PostsListView(ListView):
    model = Post
    template_name = "article_list.html"
