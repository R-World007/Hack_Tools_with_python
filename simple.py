import phonenumbers
from geopy.geocoders import Nominatim

# Parse the phone number
phone_number = "+959777097707"
parsed_number = phonenumbers.parse(phone_number)

# Get the GPS coordinates of the phone number
latitude = parsed_number.geo_latitude
longitude = parsed_number.geo_longitude

# Get the location of the GPS coordinates
geolocator = Nominatim(user_agent="my_app")
location = geolocator.reverse(f"{latitude}, {longitude}")

# Print the location information
print(location.address)
