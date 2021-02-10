from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogger, Blogpost, Comment
from django.views import generic
from django.views.generic.edit import  CreateView, DeleteView, ModelFormMixin
# Create your views here.
def index(request):
    bloggers = Blogger.objects.all()
    context = {
        "bloggers":bloggers,
    }
    return render(request, 'index.html', context)

class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 10


class BloggerDetailView(generic.DetailView):
    model = Blogger


class BlogpostListView(generic.ListView):
    model = Blogpost
    paginate_by = 10


class BlogDetailView(generic.DetailView):
    model = Blogpost


class CommentCreateView(generic.CreateView):
    model = Comment