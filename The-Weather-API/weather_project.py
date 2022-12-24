import requests

API_KEY = "dd50f5b11643407190761005222412"
BASE_URL = "http://api.weatherapi.com/v1/current.json?key="

country_city = input("Enter a city or country name: ")
req_url = f"{BASE_URL}{API_KEY}&q={country_city}&aqi=yes"
response = requests.get(req_url)

my_data = response.json()
print(my_data)
# print(my_data.keys())


def print_data():

    # checking status code and type data of response
    if response.status_code == 200 and response.headers['Content-Type'] == "application/json":
        print("Success!\n")
    else:
        print("An error occurred!\n")

    print(f"\t\t\n........The Weather forecast........")

    print(f"""

        County: {my_data['location']['country']}
        City: {my_data['location']['name']}
        Temperature: {my_data['current']['temp_c']} celsius
        The weather condition: {my_data['current']['condition']['text']}
        Humidity: {my_data['current']['humidity']}
        Cloud: {my_data['current']['cloud']}

    """
          )


print_data()


# Downloading an image of the weather of a particular city
def download_img():
    city = my_data['location']['name']
    img_url = my_data['current']['condition']['icon']

    img = requests.get(f"http:{img_url}")
    # print(img.content)

    with open(f"{city}.png", "wb") as f:
        f.write(img.content)
        print(f"The image of the weather of {city} was downloaded successfully!")


download_img()
