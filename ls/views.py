from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import (BlogPostForm,BlogCommentForm,FeedbackForm,TechPostForm,TechCommentForm
                    ,EntertainmentPostForm,EntertainmentCommentForm,NewsPostForm,NewsCommentForm)
from django.urls import reverse_lazy
# Create your views here.

class Home(TemplateView):

    template_name = 'home.html'



class AstroBlog(ListView):
    model = models.BlogPost
    context_object_name = 'post_list'
    queryset = models.BlogPost.objects.order_by('-post_date')
    template_name = 'astroblog.html'

class AstroPostDetail(DetailView):

    model = models.BlogPost
    context_object_name = 'post_detail'
    template_name = 'blog_post_detail.html'
   


class NewPostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'post_form.html'
    model = models.BlogPost
    fields = '__all__'
    template_name = 'post_form.html'
    


class AddComment(CreateView):
    model = models.BlogComment
    template_name = 'comment_form.html'
    form_class = BlogCommentForm

    def form_valid(self,form):
        form.instance.Post_id  = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('ls:astroblog')

class FeedbackView(CreateView):
    model = models.Feedback
    redirect_field_name = 'feedback_form.html'
    
    fields = '__all__'
    template_name = 'feedback_form.html'


class PostDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    redirect_field_name = 'post_confirm_delete.html'
    model = models.BlogPost
    template_name='post_confirm_delete.html'
    success_url = reverse_lazy('ls:astroblog')
########################################################

class TechBlog(ListView):
    model = models.TechPost
    context_object_name = 'post_list'
    queryset = models.TechPost.objects.order_by('-post_date')
    template_name = 'tech_list.html'

class TechPostDetail(DetailView):

    model = models.TechPost
    context_object_name = 'post_detail'
    template_name = 'tech_detail.html'
   


class TechNewPostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'tech_post_form.html'
    model = models.TechPost
    fields = '__all__'
    template_name = 'tech_post_form.html'
    


class TechAddComment(CreateView):
    model = models.TechComment
    template_name = 'tech_comment_form.html'
    form_class = TechCommentForm

    def form_valid(self,form):
        form.instance.Post_id  = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('ls:technology')

#########################################################################
class EntertainmentBlog(ListView):
    model = models.EntertainmentPost
    context_object_name = 'post_list'
    queryset = models.EntertainmentPost.objects.order_by('-post_date')
    template_name = 'entertainment_list.html'

class EntertainmentPostDetail(DetailView):

    model = models.EntertainmentPost
    context_object_name = 'post_detail'
    template_name = 'entertainment_detail.html'
   


class EntertainmentNewPostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'entertainment_post_form.html'
    model = models.EntertainmentPost
    fields = '__all__'
    template_name = 'entertainment_post_form.html'
    


class EntertainmentAddComment(CreateView):
    model = models.EntertainmentComment
    template_name = 'entertainment_comment_form.html'
    form_class = EntertainmentCommentForm

    def form_valid(self,form):
        form.instance.Post_id  = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('ls:entertainment')


##################################
class NewsList(ListView):
    model = models.NewsPost
    context_object_name = 'news_list'
    queryset = models.NewsPost.objects.order_by('-post_date')
    template_name = 'news_list.html'

class NewsPostDetail(DetailView):

    model = models.NewsPost
    context_object_name = 'post_detail'
    template_name = 'news_detail.html'
   


class NewsNewPostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'news_form.html'
    model = models.NewsPost
    fields = '__all__'
    template_name = 'news_post_form.html'
    


class NewsAddComment(CreateView):
    model = models.NewsComment
    template_name = 'news_comment_form.html'
    form_class = NewsCommentForm

    def form_valid(self,form):
        form.instance.Post_id  = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('ls:news')

