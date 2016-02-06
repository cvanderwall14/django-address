from django import forms
from django.forms import ModelForm, HiddenInput
from django.conf import settings

from address.models import *


class AddressWidget(forms.TextInput):
    class Media:
        js = (
            'https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&libraries=places',
            'address/js/address.js',
        )


class AddressFormSimple(forms.Form):
    raw = forms.CharField(label='Address', widget=AddressWidget(attrs={'onFocus': 'init()'}))
    street_number = forms.CharField(widget=forms.HiddenInput(), required=False)
    street = forms.CharField(widget=forms.HiddenInput(), required=False)    
    city = forms.CharField(widget=forms.HiddenInput(), required=False)    
    state = forms.CharField(widget=forms.HiddenInput(), required=False)
    postal_code = forms.CharField(widget=forms.HiddenInput(), required=False)
    country = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    def is_valid(self):
        valid = super(AddressFormSimple, self).is_valid()
        if len(self.cleaned_data['raw']) > 1000:
            self.add_error('raw', 'Address must be less than 1,000 characters.')
        if len(self.cleaned_data['street_number']) > 50:
            self.add_error('raw','Street number must be less than 50 characters.')
        if len(self.cleaned_data['street']) > 100:
            self.add_error('raw', 'Street name must be less than 100 characters.')
        if len(self.cleaned_data['city']) > 100:
            self.add_error('raw', 'City name must be less than 100 characters.')
        if len(self.cleaned_data['state']) > 100:
            self.add_error('raw', 'State name must be less than 100 characters.')
        if len(self.cleaned_data['postal_code']) > 20:
            self.add_error('raw', 'Postal code must be less than 20 characters.')
        if len(self.cleaned_data['country']) > 100:
            self.add_error('raw', 'Country name must be less than 100 characters.')
        if self._errors:
            return False
        return True
               

    def save(self, commit=True):
        address = Address()
        address.raw = self.cleaned_data['raw']
        address.street_number = self.cleaned_data['street_number']
        address.street = self.cleaned_data['street']
        address.city, created = City.objects.get_or_create(name=self.cleaned_data['city'])
        address.state, created = State.objects.get_or_create(name=self.cleaned_data['state'])
        address.postal_code, created = PostalCode.objects.get_or_create(value=self.cleaned_data['postal_code'])
        address.country, created = Country.objects.get_or_create(name=self.cleaned_data['country'])
        if commit:
            address.save()
        return address
