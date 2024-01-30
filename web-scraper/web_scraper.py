import requests

url = 'https://www.cheapshark.com/api/1.0/games?title=Grand%20Theft%20Auto%20V&lowerPrice=0&upperPrice=50&limit=100'

response = requests.get(url)

print(response.text)
