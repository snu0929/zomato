from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = (
        ('received', 'Received'),
        ('preparing', 'Preparing'),
        ('completed', 'Completed'),
    )

    customer_name = models.CharField(max_length=100)
    dishes = models.ManyToManyField(Dish)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='received')

    def __str__(self):
        return f"Order by {self.customer_name}"
