import requests
print("\n ")

r= requests.get(url='http://127.0.0.1:5000/')
# r= requests.get(url='http://samples.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=439d4b804bc8187953eb36d2a8c26a02')
print("--- status_code --- ")
print(r)
print(r.status_code)

print("\n ")

print("--- json() --- ")
print(r.json())
result = r.json()
print(result)
print(result['message'])

print("\n ")



