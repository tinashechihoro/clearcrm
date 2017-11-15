
from django.db import models
from django.contrib.auth.models import User

class Subscriber(models.Model):
    user_rec = models.ForeignKey(User)
    address_one = models.CharField(max_length=100,help_text='your first address')
    address_two = models.CharField(max_length=100, blank=True,help_text='your second address')
    city = models.CharField(max_length=50,help_text=' your city')
    state = models.CharField(max_length=2, help_text='your state')
    stripe_id = models.CharField(max_length=30, blank=True,help_text='your stripe  id')

    class Meta:
        verbose_name_plural = 'subscribers'

    def __str__(self):
        return "{0} Subscription Info".format(self.user_rec)
