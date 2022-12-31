import requests


def print_data(country):

    API_KEY = "dd50f5b11643407190761005222412"
    BASE_URL = "http://api.weatherapi.com/v1/current.json?key="

    req_url = f"{BASE_URL}{API_KEY}&q={country}&aqi=yes"
    response = requests.get(req_url)

    my_data = response.json()

    # checking status code and type data of response
    if response.status_code == 200 and response.headers['Content-Type'] == "application/json":
        country_name = my_data['location']['country']
        city_name = my_data['location']['name']
        info = f"""
            County: {my_data['location']['country']}
            City: {my_data['location']['name']}
            Temperature: {my_data['current']['temp_c']} celsius
            Temperature: {my_data['current']['temp_f']} fahrenheit
            The weather condition: {my_data['current']['condition']['text']}
            Humidity: {my_data['current']['humidity']}
            Cloud: {my_data['current']['cloud']}
            """
        return [info, country_name, city_name]

    else:
        print("An error occurred!\n")


