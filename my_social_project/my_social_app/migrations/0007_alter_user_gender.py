# Generated by Django 4.1 on 2022-10-10 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_social_app', '0006_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('0', 'None'), ('1', 'Male'), ('2', 'Female'), ('3', 'Transgender')], default='0', max_length=16),
        ),
    ]