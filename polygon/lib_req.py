import requests

# res = requests.post('https://goggle.com')
# print(res)

URL = 'https://itunes.apple.com/search?term=Шнуров'

res = requests.get(URL)
# print(type(res.text))

print(res.json())
print(type(res.json()))