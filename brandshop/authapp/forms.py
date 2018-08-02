from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from authapp.models import ShopUser


class ShopUserLoginForm(forms.Form):
    model = ShopUser
    username = forms.CharField(max_length=16, required=True, label='',
                               widget=forms.TextInput(
                                   attrs={'type': 'text', 'name': 'login', 'value': '', 'placeholder': 'name',
                                          'class': 'modalDialog_My-Account_login'})
                               )

    password = forms.CharField(max_length=16, required=True, label='',
                               widget=forms.PasswordInput(
                                   attrs={'type': 'password', 'placeholder': 'password',
                                          'class': 'modalDialog_My-Account_login'})
                               )


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ['username', 'password', 'email', 'first_name', 'email', 'age', 'avatar']
    #     fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.widgets.TextInput(attrs={'type': 'text', 'name': 'username', 'value': '', 'placeholder': 'username',
                                          'class': 'modalDialog_My-Account_register'}),
            'password': forms.widgets.PasswordInput(
                attrs={'type': 'password', 'placeholder': 'password',
                       'class': 'modalDialog_My-Account_register'}),
        }
    password2 = forms.CharField(max_length=16, required=True, label='',
                               widget=forms.PasswordInput(
                                   attrs={'type': 'password', 'placeholder': 'password again',
                                          'class': 'modalDialog_My-Account_register'})
                                )


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ['username', 'password', 'email', 'first_name', 'email', 'age', 'avatar']

        def __init__(self, *args, **kwargs):
            super(ShopUserEditForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'modalDialog_My-Account_register'
                if field_name == 'password' or field_name == 'avatar':
                    field.widget = forms.HiddenInput()
                elif field_name in ['username' , 'email', 'age', 'first_name']:
                    field.widget.attrs['class'] = 'edit_data'
