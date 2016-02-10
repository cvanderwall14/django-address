from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Cities'
    
    def __str__(self):
        return self.name


class PostalCode(models.Model):
    value = models.CharField(max_length=20)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.value


class Address(models.Model):
    street_number = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    city = models.ForeignKey(City, blank=True, null=True)
    state = models.ForeignKey(State, blank=True, null=True)
    postal_code = models.ForeignKey(PostalCode, blank=True, null=True)    
    country = models.ForeignKey(Country, blank=True, null=True)
    raw = models.CharField(max_length=1000, blank=True, null=True)
    care_of = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Addresses'

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
        if txt:
            return txt
        else:
            return self.raw

    def save(self, *args, **kwargs):
        gmaps = googlemaps.Client(key=local_settings.GOOGLE_MAPS_KEY)
        geocode_result = gmaps.geocode(str(self))
        self.latitude = geocode_result[0]['geometry']['location']['lat']
        self.longitude = geocode_result[0]['geometry']['location']['lng']
        super(Address, self).save(*args, **kwargs)
