from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    SPLIT_TYPE_CHOICES = [('equal', 'Equal'), ('percentage', 'Percentage'), ('custom', 'Custom')]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="expenses")
    split_type = models.CharField(max_length=20, choices=SPLIT_TYPE_CHOICES, default='equal')
    date = models.DateField(auto_now_add=True)
    receipt_image = models.ImageField(upload_to='receipts/', blank=True, null=True)

    def __str__(self):
        return f"{self.amount} - {self.category.name}"


class Settlement(models.Model):
    PAYMENT_STATUS_CHOICES = [('pending', 'Pending'), ('completed', 'Completed')]

    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    settlement_method = models.CharField(max_length=50, blank=True)
    due_date = models.DateField()

    def __str__(self):
        return f"Settlement - {self.payment_status}"


class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name="groups")

    def __str__(self):
        return self.name
