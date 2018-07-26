from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product, ProductCatalog,  ProductBrand, ProductColor, ProductSize
from django.contrib.auth.models import User
import json, os

JSON_PATH = 'mainapp/json'

def loadFromJSON (file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json' ), 'r' ) as infile:
        return json.load(infile)


class Command (BaseCommand):
    def handle (self, *args, **options):
        # Работа с таблицей категория
        categories = loadFromJSON( 'ProductCategories' )
        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        # Работа с таблицей каталог
        catalogs = loadFromJSON('ProductCatalog')
        ProductCatalog.objects.all().delete()
        for catalog in catalogs:
            new_catalog = ProductCatalog(**catalog)
            new_catalog.save()

        # Работа с таблицей брэнд
        brands = loadFromJSON('ProductBrand')
        ProductBrand.objects.all().delete()
        for brand in brands:
            new_brand = ProductBrand(**brand)
            new_brand.save()

        # Работа с таблицей цвет
        colores = loadFromJSON('ProductColor')
        ProductColor.objects.all().delete()
        for color in colores:
            new_color = ProductColor(**color)
            new_color.save()

        # Работа с таблицей размер
        sizes = loadFromJSON('ProductSize')
        ProductSize.objects.all().delete()
        for size in sizes:
            new_size = ProductSize(**size)
            new_size.save()


        # Работа с таблицей продукты
        products = loadFromJSON( 'Product' )
        Product.objects.all().delete()

        for product in products:
            # Привязка к категории
            category_name = product["Category_id"]
            # Получаем категорию по имени
            _category = ProductCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            product[ 'Category_id' ] = _category.id

            # Привязка к каталогу
            catalog_name = product["Catalog_id"]
            _catalog = ProductCatalog.objects.get(name_catalog=catalog_name)
            product['Catalog_id'] = _catalog.id

            # Привязка к брэнду
            brand_name = product["Brand_id"]
            _brand = ProductBrand.objects.get(name_brand=brand_name)
            product['Brand_id'] = _brand.id

            # Привязка к цвету
            color_name = product["Color_id"]
            _color = ProductColor.objects.get(name_color=color_name)
            product['Color_id'] = _color.id

            # Привязка к размеру
            size_name = product["Size_id"]
            _size = ProductSize.objects.get(name_size=size_name)
            product['Size_id'] = _size.id

            new_product = Product(**product)
            new_product.save()