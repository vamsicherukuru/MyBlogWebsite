# Generated by Django 3.0.3 on 2020-08-09 15:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0006_auto_20200809_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 9, 15, 37, 35, 228041, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 9, 15, 37, 35, 227043, tzinfo=utc)),
        ),
    ]
