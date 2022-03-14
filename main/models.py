from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=20, blank=True)
    lastname = models.CharField(max_length=20, blank=True)
    email = models.EmailField('email address', blank=True)
    photo = models.ImageField(max_length=100, blank=True)
    country = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/main/img/user_not_img.png"
