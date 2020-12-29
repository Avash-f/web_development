from django.db import models
from kawasaki.models import Kawasaki
from customer.models import Customer
# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(auto_created=True, primary_key=True)
    kawasaki=models.ForeignKey(Kawasaki,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

    class Meta:
        db_table = "order"
