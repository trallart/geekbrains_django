from django.db import models
from django.conf import settings
from mainapp.models import Product

# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # Ссылка на id продукта
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime=models.DateTimeField(verbose_name='время', auto_now_add=True)

    # Получение стоимости нескольких товаров одного типа
    def _get_product_coast(self):
        return self.product.price * self.quantity

    product_cost = property(_get_product_coast)