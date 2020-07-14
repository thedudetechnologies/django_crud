from django.shortcuts import render

# Create your views here.
def capture(request):
    return render(request, 'capture/index.html')

def about(request):
    return render(request, 'capture/about.html')

def services(request):
    return render(request, 'capture/services.html')

def gallery(request):
    return render(request, 'capture/gallery.html')

def blog(request):
    return render(request, 'capture/blog.html')

def contact(request):
    return render(request, 'capture/contact.html')

