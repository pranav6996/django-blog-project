from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts' #we change it to this value instead of object_list which is default to posts so that we can use it easily it isnt compulsory but we can use this to change the name to what we want
    template_name='blog/home.html'
    ordering=['-date_created']
    paginate_by=4 


class UserListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts' #we change it to this value instead of object_list which is default to posts so that we can use it easily it isnt compulsory but we can use this to change the name to what we want
    template_name='blog/user_view.html'
    ordering=['-date_created']
    paginate_by=4
    
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_created')



class PostDetail(DetailView):
    model=Post
    template_name='blog/detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields=['title','content'] #form = ModelForm(Post, fields=['title', 'content']) this will be created by django automatically
    template_name='blog/create_post.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title','content'] #form = ModelForm(Post, fields=['title', 'content']) this will be created by django automatically
    template_name='blog/create_post.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template_name='blog/post_conform_detail.html'
    success_url="/" # when the deletion operation is done succesfully this is used to redirect the user who deleted it back to the home page
    def test_func(self):
        post=self.get_object()
        if (self.request.user==post.author):
            return True
        return False




def about(request):
    return render(request,'blog/about.html',{'title':'about'})

def testing(request):
    return render(request,'blog/test.html')


# Create your views here.