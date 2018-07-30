from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductCatalog)
admin.site.register(models.ProductBrand)
admin.site.register(models.ProductColor)
admin.site.register(models.ProductSize)
admin.site.register(models.Product)