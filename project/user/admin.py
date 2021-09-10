from django.contrib import admin
from user.models import Action, User, ActivityHistory

# Register your models here.
admin.site.register([User, ActivityHistory, Action])