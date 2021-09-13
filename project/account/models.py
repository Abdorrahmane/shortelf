from django.db import models
from django.db.models.deletion import DO_NOTHING
from user.models import User

# choices enums
class AccountType(models.IntegerChoices):
    SHORT_LINKS_MAKER = 0
    ADD_BUYER = 1

#models
class Account(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200)
    account_type = models.IntegerField(choices=AccountType.choices)   
    user = models.ForeignKey(User, on_delete=DO_NOTHING)