
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Tiket(models.Model):
    TiketState = [
        (1, 'in progress'),
        (2, 'resolved'),
        (3, 'frozen')
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=255)
    state = models.IntegerField(('status'), choices=TiketState, default=1, blank=True)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username


class TiketMessage(models.Model):
    ticket = models.ForeignKey(Tiket, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'ticket {}'.format(self.ticket)


class Answer(models.Model):
    TiketState = [
        (1, 'in progress'),
        (2, 'resolved'),
        (3, 'frozen')
    ]
    ticket = models.ForeignKey(Tiket, on_delete=models.CASCADE)
    text = models.TextField()
    state = models.IntegerField(('status'), choices=TiketState, default=1, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'answer the ticket {}'.format(self.ticket)
