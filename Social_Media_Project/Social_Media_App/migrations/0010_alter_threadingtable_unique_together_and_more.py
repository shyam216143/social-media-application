# Generated by Django 4.1 on 2022-09-13 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Social_Media_App', '0009_threadingtable_messages1'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='threadingtable',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='threadingtable',
            name='first_person',
        ),
        migrations.RemoveField(
            model_name='threadingtable',
            name='second_person',
        ),
        migrations.DeleteModel(
            name='Messages1',
        ),
        migrations.DeleteModel(
            name='ThreadingTable',
        ),
    ]
