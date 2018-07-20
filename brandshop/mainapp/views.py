from django.shortcuts import render

# Create your views here.
# Вызов главной страницы
def main(reauest):
    return render(reauest, 'mainapp/index.html')

# Вызов каталога товаров
def products(reauest):
    return render(reauest, 'mainapp/men.html')

# Вызов подробного описания товара
def single_page(reauest):
    return render(reauest, 'mainapp/single_page.html')


# Вызов страницы контактов (корзины)
def contacts(reauest):
    return render(reauest, 'mainapp/shopping_cart.html')