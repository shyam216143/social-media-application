# Generated by Django 4.1 on 2022-10-11 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_social_app', '0012_alter_user_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countries',
            name='name',
        ),
    ]
