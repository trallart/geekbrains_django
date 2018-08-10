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

# функция обработки чекбоксов Size на сайте
def checkbox_size(request, value):
    print('*'*50, value)
    if value in request.GET and value=='1':
        name = 'checked'
        value= '1'
    else:
        name = ''
        value = '0'
    return name, value



# Вызов каталога товаров
def products(reauest, categories_id='for_men'):
    global LINKS_MENU

    # Обработка фильтра SortBy
    if 'sort' in reauest.GET:
        sort = reauest.GET['sort']
        messege = 'Вы искали сообщение: %r' % reauest.GET['sort']
        print('*' * 50, messege)
    else:
        sort = 'name'
        print('*'*100)

    if sort=="Size_id":
        sort_by = ['', 'selected', '']
    elif sort=='price':
        sort_by = ['', '', 'selected']
    else:
        sort_by = ['selected', '', '']

    # if 'size' in reauest.GET:


    XSS = checkbox_size(reauest, 'XSS')
    XS = checkbox_size(reauest, 'XS')
    S = checkbox_size(reauest, 'S')
    M = checkbox_size(reauest, 'M')
    L = checkbox_size(reauest, 'L')
    XL = checkbox_size(reauest, 'XL')
    XXL = checkbox_size(reauest, 'XXL')

    size_chekbox = [XSS, XS, S, M, L, XL, XXL]

    print('Значения чекбоксов', size_chekbox)




    if categories_id=="for_woman":
        data = Product.objects.filter(Category_id=2).order_by(sort)
        lst_catalog=sorted_menu(data)
        lst_brand=sorted_menu(data)
        category_catalog = ProductCatalog.objects.filter(id__in=lst_catalog)
        category_brand = ProductBrand.objects.filter(id__in=lst_brand)


    elif categories_id=="for_kids":
        data = Product.objects.filter(Category_id=3).order_by(sort)
        lst_catalog = sorted_menu(data)
        lst_brand = sorted_menu(data)
        category_catalog = ProductCatalog.objects.filter(id__in=lst_catalog)
        category_brand = ProductBrand.objects.filter(id__in=lst_brand)


    elif categories_id=="accesorie":
        data = Product.objects.filter(Category_id=4).order_by(sort)
        # В данной категории будем пока отображать все
        category_catalog = ProductCatalog.objects.all()
        category_brand = ProductBrand.objects.all()

    else:
        data = Product.objects.filter(Category_id=1).order_by(sort)
        lst_catalog = sorted_menu(data)
        lst_brand = sorted_menu(data)
        category_catalog = ProductCatalog.objects.filter(id__in=lst_catalog)
        category_brand = ProductBrand.objects.filter(id__in=lst_brand)



    content = {
        'title': 'products',
        'links_menu': LINKS_MENU,
        'data' : data,
        'category_menu': [category_catalog, categories_id],
        'category_brand': [category_brand, categories_id],
        'categories_id': categories_id,
        'size_chekbox': [XSS, XS, S, M, L, XL, XXL],
        'sortby': sort_by,
    }
    # print("Печать конткнта", content)
    return render(reauest, 'mainapp/men.html', content)


def catalog_filter(request, categories_id, catalog_id):
    global LINKS_MENU
    print('+'*100)
    print(categories_id, 'Имя категории')
    print(catalog_id, 'Имя каталога')
    # Нахождение Индекса категории и каталога
    catalog = ProductCatalog.objects.filter(name_catalog=catalog_id)
    print(catalog)
    category = ProductCategory.objects.filter(name=categories_id)
    print(category)
    index_catalog=catalog[0].id
    index_category=category[0].id
    print(index_catalog, index_category)


    # Фильтрация базу даннных по категории и каталогу
    data = Product.objects.filter(Category_id=index_category, Catalog_id=index_catalog)
    print(data, 'Данные по 2-м фильтрам')
    # Формирование списка каталога
    data_filter = Product.objects.filter(Category_id=index_category)
    print(data_filter, 'Фильтр данных по категории')
    lst_catalog=sorted_menu(data_filter)
    lst_brand=sorted_menu(data_filter)
    category_catalog = ProductCatalog.objects.filter(id__in=lst_catalog)
    category_brand = ProductBrand.objects.filter(id__in=lst_brand)

    content = {
        'title': 'products',
        'links_menu': LINKS_MENU,
        'data': data,
        'category_catalog': category_catalog,
        'category_brand': [category_brand, categories_id],
        'category_menu': [category_catalog, categories_id],

    }
    # print("Печать конткнта", content)
    return render(request, 'mainapp/men.html', content)



def brand_filter(request, categories_id, catalog_id, brand_id):
    global LINKS_MENU
    print('-'*100)
    print(categories_id, 'Имя категории')
    print(brand_id, 'Имя каталога')
    # Нахождение Индекса категории и каталога
    brand= ProductBrand.objects.filter(name_brand=brand_id)
    category = ProductCategory.objects.filter(name=categories_id)
    index_brand=brand[0].id
    index_category=category[0].id
    print(index_brand, index_category)


    # Фильтрация базу даннных по категории и каталогу
    data = Product.objects.filter(Category_id=index_category, Brand_id=index_brand)
    print(data, 'Данные по 2-м фильтрам')
    # Формирование списка бренда
    data_filter = Product.objects.filter(Category_id=index_category)
    print(data_filter, 'Фильтр данных по категории')

    lst_catalog=sorted_menu(data_filter)
    lst_brand=sorted_menu(data_filter)
    category_catalog = ProductCatalog.objects.filter(id__in=lst_catalog)
    category_brand = ProductBrand.objects.filter(id__in=lst_brand)

    content = {
        'title': 'products',
        'links_menu': LINKS_MENU,
        'data': data,
        'category_catalog': category_catalog,
        'category_brand': [category_brand, categories_id],
        'category_menu': [category_catalog, categories_id],
    }
    # print("Печать конткнта", content)
    return render(request, 'mainapp/men.html', content)






# Вызов подробного описания товара
def single_page(reauest):
    global LINKS_MENU
    content ={
        'title': 'tovar',
        'links_menu': LINKS_MENU
    }
    return render(reauest, 'mainapp/single_page.html', content)








def admines(request):
    return render(request, 'mainapp/index.html')

