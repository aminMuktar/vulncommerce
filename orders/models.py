from django.db import models
from catalog.models import Product
# Create your models here.


class Order(models.Model):
    SUBMITTED=1
    PROCESSED=2
    SHIPPED=3
    CANCELED=4
    ORDER_STATUS=(
        (SUBMITTED,'submitted'),
        (PROCESSED,'processed'),
        (SHIPPED,'shipped'),
        (CANCELED,'canceled'),
    )
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    ip_address=models.GenericIPAddressField()
    city=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    status=models.IntegerField(choices=ORDER_STATUS, default=SUBMITTED)

    class Meta:
        ordering=('-created_at',)

    def __str__(self):
        return 'Order {}'.format(self.id)
    
    @property
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name='items', on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='order_items', on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)
    
    def get_cost(self):
        return self.price * self. quantity



