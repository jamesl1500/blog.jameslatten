from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def HomePage(request):
    template_name = "index.html"

    return render(request, template_name)

def Resume(request):
    template_name = "resume.html"

    return render(request, template_name)

def ContactMe(request):
    template_name = "resume.html"

    return render(request, template_name)