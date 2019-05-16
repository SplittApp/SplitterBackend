from django.db import models
from django.contrib.auth.models import User

from phone_field import PhoneField
from localflavor.us.models import USStateField, USZipCodeField


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    synapse = models.CharField(max_length=25, null=True)
    bio = models.TextField(null=True)
    profile_pic = models.ImageField(
        upload_to='./profile_pics/',
        max_length=150
    )
    facebook = models.URLField(max_length=150)
    twitter = models.URLField(max_length=150)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + 'profile'


class Detail(models.Model):
    NONE = 'N'
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    DECLINE = 'D'
    GENDER_CHOICES = (
        (NONE, 'None'),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (DECLINE, 'Decline to answer')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=NONE)
    phone = PhoneField(blank=True, help_text='Phone Number')
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = USStateField()
    country = models.CharField(max_length=25,default='USA')
    zip_code = USZipCodeField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + self.city

class Friend(models.Model):
    friender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friender')
    friended = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friended')
    status = models.IntegerField()
    blocked = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.friender.username + self.friended
