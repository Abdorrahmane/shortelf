from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields.related import ForeignKey
from user.models import User

# choices enums
class LinkStatus(models.IntegerChoices):
    INACTIVE = 0
    PROCESSING = 1
    ACTIVE = 2
    REJECTED = 3

# models
class Link(models.Model):
    url = models.URLField()
    short_form = models.URLField()
    shortened_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=LinkStatus.choices)
    shortened_by = ForeignKey(User, on_delete=DO_NOTHING)
    
    
class Visit(models.Model):
    visitor_ip = models.GenericIPAddressField()
    is_bot = models.BooleanField(default=False)
    visit_revenue = models.FloatField(0.00)
    visited_link = models.ForeignKey(Link, on_delete=DO_NOTHING)
    