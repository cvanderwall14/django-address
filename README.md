#Django Address

Django Address is a simple Django app to store address
data. The address form has Google Map's Autocomplete
functionality built in.

Quick start
-------------

1. Add "address" to your INSTALLED_APPS setting like this:

     INSTALLED_APPS = [
          ...
         'address',
     ]

2. Run 'python manage.py makemigrations address' and 'python manage.py migrate
   address' to create the address models.

3. To use the address form, just import 'AddressFormSimple' from address.forms.

4. Don't forget to include {{ form.media }} in the head of your html to
   activate the autocomplete Javascript.

5. You may also need to run 'python manage.py collectstatic'
