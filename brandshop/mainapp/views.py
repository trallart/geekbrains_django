from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductCategory, Product, ProductCatalog, ProductBrand

from django.core.paginator import Paginator, InvalidPage

LINKS_MENU = [
    {'href': "/", 'name': 'home'},
    {'href': "/products/for_men", 'name': 'men'},
    {'href': "/products/for_woman/", 'name': 'woman'},
    {'href': "/products/for_kids", 'name': 'kids'},
    {'href': "/products/accesorie", 'name': 'accoseriese'},
    {'href': "#", 'name': 'featured'},
    {'href': "#", 'name': 'hot deals'}
]



# КОНТРОЛЛЕР ОБРАБОТКИ ГЛАВНОЙ СТРАНИЦЫ САЙТА
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

# Функция формирования бокового меню сайта
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
    if value in request.GET and request.GET[value] != '0':
        name = 'checked'
        checkout = '0'
    else:
        name = ''
        checkout = '1'
    return name, checkout, value


# -------Вызов каталога товаров-----------------------------------------------------
# КОНТРОЛЛЕР №1 ОБРАБОТКИ СПИСКА ТОВАРОВ ПО КАТЕГОРИИ
def products(reauest, categories_id='for_men'):
    global LINKS_MENU

    # ОБРАБОТКА ФИЛЬТРА SortBy
    if 'sort' in reauest.GET:
        sort = reauest.GET['sort']
        messege = 'Вы искали сообщение: %r' % reauest.GET['sort']
        # print('*' * 50, messege)
    else:
        sort = 'name'
        # print('*'*100)
    if sort == "Size_id":
        sort_by = ['', 'selected', '']
    elif sort == 'price':
        sort_by = ['', '', 'selected']
    else:
        sort_by = ['selected', '', '']

    # ОБРАБОТКА ФИЛЬТРА SIZE (CHECKBOX)
    XXS = checkbox_size(reauest, 'XXS')
    XS = checkbox_size(reauest, 'XS')
    S = checkbox_size(reauest, 'S')
    M = checkbox_size(reauest, 'M')
    L = checkbox_size(reauest, 'L')
    XL = checkbox_size(reauest, 'XL')
    XXL = checkbox_size(reauest, 'XXL')

    size_chekbox = [XXS, XS, S, M, L, XL, XXL]

    filter_size = []
    for value in size_chekbox:
        if value[1] == '0':
            filter_size.append(value[2])
    if filter_size == []:
        filter_size = ['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL']

    # ОБРАБОТКА ФИЛЬТРА SHOW
    start_show = 3
    finish_show = 18
    step_show = 3
    if 'show' in reauest.GET:
        show = reauest.GET['show']
        # messege = 'Вы искали сообщение: %r' % reauest.GET['show']
        # print('*' * 50, messege)
    else:
        show = '09'
    show = int(show)
    show_by = list(range(start_show, finish_show, step_show))
    show_by.insert(show_by.index(show), 'selected')

    # Обработка кнопки ViewAll
    try:
        view = reauest.GET['view_all']
        view = int(view)
    except KeyError:
        view = 1

    # Обработка пагинатора
    try:
        page_num = reauest.GET['page']
    except KeyError:
        page_num = 1

    paginator = Paginator(
        Product.objects.filter(Category__name=categories_id, Size__name_size__in=filter_size).order_by(sort),
        show * view)

    try:
        data = paginator.page(page_num)
    except InvalidPage:
        data = paginator.page(1)

    # Фильтрация результатов для бокового
    data1 = Product.objects.filter(Category__name=categories_id).all()
    lst_catalog = sorted_menu(data1)
    lst_brand = sorted_menu(data1)
    category_catalog = ProductCatalog.objects.filter(id__in=lst_catalog)
    category_brand = ProductBrand.objects.filter(id__in=lst_brand)
    # print(category_brand)

    content = {
        'title': 'products',
        'links_menu': LINKS_MENU,
        'data': data,
        'category_menu': [category_catalog, categories_id],
        'category_brand': [category_brand, categories_id],
        'categories_id': categories_id,
        'size_chekbox': [XXS, XS, S, M, L, XL, XXL],
        'sortby': sort_by,
        'show_by': show_by,
    }
    # print("Печать конткнта", content)
    return render(reauest, 'mainapp/men.html', content)


# КОНТРОЛЛЕР №1 ОБРАБОТКИ СПИСКА ТОВАРОВ ПО КАТЕГОРИИ + КАТАЛОГУ И БРЭНДУ
def catalog_filter(request, categories_id, catalog_id):
    global LINKS_MENU

    # ОБРАБОТКА ФИЛЬТРА SortBy
    if 'sort' in request.GET:
        sort = request.GET['sort']
    else:
        sort = 'name'
    if sort == "Size_id":
        sort_by = ['', 'selected', '']
    elif sort == 'price':
        sort_by = ['', '', 'selected']
    else:
        sort_by = ['selected', '', '']

    # ОБРАБОТКА ФИЛЬТРА SHOW
    start_show = 3
    finish_show = 18
    step_show = 3
    if 'show' in request.GET:
        show = request.GET['show']
    else:
        show = '09'
    show = int(show)
    show_by = list(range(start_show, finish_show, step_show))
    show_by.insert(show_by.index(show), 'selected')

    # ОБРАБОТКА ФИЛЬТРА SIZE (CHECKBOX)
    XXS = checkbox_size(request, 'XXS')
    XS = checkbox_size(request, 'XS')
    S = checkbox_size(request, 'S')
    M = checkbox_size(request, 'M')
    L = checkbox_size(request, 'L')
    XL = checkbox_size(request, 'XL')
    XXL = checkbox_size(request, 'XXL')

    size_chekbox = [XXS, XS, S, M, L, XL, XXL]

    filter_size = []
    for value in size_chekbox:
        if value[1] == '0':
            filter_size.append(value[2])
    if filter_size == []:
        filter_size = ['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL']

    # Нахождение Индекса категории и каталога
    try:
        catalog = ProductCatalog.objects.filter(name_catalog=catalog_id)
        catalog[0]  # Вызывает исключение если данные не находятся в базе
    except IndexError:
        catalog = False
    try:
        brand = ProductBrand.objects.filter(name_brand=catalog_id)
        brand[0]  # Вызывает исключение если данные не находятся в базе
    except IndexError:
        # Необходимо будет вызвать, страница не найдена
        brand = False

    # Обработка категории (боковое меню сайта)
    data_filter = Product.objects.filter(Category__name=categories_id).all()
    lst_catalog = sorted_menu(data_filter)
    lst_brand = sorted_menu(data_filter)
    category_catalog = ProductCatalog.objects.filter(id__in=lst_catalog)
    category_brand = ProductBrand.objects.filter(id__in=lst_brand)
    print('-' * 100)

    # Обработка кнопки ViewAll
    try:
        view = request.GET['view_all']
        view = int(view)
    except KeyError:
        view = 1

    # Обработка пагинатора
    try:
        page_num = request.GET['page']
    except KeyError:
        page_num = 1

    # Обработка каталога
    if catalog is not False:
        # Фильтрация базу даннных по категории и каталогу
        paginator = Paginator(
            Product.objects.filter(Category__name=categories_id, Catalog__name_catalog=catalog_id,
                                   Size__name_size__in=filter_size).order_by(sort), show * view)
    elif brand is not False:
        index_catalog = brand[0].id  # id таблицы каталога
        # Фильтрация базу даннных по категории и каталогу
        paginator = Paginator(
            Product.objects.filter(Category__name=categories_id, Brand__name_brand=catalog_id,
                                   Size__name_size__in=filter_size).order_by(sort), show * view)
    else:
        paginator = []

    try:
        data = paginator.page(page_num)
    except InvalidPage:
        data = paginator.page(1)

    content = {
        'title': 'products',
        'links_menu': LINKS_MENU,
        'data': data,
        'category_catalog': category_catalog,
        'category_brand': [category_brand, categories_id],
        'category_menu': [category_catalog, categories_id],
        'size_chekbox': [XXS, XS, S, M, L, XL, XXL],
        'sortby': sort_by,
        'show_by': show_by,
    }
    return render(request, 'mainapp/men.html', content)



# Вызов подробного описания товара
def single_page(reauest):
    global LINKS_MENU
    content = {
        'title': 'tovar',
        'links_menu': LINKS_MENU
    }
    return render(reauest, 'mainapp/single_page.html', content)


def admines(request):
    return render(request, 'mainapp/index.html')
