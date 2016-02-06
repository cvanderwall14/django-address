from django.shortcuts import render
from django.views.generic import View
from django.conf import settings

from address.forms import AddressFormSimple
from address.models import *


class DemoView(View):
    """Demo page for address app."""
    template = 'demo.html'
    
    def get(self, request):
        form = AddressFormSimple()
        addresses = Address.objects.all()
        cities = City.objects.all()
        states = State.objects.all()
        postal_codes = PostalCode.objects.all()
        countries = Country.objects.all()
        data = {
            'form': form,
            'addresses': addresses,
            'cities': cities,
            'states': states,
            'postal_codes': postal_codes,
            'countries': countries
        }
        return render(request, self.template, data)

    def post(self, request):
        form = AddressFormSimple(request.POST)
        if form.is_valid():
            address = form.save()
        addresses = Address.objects.all()
        cities = City.objects.all()
        states = State.objects.all()
        postal_codes = PostalCode.objects.all()
        countries = Country.objects.all()        
        data = {
            'form': form,
            'addresses': addresses,
            'cities': cities,
            'states': states,
            'postal_codes': postal_codes,
            'countries': countries            
        }
        return render(request, self.template, data)

