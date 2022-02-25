from django.db import models
from django.contrib.auth.models import User
from orders.models import Order
# Create your models here.

class UserProfile(Order):
    user=models.OneToOneField(User,unique=True,on_delete=models.CASCADE)

    def __str__(self):
        return 'User profile for:'+self.user.email

