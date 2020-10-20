from django.db import models
from django.urls import reverse

from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class BlogPost(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,default='auth.User')
    Title = models.CharField(max_length=256)
    
    Description = RichTextField()
    
    photo = models.ImageField(upload_to='article_pics',default='default.png', blank=True)
    photodes = models.TextField(max_length=1000,blank=True,default='')
    photo1 = models.ImageField(upload_to='article_pics',default='default.png', blank=True)
    photo2 = models.ImageField(upload_to='article_pics',default='default.png', blank=True)
    photo3 = models.ImageField(upload_to='article_pics',default='default.png', blank=True)
    post_date = models.DateTimeField(auto_now_add=True)

    
    

    def __str__(self):
        return self.Title
    def get_absolute_url(self):
        return reverse("ls:astroblog")

class BlogComment(models.Model):
    Post = models.ForeignKey(BlogPost,related_name='blogcomments',null=True,on_delete=models.CASCADE)
    commentor_name = models.CharField(max_length=200)
    comment_text = RichTextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.commentor_name
    def get_absolute_url(self):
        return reverse("ls:astroblog")

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    feedback = RichTextField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("ls:home")
        
class NewsPost(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,default='auth.User')
    Title = models.CharField(max_length=256)
    
    Description = RichTextField()
    
    photo = models.ImageField(upload_to='article_pics',default='default.png', blank=True)
    photodes = models.TextField(max_length=1000,blank=True,default='')
    photo1 = models.ImageField(upload_to='article_pics',default='default.png', blank=True)
    photo2 = models.ImageField(upload_to='article_pics',default='default.png', blank=True)
    photo3 = models.ImageField(upload_to='article_pics',default='default.png', blank=True)
    post_date = models.DateTimeField(auto_now_add=True)

    
    

    def __str__(self):
        return self.Title
    def get_absolute_url(self):
        return reverse("ls:news")

class NewsComment(models.Model):
    Post = models.ForeignKey(NewsPost,related_name='newscomments',null=True,on_delete=models.CASCADE)
    commentor_name = models.CharField(max_length=200)
    comment_text = RichTextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.commentor_name
    def get_absolute_url(self):
        return reverse("ls:news")



class TechPost(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,default='auth.User')
    Title = models.CharField(max_length=256)
    
    Description = RichTextField()
    
    photo = models.ImageField(upload_to='article_pics',default='default.png', blank=True)
    photodes = models.TextField(max_length=1000,blank=True,default='')
    photo1 = models.ImageField(upload_to='article_pics',default='default.png', blank=True)
    photo2 = models.ImageField(upload_to='article_pics',default='default.png', blank=True)
    photo3 = models.ImageField(upload_to='article_pics',default='default.png', blank=True)
    post_date = models.DateTimeField(auto_now_add=True)

    
    

    def __str__(self):
        return self.Title
    def get_absolute_url(self):
        return reverse("ls:technology")

class TechComment(models.Model):
    Post = models.ForeignKey(TechPost,related_name='techcomments',null=True,on_delete=models.CASCADE)
    commentor_name = models.CharField(max_length=200)
    comment_text = RichTextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.commentor_name
    def get_absolute_url(self):
        return reverse("ls:technology")

class EntertainmentPost(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,default='auth.User')
    Title = models.CharField(max_length=256)
    
    Description = RichTextField()
    
    photo = models.ImageField(upload_to='article_pics',default='default.png', blank=True)
    photodes = models.TextField(max_length=1000,blank=True,default='')
    photo1 = models.ImageField(upload_to='article_pics',default='default.png', blank=True)
    photo2 = models.ImageField(upload_to='article_pics',default='default.png', blank=True)
    photo3 = models.ImageField(upload_to='article_pics',default='default.png', blank=True)
    post_date = models.DateTimeField(auto_now_add=True)

    
    

    def __str__(self):
        return self.Title
    def get_absolute_url(self):
        return reverse("ls:entertainment")

class EntertainmentComment(models.Model):
    Post = models.ForeignKey(EntertainmentPost,related_name='entertainmentcomments',null=True,on_delete=models.CASCADE)
    commentor_name = models.CharField(max_length=200)
    comment_text = RichTextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.commentor_name
    
    def get_absolute_url(self):
        return reverse("ls:entertainment")


