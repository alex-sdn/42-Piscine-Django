# Generated by Django 4.2 on 2024-09-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0002_tip_downvotes_tip_upvotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='can_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tip',
            name='can_downvote',
            field=models.BooleanField(default=False),
        ),
    ]
