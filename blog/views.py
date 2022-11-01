from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

from .models import Post
from .models import Jobs
from .models import Certs


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class CertDetail(generic.DetailView):
    model = Certs
    template_name = 'certs_details.html'

def HomePage(request):
    template_name = "index.html"
    jobs = Jobs.objects.order_by('-job_added')

    return render(request, template_name, {'jobs': jobs})

def CertsPage(request):
    template_name = "certs.html"
    certs = Certs.objects.order_by('-created_on')

    return render(request, template_name, {'certs': certs})

def Resume(request):
    template_name = "resume.html"

    return render(request, template_name)

def ContactMe(request):
    template_name = "contact_me.html"

    return render(request, template_name)
