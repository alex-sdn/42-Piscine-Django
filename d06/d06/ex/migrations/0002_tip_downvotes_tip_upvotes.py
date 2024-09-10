# Generated by Django 4.2 on 2024-09-10 17:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='downvotes',
            field=models.ManyToManyField(related_name='downvotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tip',
            name='upvotes',
            field=models.ManyToManyField(related_name='upvoted', to=settings.AUTH_USER_MODEL),
        ),
    ]
