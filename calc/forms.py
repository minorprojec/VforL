from django import forms
from .models import *

class Shop_details(forms.ModelForm):
    shop_owner_name = forms.CharField(widget=forms.TextInput(), max_length=100)
    shop_name = forms.CharField(widget=forms.TextInput(), max_length=100)
    address = forms.CharField(widget=forms.TextInput(), max_length=500)
    contact_no = forms.CharField(widget=forms.TextInput(), max_length=500)
    home_delievery = forms.BooleanField()
    description = forms.CharField(widget=forms.TextInput())
    image = forms.ImageField()

    class Meta():
        model = Shop
        fields = ['shop_owner_name','shop_name','address','contact_no','home_delievery','description','image']


