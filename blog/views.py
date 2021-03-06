from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Blogger, Blogpost, Comment
from django.views import generic
from django.views.generic.edit import  CreateView, DeleteView, ModelFormMixin
from django.urls import reverse_lazy, reverse

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

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context["blogpost"] = get_object_or_404(Blogpost, pk = self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """ Add Author and associated blog before saving"""
        # Add logged in user as the commenter
        form.instance.commenter = self.request.user
        # Associate the comment with the blogpost id
        form.instance.blogpost = get_object_or_404(Blogpost.post_set.id, pk = self.kwargs['pk'])
        # print(form.instance.blogpost.id)
        # Call super class form validation behavior
        return super(CommentCreateView, self).form_valid(form)


    def get_success_url(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        return reverse(context(pk=self.kwargs['pk']))
