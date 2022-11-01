from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('blog', views.PostList.as_view(), name='blog'),
    path('resume', views.Resume, name='resume'),
    path('contact_me', views.ContactMe, name='contact_me'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('certs', views.CertsPage, name='certs'),
    path('certs/<slug:slug>/', views.CertDetail.as_view(), name='cert_detail'),
]