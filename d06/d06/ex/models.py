from django.db import models
from django.contrib.auth.models import User, Permission

class Tip(models.Model):
    content = models.CharField(max_length=512)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tips')
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='upvoted')
    downvotes = models.ManyToManyField(User, related_name='downvotes')

    def upvote(self, user):
        self.upvotes.add(user)
        self.author.profile.reputation += 5
        self.author.profile.save()

    def downvote(self, user):
        self.downvotes.add(user)
        self.author.profile.reputation -= 2
        self.author.profile.save()

    def rm_upvote(self, user):
        self.upvotes.remove(user)
        self.author.profile.reputation -= 5
        self.author.profile.save()

    def rm_downvote(self,user):
        self.downvotes.remove(user)
        self.author.profile.reputation += 2
        self.author.profile.save()

    def delete(self, *args, **kwargs):
        self.author.profile.reputation -= self.upvotes.count() * 5
        self.author.profile.reputation += self.downvotes.count() * 2
        self.author.profile.update_permissions()

        super().delete(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    can_downvote = models.BooleanField(default=False)
    reputation = models.IntegerField(default=0)

    def update_permissions(self):
        #Downvotes
        if self.reputation >= 15:
            self.can_downvote = True
        else:
            self.can_downvote = False

        #Delete
        delete_perm = Permission.objects.get(codename='delete_tip')

        if self.reputation >= 30 and not self.user.has_perm('ex.delete_tip'):
            self.user.user_permissions.add(delete_perm)
        elif self.reputation < 30 and self.user.has_perm('ex.delete_tip'):
            self.user.user_permissions.remove(delete_perm)
        
        self.save()
