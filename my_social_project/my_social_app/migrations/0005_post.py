# Generated by Django 4.0.7 on 2022-10-10 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_social_app', '0004_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment_count', models.IntegerField(blank=True, null=True)),
                ('content', models.CharField(blank=True, max_length=4096, null=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('date_last_modified', models.DateTimeField(blank=True, null=True)),
                ('is_type_share', models.BooleanField(default=True)),
                ('like_count', models.IntegerField(blank=True, default=0, null=True)),
                ('post_photo', models.CharField(blank=True, max_length=255, null=True)),
                ('share_count', models.IntegerField(blank=True, default=0, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('shared_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='my_social_app.post')),
            ],
        ),
    ]
