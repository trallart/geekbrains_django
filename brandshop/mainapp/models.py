from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя категории', max_length=64, unique=True)
    discount = models.FloatField(verbose_name='скидка на категорию', blank=True, default=0)
    description = models.TextField(verbose_name='описание категории', blank=True)


    def __str__(self):
        return self.name

class ProductCatalog(models.Model):
    name_catalog = models.CharField(verbose_name='имя каталога', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание каталога', blank=True)

    def __str__(self):
        return self.name_catalog


class ProductBrand(models.Model):
    name_brand = models.CharField(verbose_name='имя бренда', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание брэнда', blank=True)

    def __str__(self):
        return self.name_brand


class ProductColor(models.Model):
    name_color = models.CharField(verbose_name='цвет товара', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание цвета', blank=True)

    def __str__(self):
        return self.name_color

class ProductSize(models.Model):
    name_size = models.CharField(verbose_name='цвет товара', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание размера', blank=True)

    def __str__(self):
        return self.name_size

class Product(models.Model):
    name = models.CharField(verbose_name='имя продукта', max_length=128)  # Имя продукта
    article = models.CharField(verbose_name='артикул товара', max_length=20, unique=True)  # Артикул продукта
    image = models.ImageField(verbose_name="products_images", blank=True)  # Ссылка на картинку товара
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    Category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)  # Ссылка на id категорию
    Catalog = models.ForeignKey(ProductCatalog, on_delete=models.PROTECT)  # Ссылка на id каталог
    Brand = models.ForeignKey(ProductBrand, on_delete=models.PROTECT)  # Ссылка на id бренда
    Color = models.ForeignKey(ProductColor, on_delete=models.PROTECT)  # Ссылка на id цвета
    Size = models.ForeignKey(ProductSize, on_delete=models.PROTECT)  # Ссылка на id размеров
    kolichestvo = models.PositiveIntegerField(verbose_name= 'кол-во товара', default=0)  # Колличество данного товара

    def __str__(self):
        return '{} ({})'.format(self.name, self.Category.name)

    # Определение вывода на экран по умолчанию
    class Meta:
        ordering = ["-price", "kolichestvo", "name"]
