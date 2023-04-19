import phonenumbers

# Parse the phone number
phone_number = "+959777097707"
parsed_number = phonenumbers.parse(phone_number)

# Check if the phone number has GPS data
if parsed_number.HasField("extension"):
    print(parsed_number.extension)
else:
    print("GPS data not available")
