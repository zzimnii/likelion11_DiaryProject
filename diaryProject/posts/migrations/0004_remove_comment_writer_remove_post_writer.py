# Generated by Django 4.2.3 on 2023-07-27 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment_writer_post_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='post',
            name='writer',
        ),
    ]