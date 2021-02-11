from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('blogs/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail' ),
    path('blogs/<int:pk>/comment/create', views.CommentCreateView.as_view(), name='comment-create'),
    path('blogs', views.BlogpostListView.as_view(), name='blogs'),
    # path('comment/create', views.CommentCreateView.as_view(), name='comment-create'),
]
