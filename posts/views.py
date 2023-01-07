from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, FormView 
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView 
from django.urls import reverse_lazy, reverse 
from .models import Post, Category
from .forms import CommentForm
from django.views import View
import logging
from django.shortcuts import render
from django.views.generic import TemplateView


logger = logging.getLogger(__name__)

class PostsListView(LoginRequiredMixin, ListView):
    logger.warning('New warning')
    model = Post
    template_name = "post_list.html"


class CommentGet(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Articlemodel = Post
    form_class = CommentForm
    template_name = "post_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse("post_detail", kwargs={"pk": post.pk})


class PostsDetailView(LoginRequiredMixin, View): 
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class PostsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Post
    fields = (
        "title",
        "body",
    )
    template_name = "post_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.is_superuser


class PostsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.is_superuser


class PostsCreateView(LoginRequiredMixin, CreateView): 
    model = Post
    template_name = "post_new.html"
    fields = ("title", "body", "category") 

    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddCategoryView(CreateView):
	model = Category
	template_name = 'add_category.html'
	fields = '__all__'
    
class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"

class CategoryClassView(TemplateView):
    template_name = "categories.html"
    def get_context_data(self, **kwargs):
        cats = kwargs.get("cats")
        category_posts = Category.objects.filter(name=cats.replace('-', ' '))
        context = {'cats':cats.replace('-', ' ').title(), 'category_posts':category_posts}
        return context