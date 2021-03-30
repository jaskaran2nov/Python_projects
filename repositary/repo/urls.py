from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('posts',views.PostView.as_view(),name="posts"),
    path('add',views.MakePost.as_view(),name="addpost"),
    path('view_post/<int:pk>',views.ViewPost.as_view(),name='view_post'),
    path('article/edit/<int:pk>',views.EditView.as_view(),name='editpost'),
    path('article/<int:pk>/remove',views.RemovePost.as_view(),name='removepost'),
]

