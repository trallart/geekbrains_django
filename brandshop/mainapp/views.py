from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductCategory, Product, ProductCatalog, ProductBrand


LINKS_MENU = [
        {'href': "/", 'name': 'home'},
        {'href': "/products/for_men", 'name': 'men'},
        {'href': "/products/for_woman/", 'name': 'woman'},
        {'href': "/products/for_kids", 'name': 'kids'},
        {'href': "/products/accesorie", 'name': 'accoseriese'},
        {'href': "#", 'name': 'featured'},
        {'href': "#", 'name': 'hot deals'}
        ]


# Create your views here.
# Вызов главной страницы
def main(reauest):
    global LINKS_MENU
    data = Product.objects.all()[:8]
    content = {
        'title': '',
        'for_men': 'hot deal',
        'for_woman': '30% offer',
        'for_kids': 'newarrivals',
        'accesories': 'lixirous & trendy',
        'links_menu': LINKS_MENU,
        'data': data
    }
    return render(reauest, 'mainapp/index.html', content)


def sorted_menu(data):
    lst = []
    for value in data:
        try:
            lst.append(value.Catalog_id)
        except AttributeError:
            pass
        try:
            lst.append(value.Brand_id)
        except AttributeError:
            pass
    lst = list(set(lst))
    lst.sort()
    return lst



# Вызов каталога товаров
def products(reauest, categories_id='for_men'):
    global LINKS_MENU

    if categories_id=="for_woman":
        data = Product.objects.filter(Category_id=2)
        lst_catalog=sorted_menu(data)
        lst_brand=sorted_menu(data)
        category_catalog = ProductCatalog.objects.filter(id__in=lst_catalog)
        category_brand = ProductBrand.objects.filter(id__in=lst_brand)

    elif categories_id=="for_kids":
        data = Product.objects.filter(Category_id=3)
        lst_catalog = sorted_menu(data)
        lst_brand = sorted_menu(data)
        category_catalog = ProductCatalog.objects.filter(id__in=lst_catalog)
        category_brand = ProductBrand.objects.filter(id__in=lst_brand)

    elif categories_id=="accesorie":
        data = Product.objects.filter(Category_id=4)
        # В данной категории будем пока отображать все
        category_catalog = ProductCatalog.objects.all()
        category_brand = ProductBrand.objects.all()
    else:
        data = Product.objects.filter(Category_id=1)
        lst_catalog = sorted_menu(data)
        lst_brand = sorted_menu(data)
        category_catalog = ProductCatalog.objects.filter(id__in=lst_catalog)
        category_brand = ProductBrand.objects.filter(id__in=lst_brand)
        print(category_brand, 'Результаты категории бренд')

    content = {
        'title': 'products',
        'links_menu': LINKS_MENU,
        'data' : data,
        'category_catalog': category_catalog,
        'category_brand': category_brand
    }
    # print("Печать конткнта", content)
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

def admines(request):
    return render(request, 'mainapp/index.html')

