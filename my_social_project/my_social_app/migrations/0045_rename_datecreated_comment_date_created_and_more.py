# Generated by Django 4.1 on 2022-10-18 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_social_app', '0044_rename_like_count_comment_likecount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='dateCreated',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='dateLastModified',
            new_name='date_last_modified',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='likeCount',
            new_name='like_count',
        ),
    ]
