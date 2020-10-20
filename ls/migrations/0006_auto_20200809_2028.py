# Generated by Django 3.0.3 on 2020-08-09 14:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0005_auto_20200809_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 9, 14, 58, 9, 723955, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 9, 14, 58, 9, 722902, tzinfo=utc)),
        ),
    ]