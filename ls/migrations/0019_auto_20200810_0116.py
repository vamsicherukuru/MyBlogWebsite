# Generated by Django 3.0.3 on 2020-08-09 19:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0018_auto_20200810_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=ckeditor.fields.RichTextField(),
        ),
    ]