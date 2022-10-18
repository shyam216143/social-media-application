# Generated by Django 4.1 on 2022-10-18 09:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_social_app', '0043_alter_post_posttags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='like_count',
            new_name='likeCount',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='date_last_modified',
        ),
        migrations.AddField(
            model_name='comment',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='dateLastModified',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
