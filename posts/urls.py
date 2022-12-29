from django.urls import path

from .views import (
    PostsListView,
    PostsDetailView,
    PostsUpdateView,
    PostsDeleteView,
    PostsCreateView,
    AddCategoryView,
    CategoryView,
)

urlpatterns = [
    path("<int:pk>/", PostsDetailView.as_view(), name="post_detail"),
    path("<int:pk>/edit/", PostsUpdateView.as_view(), name="post_edit"),
    path("<int:pk>/delete/", PostsDeleteView.as_view(), name="post_delete"),
    path("new/", PostsCreateView.as_view(), name="post_new"), 
    path("", PostsListView.as_view(), name="post_list"),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
     path('category/<str:cats>/', CategoryView, name='category'),
]


