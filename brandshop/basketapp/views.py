from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product
from mainapp.views import LINKS_MENU



from django.urls import reverse

def basket(request):
    global LINKS_MENU
    data = Basket.objects.all()


    content = {
        'title': 'basket',
        'links_menu': LINKS_MENU,
        'data': data,
        'basket': basket,
    }


    return render(request, 'basketapp/shopping_cart.html', content)



def basket_add(request, pk):
    product = get_object_or_404(Product, id=pk)
    old_basket_item = Basket.objects.filter(user=request.user, product=product)
    if old_basket_item:
        old_basket_item[0].quantity += 1
        old_basket_item[0].save()
    else:
        new_basket_item = Basket(user_id=request.user.id, product_id=product.id)
        new_basket_item.quantity += 1
        new_basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # Возвращение на туже страничку, где добавляли товар

def basket_remove(request, pk):
    content = {}
    return render(request, 'basketapp/shopping_cart.html', content)

