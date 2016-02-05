var autocomplete;
var componentForm = {
  street_number: 'short_name',
  route: 'long_name',
  locality: 'long_name',
  administrative_area_level_1: 'short_name',
  country: 'long_name',
  postal_code: 'short_name'
};
var hiddenForm = {
    'street_number': 'id_street_number',
    'route': 'id_street',
    'locality': 'id_city',
    'administrative_area_level_1': 'id_state',
    'country': 'id_country',
    'postal_code': 'id_postal_code'
};

function init() {
    var input = document.getElementById('id_address');
    autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.addListener('place_changed', fillInAddress);
}


function fillInAddress() {
  // Get the place details from the autocomplete object.
  var place = autocomplete.getPlace();

  // Clear hidden from values
  for (var field in hiddenForm) {
    document.getElementById(hiddenForm[field]).value = '';
  }
    
  // Get each component of the address from the place details
  // and fill the corresponding field on the form.
  for (var i = 0; i < place.address_components.length; i++) {
    var addressType = place.address_components[i].types[0];
    if (componentForm[addressType]) {
      var val = place.address_components[i][componentForm[addressType]];
      document.getElementById(hiddenForm[addressType]).value = val;
    }
  }
}

google.maps.event.addDomListener(window, 'load', init);
