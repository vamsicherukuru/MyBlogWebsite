from django import forms
from ls.models import (BlogPost,BlogComment,Feedback, NewsPost,NewsComment,
 TechPost,TechComment, EntertainmentPost,EntertainmentComment)

class BlogPostForm(forms.ModelForm):
    class Meta():
        model = BlogPost
        fields = '__all__'

class BlogCommentForm(forms.ModelForm):
    class Meta():
        model = BlogComment
        fields = ('commentor_name','comment_text')
class FeedbackForm(forms.ModelForm):
    class Meta():
        model = Feedback
        fields = '__all__'

class TechPostForm(forms.ModelForm):
    class Meta():
        model = TechPost
        fields = '__all__'

class TechCommentForm(forms.ModelForm):
    class Meta():
        model = TechComment
        fields = ('commentor_name','comment_text')
class EntertainmentPostForm(forms.ModelForm):
    class Meta():
        model = EntertainmentPost
        fields = '__all__'

class EntertainmentCommentForm(forms.ModelForm):
    class Meta():
        model = EntertainmentComment
        fields = ('commentor_name','comment_text')
class NewsPostForm(forms.ModelForm):
    class Meta():
        model = NewsPost
        fields = '__all__'

class NewsCommentForm(forms.ModelForm):
    class Meta():
        model = NewsComment
        fields = ('commentor_name','comment_text')
