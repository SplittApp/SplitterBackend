from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    group_icon = models.ImageField(upload_to='./group_icons', max_length=100)
    reference = models.CharField(max_length=22)
    members = models.IntegerField()
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + self.host.username

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    reference = models.CharField(max_length=22)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    open_tabs = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + self.group.name
