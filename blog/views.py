from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogger, Blogpost

# Create your views here.
def index(request):
    bloggers = Blogger.objects.all()
    context = {
        "bloggers":bloggers,
    }
    return render(request, 'index.html', context)