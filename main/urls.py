from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-submit/', views.contact_submit, name='contact_submit'),
    path('upload-file/', views.upload_file, name='upload_file'),
]

