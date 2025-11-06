import requests
answer= input(f"what is the city whose information you want to find out: ")

request = f"http://api.openweathermap.org/geo/1.0/direct?q={answer}&appid=5aa5a783ad09e19191f0cc616702785a"
response = requests.get(request).json()
x = response[0]['lat']
y= response[0]['lon']

request2 = f"https://api.openweathermap.org/data/3.0/onecall?lat={x}&lon={y}.04&appid=5aa5a783ad09e19191f0cc616702785a"
response2 = requests.get(request).json()

z = response2
print(z)