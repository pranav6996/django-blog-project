from django.urls import path
from . import views 
from .views import PostListView,PostDetail,PostCreateView,PostUpdateView,PostDeleteView,UserListView
urlpatterns=[
    path('',PostListView.as_view() , name="blog-home"),
    path('post/<int:pk>/',PostDetail.as_view(),name='post-detail'),
    path('user/<str:username>',UserListView.as_view(),name='user-posts'),
    path('post/new',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post-delete'),
    path('about/',views.about,name="blog-about"),
    path('testing/',views.testing,name="blog-testing"),
]
