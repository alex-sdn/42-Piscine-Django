# Generated by Django 4.2 on 2024-09-10 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0003_tip_can_delete_tip_can_downvote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tip',
            name='can_delete',
        ),
        migrations.RemoveField(
            model_name='tip',
            name='can_downvote',
        ),
    ]
