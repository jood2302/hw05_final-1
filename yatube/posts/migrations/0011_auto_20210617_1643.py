# Generated by Django 2.2.6 on 2021-06-17 13:43

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20210617_1642'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='not_yourself_follow',
        ),
        
    ]
