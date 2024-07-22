from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.

# kharj
class Expense(models.Model):
    title = models.CharField(_("عنوان"), max_length=255)
    date = models.DateTimeField(_("تاریخ"))
    amount = models.BigIntegerField(_("مقدار"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
            
