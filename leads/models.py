from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import OneToOneField


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=15)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.SET_DEFAULT, default="Unassigned")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.username


def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)