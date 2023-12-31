from django.db import models
from profiles.models import Profile
from receivers.models import Receiver

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


# Create your models here.
class Invoice(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    number = models.CharField(max_length=150)
    completion_date = models.DateField()
    issue_date = models.DateField()
    payment_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    # if closed == True, then hide adding positions, and unable to add new ones
    closed = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag, blank=True)
    #checking changes

    def __str__(self):
        return f"Invoice number: {self.number}, pk: {self.pk}"

    def get_positions(self):
        pass

    # sum all the positions in the invoice
    def get_total_amount(self):
        pass