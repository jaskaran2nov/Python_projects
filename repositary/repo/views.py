from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    return render(request,'index.html')

def searchpost(request):
    if request.method=="POST":
        query=request.POST["search"]
        a=Post.objects.filter(titel=query)

class PostView(ListView):
    model =Post
    template_name ="posts.html"
    ordering=['-id']

class MakePost(CreateView):
    model =Post
    form_class =PostForm
    template_name='add_post.html'

class ViewPost(DetailView):
    model =Post
    template_name ="view_posts.html"

class EditView(UpdateView):
    model= Post
    form_class=PostForm
    template_name='edit_post.html'

class RemovePost(DeleteView):
    model=Post
    template_name='delet_post.html'
    success_url=reverse_lazy('posts')
