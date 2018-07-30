from django import forms
from django.contrib.auth.forms import AuthenticationForm
from authapp.models import ShopUser


class ShopUserLoginForm(AuthenticationForm):

    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm,self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            print(field_name)
            field.widget.attrs['class']='form-control'