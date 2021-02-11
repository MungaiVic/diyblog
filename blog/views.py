from typing import get_args
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Blogger, Blogpost, Comment
from django.views import generic
from django.urls import reverse_lazy, reverse
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
    fields = ['reaction']
    success_url = reverse_lazy("blog-detail")

    def post(self, request, pk):
        Comment.objects.create(
            commenter=request.POST.get('commenter'),
            reaction=request.POST.get('reaction'),
            post=Blogpost.objects.get(id=pk),
            )
        return self.get_success_url(pk)

    def get_success_url(self, pk):
        return reverse('blog-detail', kwargs={'pk': pk})


    # def get_absolute_url(self): # new
    #     return reverse('blog-detail', args=[str(self.id)])

