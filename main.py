import requests

def findCountry(ip_address):
    API = 'https://api.ip2country.info/ip?{}'
    getResult = requests.get(API.format(ip_address))
    result = getResult.json()
    country = "IP {} from {}".format(ip_address, result['countryName'])
    return country

print(findCountry('212.45.128.255'))