# Generated by Django 4.1 on 2022-10-10 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_social_app', '0018_alter_user_date_last_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('date_created', models.DateTimeField(auto_created=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_last_modified', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=64)),
                ('tag_use_counter', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'tags',
                'managed': False,
            },
        ),
    ]