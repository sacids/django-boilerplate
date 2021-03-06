from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    slug            = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    organization    = models.CharField(max_length=100, blank=True, null=True)
    sub_token       = models.TextField(blank=True, null=True)
    photo           = models.ImageField("Photo", upload_to="uploads/profile/", null=True, blank=True)
    email_verified  = models.BooleanField("Email verified", default=False)
    

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            instance.profile.save()

class activation_otp(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    otp             = models.CharField(max_length=6)
    created_on      = models.DateField(auto_now=True, auto_now_add=False)
    