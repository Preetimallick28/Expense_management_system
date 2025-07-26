from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Expense(models.Model):
    title = models.CharField(max_length=100)
    Amount = models.IntegerField()
    Credit = models.IntegerField()
    Debit = models.IntegerField()
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


