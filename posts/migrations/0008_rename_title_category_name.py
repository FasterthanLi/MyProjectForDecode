# Generated by Django 4.1.4 on 2022-12-29 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
    ]
