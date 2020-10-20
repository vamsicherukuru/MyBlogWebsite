from django.contrib import admin
from .models import (BlogPost,BlogComment,Feedback, NewsPost,NewsComment,
 TechPost,TechComment, EntertainmentPost,EntertainmentComment)
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(BlogComment)
admin.site.register(NewsPost)
admin.site.register(NewsComment)
admin.site.register(EntertainmentPost)
admin.site.register(EntertainmentComment)
admin.site.register(TechPost)
admin.site.register(TechComment)
admin.site.register(Feedback)
