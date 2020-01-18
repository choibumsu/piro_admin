from django import forms
from .models import *


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name', 'tel', 'address')


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'photo', 'description',
                  'price', 'amount', 'customer')
