from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from django.utils import timezone
from blog.forms import PostForm

from django.urls import reverse_lazy
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView )
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

# Create your views here.


class PostListView(ListView):
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    ordering = ['-created_date']
    model = Post



class PostDetailView(DetailView):
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'
    model = Post

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Inclure request.FILES
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post créé avec succès.')
            return redirect('blogs:post_list')
    else:
        form = PostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})

def delete_post(request, id):
    Post(id = id).delete()
    return redirect('blogs:post_list')



