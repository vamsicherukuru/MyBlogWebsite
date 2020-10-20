from django import urls
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ls'

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('astroblog', views.AstroBlog.as_view(), name='astroblog'),
    path('post/<int:pk>',views.AstroPostDetail.as_view(),name='post_detail'),
    path('createPost',views.NewPostView.as_view(),name='createPost'),
    path('post/<int:pk>/comment',views.AddComment.as_view(),name='makeComment'),
    path('feedback',views.FeedbackView.as_view(),name='feedback'),
    path('delete/<int:pk>',views.PostDeleteView.as_view(),name='delete'),
    path('entertainment', views.EntertainmentBlog.as_view(), name='entertainment'),
    path('entertainmentPost',views.EntertainmentNewPostView.as_view(),name='entertainmentPost'),
    path('entertainment/<int:pk>',views.EntertainmentPostDetail.as_view(),name='entertainment_detail'),
    path('entertainment/<int:pk>/comment',views.EntertainmentAddComment.as_view(),name='entertainmentCommentAdd'),
    path('technology', views.TechBlog.as_view(), name='technology'),
    path('technology/<int:pk>',views.TechPostDetail.as_view(),name='tech_detail'),
    path('techPost',views.TechNewPostView.as_view(),name='techPost'),
    path('technology/<int:pk>/comment',views.TechAddComment.as_view(),name='TechCommentAdd'),
    path('news', views.NewsList.as_view(), name='news'),
    path('news/<int:pk>',views.NewsPostDetail.as_view(),name='news_detail'),
    path('newsPost',views.NewsNewPostView.as_view(),name='newsPost'),
    path('news/<int:pk>/comment',views.NewsAddComment.as_view(),name='NewsCommentAdd'),



    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)