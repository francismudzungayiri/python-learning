import requests

parameters = {
    'lat': -17.820950,
    'lng': 31.038160,
    'formatted':0 
}

response = requests.get('https://api.sunrise-sunset.org/json', params= parameters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

print(f"SUNRISE: {sunrise}, SUNSET: {sunset}")