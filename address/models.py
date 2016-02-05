from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class PostalCode(models.Model):
    value = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.value


class Address(models.Model):
    street_number = models.CharField(max_length=10, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    city = models.ForeignKey(City, blank=True, null=True)
    state = models.ForeignKey(State, blank=True, null=True)
    postal_code = models.ForeignKey(PostalCode, blank=True, null=True)    
    country = models.ForeignKey(Country, blank=True, null=True)
    raw = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        txt = ''
        if self.street_number:
            txt = self.street_number
        if self.street:
            if txt:
                txt += ' '
            txt += self.street
        if self.city:
            if txt:
                txt += ', '
            txt += str(self.city)
        if self.state:
            if txt:
                txt += ', '
            txt += str(self.state)
        if self.postal_code:
            if txt:
                txt += ' '
            txt += str(self.postal_code)
        if self.country:
            if txt:
                txt += ', '
            txt += str(self.country)
        return txt
