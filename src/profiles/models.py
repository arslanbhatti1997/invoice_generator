from django.db import models
from django.contrib.auth.models import User

"""
Class for the owner of the invoice
"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # blank means that the field is optional
    account_number = models.CharField(max_length=26, blank=True)
    company_name = models.CharField(max_length=220)
    company_info = models.TextField()
    # auto_now_add==True for when the object is first created
    created = models.DateTimeField(auto_now_add=True)
    # Automatically set the field to now every time the object is saved.
    # Useful for “last-modified” timestamps.
    update = models.DateTimeField(auto_now=True)

    # avatar =
    # company_logo =

    def __str__(self):
        return f"Profile of the user: {self.user.username}"