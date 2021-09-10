from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import DateTimeField, GenericIPAddressField


# choices enums
class ActionType(models.IntegerChoices):
    WITHDRAW = 1
    DISPUTE = 2

class Status(models.IntegerChoices):
    IN_PROGRESS = 0
    APPROVED = 1
    REJECTED = 2
class ActivityType(models.IntegerChoices):
    LOGED_IN = 0
    LOGED_OUT = 1
    CHANGED_PASSWORD = 2
    CHANGED_PHONE_NUMBER = 3

#models
class User(models.Model):
    username = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30)
    paypal_email = models.EmailField()


# models
class Action(models.Model):
    type = models.IntegerField(choices=ActionType.choices)
    status = models.IntegerField(choices=Status.choices)
    made_at = models.DateTimeField(auto_now_add=True)
    last_modification_at = models.DateTimeField(auto_now=True)
    made_by = models.ForeignKey('User', on_delete=models.DO_NOTHING)

class ActivityHistory(models.Model):
    last_activity_at = DateTimeField(auto_now_add=True)
    activity_type = models.IntegerField(choices=ActivityType.choices)
    ip_address = GenericIPAddressField()
    user = models.ForeignKey(User, on_delete=DO_NOTHING)

