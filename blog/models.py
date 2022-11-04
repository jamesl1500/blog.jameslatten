from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

# Post Datbase Model
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    cover = models.ImageField(upload_to='static/storage/images/', blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title

# Jobs Database Model
class Jobs(models.Model):
    job_title = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    job_desc = models.TextField()
    job_date = models.CharField(max_length=200)
    job_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-job_added']

    def __str__(self):
        return self.job_title

# Certs Database Model
CERT_STATUS = (
    (0, "Draft"),
    (1, "In Progress"),
    (2, "Obtained")
)

class Certs(models.Model):
    cert_title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    cert_subjects = models.CharField(max_length=255)
    cert_desc = models.TextField()
    cert_link = models.CharField(max_length=255)
    cert_image = models.ImageField(upload_to='static/storage/images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    cert_status = models.IntegerField(choices=CERT_STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.cert_title