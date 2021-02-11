from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

# Create your models here.
class Blogger(models.Model):
    """Model representing a blogger."""
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    pseudonym = models.CharField(max_length=50, unique=True, null=True)
    bio = models.TextField(max_length=1000, null=False, blank=False, help_text="Some information about you would be great... ")

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse("blogger-detail", args=[str(self.id)])


    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Blogpost(models.Model):
    """Model representing a blog post."""
    title = models.CharField(max_length=200, null=False, blank=False)
    #? Foreign key used because a blog post can only have one author(blogger), but authors can have multiple blog posts
    author = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True) # Foreign key is a 'one-to-many- field. Where is it declared, that is the 'one' side
    post_date = models.DateTimeField(auto_now_add= True) # Date when it was posted
    description = models.TextField(max_length=3000, help_text="Type something amazing...") # Blog content.
    tag = models.ManyToManyField('Tag', help_text='Select a genre for this blog post')

    class Meta:
        ordering = ['post_date']
        permissions =(("can_edit_blog_post", "Edit blog post"), )

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        """
        Returns the url to access a particular blog instance.
        """
        return reverse('blog-detail', args=[str(self.id)])


class Comment(models.Model):
    """Model representing a comment."""
    # commenter = models.ForeignKey(User,null=True, on_delete=models.SET_NULL) #! This needs to be a User object
    commenter = models.CharField(max_length=200,default='commenter', null=False)
    reaction = models.TextField(max_length=500, default='' ,null=False, blank=False)
    comment_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    class Meta:
        ordering = ['comment_date']

    def __str__(self):
        """String for the commenter and the comment date"""
        return f'{self.commenter} ({self.comment_date})'


    def get_absolute_url(self):
        """Returns the url to access a particular blogpost instance"""
        return reverse("blog-detail", args=[str(self.id)])


class Tag(models.Model):
    """Model representing a blog post genre."""
    name = models.CharField(max_length=200, help_text='Enter the category of your blog post (e.g Business, self help...)')

    def __str__(self):
        """String for representing model tag/genre"""
        return self.name
