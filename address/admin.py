from django.contrib import admin

from address.models import *


admin.site.register(Address)
admin.site.register(City)
admin.site.register(State)
admin.site.register(PostalCode)
admin.site.register(Country)
