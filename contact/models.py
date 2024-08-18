from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Contact(models.Model):
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return  self.body if self.body  else str(self.date)

    # def __str__(self):
    #     return  self.body if self.body  else str(self.date)