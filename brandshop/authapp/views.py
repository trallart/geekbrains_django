from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from mainapp.views import LINKS_MENU


from . models import ShopUser


from django.views.generic import FormView
from . import forms




from django.http import HttpResponse

# Create your views here.
def login (request):
    title = 'вход'

    login_form = ShopUserLoginForm(data=request.POST)

    content = {'title': title, 'login_form': login_form, 'links_menu': LINKS_MENU}
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST[ 'username' ]
        password = request.POST[ 'password' ]
        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse( 'main' ))

    return render(request, 'authapp/login.html' , content)
    # return HttpResponse('Hello world')

def logout (request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    title='register'
    if request.method == "POST":
        register_form = ShopUserRegisterForm(request.POST)
        username1 = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['password2']
        if password1 is not None and password1 == password2:
            user = ShopUser.objects.create_user(username=username1,password=password1)
            user.save()
            user = auth.authenticate(username=username1, password=password1)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))

    else:
        register_form = ShopUserRegisterForm()

    content = {'title': title, 'register_form': register_form, 'links_menu': LINKS_MENU}
    return render(request, 'authapp/register.html', content)


def edit(request):
    title ='edit profile'


    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)
        content = {'title': title, 'edit_form': edit_form, 'links_menu': LINKS_MENU}
        return render(request, 'authapp/edit.html', content)




