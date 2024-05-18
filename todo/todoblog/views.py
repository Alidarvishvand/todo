from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.http import HttpResponse

# import todo form and models

from .forms import TodoForm
from .models import Post

class IndexTemplate(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "TODO LIST"
        context["form"] = TodoForm()
        return context
    def post(self, request):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

def remove(request, item_id):
    item = Post.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('index')


class PostListView(ListView):
    queryset = Post.objects.all()
    model = Post
    context_object_name = "posts"
    paginate_by = 1
    
    def get_queryset(self):
        posts = Post.objects.filter()
        return posts
    
