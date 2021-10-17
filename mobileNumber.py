import phonenumbers

# use below case to install the phonenumbers module
# pip install phonenumbers

from phonenumbers import carrier, geocoder, timezone


print("Enter the mobile number with the country ID")

mobileNumber=input("Ex +129876543210\n")

mobileNumber = phonenumbers.parse(mobileNumber)

# turning in timezone of the phone number

print (timezone.time_zones_for_number(mobileNumber))

# Acquiring carrier of a phone number

print(carrier.name_for_number(mobileNumber, "en"))

# Gathering information on the region.
# Use "hi" for hindi and it also supports much more languages

print (geocoder.description_for_number(mobileNumber, "en"))

# Validating the phone number.

print("Valid cellular phone number:",phonenumbers.is_valid_number (mobileNumber))

# Making sure the number is available.

print("Checking possibility of Number :", phonenumbers.is_possible_number(mobileNumber))

