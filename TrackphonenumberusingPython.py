#Use Jupytercfor the first projet
#Track phone number using Python
#pip install phonenumbers

import phonenumbers

#import geocoder
from phonenumbers import geocoder

#specify then phone number
a = input("Enter the phone number : ")
phonenumbers = phonenumbers.parse(a)

#Display the location of phone number
print(geocoder.description_for_number(phonenumber,'e'))