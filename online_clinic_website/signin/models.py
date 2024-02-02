from django.db import models


class Clinic(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.IntegerField()
    cost = models.IntegerField()

    def __str__(self):
        return self.name


class Transaction(models.Model):
    username = models.CharField(max_length=200)
    clinic_name = models.CharField(max_length=200)
    amount_paid = models.FloatField()

# This model represents a capacity increase that records the details of a request to increase the clinic's capacity
class CapacityIncrease(models.Model):
    username = models.CharField(max_length=200)
    clinic_name = models.CharField(max_length=200)
    increase_amount = models.IntegerField()


