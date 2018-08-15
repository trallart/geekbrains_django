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
    if value in request.GET and request.GET[value] != '0':
        name = 'checked'
        checkout = '0'
    else:
        name = ''
        checkout = '1'
    return name,  checkout, value


#-------Вызов каталога товаров-----------------------------------------------------
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
    if sort=="Size_id":
        sort_by = ['', 'selected', '']
    elif sort=='price':
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

    filter_size=[]
    for value in size_chekbox:
        if value[1] == '0':
            filter_size.append(value[2])
    if filter_size == []:
        filter_size = ['XXS', 'XS' , 'S', 'M', 'L', 'XL', 'XXL']

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
    show=int(show)
    show_by=list(range(start_show,finish_show, step_show))
    show_by.insert(show_by.index(show), 'selected')

    # Обработка кнопки ViewAll
    try:
        view = reauest.GET['view_all']
        view = int(view)
    except KeyError:
        view = 0


    #Обработка пагинатора
    try:
        page_num = reauest.GET['page']
    except KeyError:
        page_num = 1

    if view != 0:
        paginator = Paginator(Product.objects.filter(Category__name=categories_id, Size__name_size__in=filter_size).order_by(sort), show*view)
    else:
        paginator = Paginator(Product.objects.filter(Category__name=categories_id, Size__name_size__in=filter_size).order_by(sort), show)
    try:
        data=paginator.page(page_num)
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
        'data' : data,
        'category_menu': [category_catalog, categories_id],
        'category_brand': [category_brand, categories_id],
        'categories_id': categories_id,
        'size_chekbox': [XXS, XS, S, M, L, XL, XXL],
        'sortby': sort_by,
        'show_by': show_by,
    }
    # print("Печать конткнта", content)
    return render(reauest, 'mainapp/men.html', content)


#-------Вызов функции фильтрации товара по каталогу и бренду----------------------------------------------------
def catalog_filter(request, categories_id, catalog_id):
    global LINKS_MENU

    # ОБРАБОТКА ФИЛЬТРА SortBy
    if 'sort' in request.GET:
        sort = request.GET['sort']
        print('1111111111', sort)
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
        # messege = 'Вы искали сообщение: %r' % reauest.GET['show']
        # print('*' * 50, messege)
    else:
        show = '09'
    show = int(show)
    show_by = list(range(start_show, finish_show, step_show))
    show_by.insert(show_by.index(show), 'selected')


    print('+'*100)
    print(categories_id, 'Имя категории')
    print(catalog_id, 'Имя каталога')
    # Нахождение Индекса категории и каталога
    category = ProductCategory.objects.filter(name=categories_id)
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


    # Обработка категории
    # index_category = category[0].id
    data_filter = Product.objects.filter(Category__name=categories_id).all()
    lst_catalog = sorted_menu(data_filter)
    lst_brand = sorted_menu(data_filter)
    category_catalog = ProductCatalog.objects.filter(id__in=lst_catalog)
    category_brand = ProductBrand.objects.filter(id__in=lst_brand)
    print('-'*100)

    # Обработка каталога
    if catalog is not False:
        index_catalog = catalog[0].id  # id таблицы каталога
        # Фильтрация базу даннных по категории и каталогу
        data = Product.objects.filter(Category__name=categories_id, Catalog_id=index_catalog).order_by(sort)[:show]
    elif brand is not False:
        index_catalog = brand[0].id  # id таблицы каталога
        # Фильтрация базу даннных по категории и каталогу
        data = Product.objects.filter(Category__name=categories_id, Brand_id=index_catalog).order_by(sort)[:show]
    else:
        data = []


    content = {
        'title': 'products',
        'links_menu': LINKS_MENU,
        'data': data,
        'category_catalog': category_catalog,
        'category_brand': [category_brand, categories_id],
        'category_menu': [category_catalog, categories_id],
        'sortby': sort_by,
        'show_by': show_by,
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

