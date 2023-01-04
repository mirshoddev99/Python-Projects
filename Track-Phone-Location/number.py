import phonenumbers
from phonenumbers import geocoder


def get_country_from_number(my_num):
    try:
        parse = phonenumbers.parse(my_num)
        print(geocoder.description_for_number(parse, 'en'))
    except:
        print("An error occurred!")


my_number = "+821067881928"
get_country_from_number(my_number)

my_number = "+998912413425"
get_country_from_number(my_number)