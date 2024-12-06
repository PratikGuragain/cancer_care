from django.shortcuts import render, redirect
from .models import Contact, FileUpload
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        messages.success(request, 'Your message has been submitted.')
        return redirect('home')

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        FileUpload.objects.create(file=file)
        messages.success(request, 'File uploaded successfully.')
        return redirect('home')

