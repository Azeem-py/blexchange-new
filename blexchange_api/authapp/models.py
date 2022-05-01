from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from requests import request
# Create your models here.

class CustomUser(AbstractUser):
    ownMultipleBlogs = models.BooleanField(default=False)

class Link(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    link = models.CharField(max_length=1000)
    niche = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)


class activity(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='senderid', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='receiverid', on_delete=models.CASCADE)
    sender_link = models.ForeignKey(Link, related_name='senderlinkid', on_delete=models.CASCADE)
    receiver_link = models.ForeignKey(Link, related_name='receiverlinkid', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    #type 1 = request gotten, 2 = requet sent, 3= backlink sent, 4=backlink gotten
    type = models.IntegerField()



