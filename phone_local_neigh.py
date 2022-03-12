import phonenumbers
from phonenumbers import geocoder

phone = input('Inform the phone number like format :+55 ()xxxxxxxx without separators: ')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))
