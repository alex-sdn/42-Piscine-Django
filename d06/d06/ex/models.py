from django.db import models
from django.contrib.auth.models import User

class Tip(models.Model):
    content = models.CharField(max_length=512)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tips')
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='upvoted')
    downvotes = models.ManyToManyField(User, related_name='downvotes')
