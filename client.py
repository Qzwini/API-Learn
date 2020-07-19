import requests
print("\n ")

r= requests.get(url='http://127.0.0.1:5000/me')
# r= requests.get(url='http://samples.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=439d4b804bc8187953eb36d2a8c26a02')
print("--- status_code --- ")
print(r)
print(r.status_code)

print("\n ")

print("--- json(1) --- ")
print(r.json())
result = r.json()
print(result)
print(result['message'])
print(result.get('message'))

print("\n ")

print("--- json(2) --- ")
q= requests.post(url='http://127.0.0.1:5000/', json={'name': "Ali"})
print(q.status_code)
print (q.json().get('message'))
print("\n ")

print("--- json(3) --- ")
coun = 'iq'
country =  requests.post(url='http://127.0.0.1:5000/weather/{}'.format(coun))
print(country.status_code)
print('the temp in {}  - is {}'.format(coun, country.json().get('temp')))