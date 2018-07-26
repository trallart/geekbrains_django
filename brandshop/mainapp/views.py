from django.shortcuts import render
from django.http import HttpResponse

LINKS_MENU = [
        {'href': "/", 'name': 'home'},
        {'href': "products", 'name': 'men'},
        {'href': "products", 'name': 'woman'},
        {'href': "products", 'name': 'kids'},
        {'href': "products", 'name': 'accoseriese'},
        {'href': "products", 'name': 'featured'},
        {'href': "products", 'name': 'hot deals'}
        ]


# Create your views here.
# Вызов главной страницы
def main(reauest):
    global LINKS_MENU
    content = {
        'title': '',
        'for_men': 'hot deal',
        'for_woman': '30% offer',
        'for_kids': 'newarrivals',
        'accesories': 'lixirous & trendy',
        'links_menu': LINKS_MENU,
        'data': {
            'item1': {'name':'Mango people t-shirt', 'image': '/static/img/1.png', 'price': '$52.00'},
            'item2': {'name': 'Mango people t-shirt', 'image': '/static/img/2.png', 'price': '$52.00'},
            'item3': {'name': 'Mango people t-shirt', 'image': '/static/img/3.png', 'price': '$52.00'},
            'item4': {'name': 'Mango people t-shirt', 'image': '/static/img/4.png', 'price': '$52.00'},
            'item5': {'name': 'Mango people t-shirt', 'image': '/static/img/5.png', 'price': '$52.00'},
            'item6': {'name': 'Mango people t-shirt', 'image': '/static/img/6.png', 'price': '$52.00'},
            'item7': {'name': 'Mango people t-shirt', 'image': '/static/img/7.png', 'price': '$52.00'},
            'item8': {'name': 'Mango people t-shirt', 'image': '/static/img/8.png', 'price': '$52.00'}
        }
    }
    return render(reauest, 'mainapp/index.html', content)

# Вызов каталога товаров
def products(reauest):
    global LINKS_MENU
    content = {
        'title': 'products',
        'links_menu': LINKS_MENU
    }
    return render(reauest, 'mainapp/men.html', content)

# Вызов подробного описания товара
def single_page(reauest):
    global LINKS_MENU
    content ={
        'title': 'tovar',
        'links_menu': LINKS_MENU
    }
    return render(reauest, 'mainapp/single_page.html', content)


# Вызов страницы контактов (корзины)
def contacts(reauest):
    global LINKS_MENU
    content = {
        'title': 'contacts',
        'links_menu': LINKS_MENU
    }
    return render(reauest, 'mainapp/shopping_cart.html', content)

