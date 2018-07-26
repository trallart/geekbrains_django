from .models import ProductCategory, Product

# Вызов каталога товаров


data = Product.objects.all()
print(data)
content = {
    'title': 'products',
    'links_menu': LINKS_MENU,
    'data' : data
}


