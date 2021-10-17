# phonenumbers
<h2>Python is a very powerful language and also very rich in libraries.
Phonenumbers are one of the modules that provides numerous features like providing basic information about a phone number,
validation of a phone number etc.</h2>
Here, we will learn how to use phonenumbers module just by writing simple Python programs. 

First use the below command to install required module.

    pip install phonenumbers

Some of the use cases are,
__Get Timezone:__
*Here is the simple Python program to get the timezone of a phone number using phonenumbers module.
First, we do parse the string input to phonenumber format, and then we use an inbuilt function to get the timezone of a user.
It gives the output for valid numbers only,so do check if there is no relevant output.*

**ex: timezone.time_zones_for_number(mobileNumber)**


__Carrier and Region of a Phone Number:__
*Here we will learn how to find the carrier and region of a phone number using the geocoder and carrier functions of this module.Here we can choose multiple languages to display the result.*

**ex for carrier : carrier.name_for_number(mobileNumber, "en")
ex for region: geocoder.description_for_number(mobileNumber, "hi")**


Validation of a phone number:
*A simple python program, to check whether a given phone number is valid or not (e.g. it’s in an assigned exchange), and to check whether a given phone number is possible or not (e.g. it has the right number of digits).*

**ex: phonenumbers.is_valid_number (mobileNumber)**


    Test output:
    Enter the mobile number with the country ID
    Ex +129876543210
    
    +91xxxxxxxxxx
    ('Asia/Calcutta',)
    Reliance Jio
    भारत
    Valid cellular phone number: True
    Checking possibility of Number : True


