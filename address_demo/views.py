from django.shortcuts import render
from django.views.generic import View
from django.conf import settings

from address.forms import AddressFormSimple


class DemoView(View):
    """Demo page for address app."""
    template = 'demo.html'
    
    def get(self, request):
        form = AddressFormSimple()
        data = {
            'form': form,
            'GOOGLE_API_KEY': settings.GOOGLE_API_KEY,
        }
        return render(request, self.template, data)

