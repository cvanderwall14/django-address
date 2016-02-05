from django import forms
from django.conf import settings


class AddressWidget(forms.TextInput):
    class Media:
        js = (
            'https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&libraries=places',
            'address/js/address.js',
        )


class AddressFormSimple(forms.Form):
    address = forms.CharField(label='Address', widget=AddressWidget(attrs={'onFocus': 'init()'}))
