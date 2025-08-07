from django.db import models

class Order(models.Model):
    provider_id = models.CharField(max_length=100)
    order_date = models.DateField(auto_now_add=True)
    
class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=100)
    quantity = models.DecimalField(decimal_places=2, max_digits=100)
    price = models.DecimalField(decimal_places=2, max_digits=100)