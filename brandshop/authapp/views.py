from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm
from django.contrib import auth
from django.urls import reverse
from mainapp.views import LINKS_MENU



from django.http import HttpResponse

# Create your views here.
def login (request):
    title = 'вход'

    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST[ 'username' ]
        password = request.POST[ 'password' ]
        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse( 'main' ))

    content = { 'title' : title, 'login_form' : login_form, 'links_menu': LINKS_MENU}

    return render(request, 'authapp/login.html' , content)
    # return HttpResponse('Hello world')

def logout (request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))