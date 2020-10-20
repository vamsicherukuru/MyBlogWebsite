# Generated by Django 3.0.3 on 2020-08-10 09:54

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ls', '0019_auto_20200810_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentor_name', models.CharField(max_length=200)),
                ('comment_text', ckeditor.fields.RichTextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=256)),
                ('Description', ckeditor.fields.RichTextField()),
                ('photo', models.ImageField(blank=True, default='default.png', upload_to='article_pics')),
                ('photodes', models.TextField(blank=True, default='', max_length=1000)),
                ('photo1', models.ImageField(blank=True, default='default.png', upload_to='article_pics')),
                ('photo2', models.ImageField(blank=True, default='default.png', upload_to='article_pics')),
                ('photo3', models.ImageField(blank=True, default='default.png', upload_to='article_pics')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EntertainmentComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentor_name', models.CharField(max_length=200)),
                ('comment_text', ckeditor.fields.RichTextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntertainmentPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=256)),
                ('Description', ckeditor.fields.RichTextField()),
                ('photo', models.ImageField(blank=True, default='default.png', upload_to='article_pics')),
                ('photodes', models.TextField(blank=True, default='', max_length=1000)),
                ('photo1', models.ImageField(blank=True, default='default.png', upload_to='article_pics')),
                ('photo2', models.ImageField(blank=True, default='default.png', upload_to='article_pics')),
                ('photo3', models.ImageField(blank=True, default='default.png', upload_to='article_pics')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewsComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentor_name', models.CharField(max_length=200)),
                ('comment_text', ckeditor.fields.RichTextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=256)),
                ('Description', ckeditor.fields.RichTextField()),
                ('photo', models.ImageField(blank=True, default='default.png', upload_to='article_pics')),
                ('photodes', models.TextField(blank=True, default='', max_length=1000)),
                ('photo1', models.ImageField(blank=True, default='default.png', upload_to='article_pics')),
                ('photo2', models.ImageField(blank=True, default='default.png', upload_to='article_pics')),
                ('photo3', models.ImageField(blank=True, default='default.png', upload_to='article_pics')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TechComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentor_name', models.CharField(max_length=200)),
                ('comment_text', ckeditor.fields.RichTextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('Post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='techcomments', to='ls.NewsPost')),
            ],
        ),
        migrations.CreateModel(
            name='TechPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=256)),
                ('Description', ckeditor.fields.RichTextField()),
                ('photo', models.ImageField(blank=True, default='default.png', upload_to='article_pics')),
                ('photodes', models.TextField(blank=True, default='', max_length=1000)),
                ('photo1', models.ImageField(blank=True, default='default.png', upload_to='article_pics')),
                ('photo2', models.ImageField(blank=True, default='default.png', upload_to='article_pics')),
                ('photo3', models.ImageField(blank=True, default='default.png', upload_to='article_pics')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='newscomment',
            name='Post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='newscomments', to='ls.NewsPost'),
        ),
        migrations.AddField(
            model_name='entertainmentcomment',
            name='Post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entertainmentcomments', to='ls.EntertainmentPost'),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='Post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogcomments', to='ls.BlogPost'),
        ),
    ]
