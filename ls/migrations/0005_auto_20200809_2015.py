# Generated by Django 3.0.3 on 2020-08-09 14:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0004_auto_20200809_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 9, 14, 45, 26, 931921, tzinfo=utc)),
        ),
    ]
