import phonenumbers
from geopy.geocoders import Nominatim

# Parse the phone number
phone_number = "+959777097707"
parsed_number = phonenumbers.parse(phone_number)

# Get the location of the phone number's area code
geolocator = Nominatim(user_agent="my_app")
location = geolocator.geocode(parsed_number.country_code + parsed_number.area_code)

# Print the location information
print(location.address)
