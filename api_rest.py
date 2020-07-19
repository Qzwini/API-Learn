from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api=Api(app)

weather_data = {
    'UK': {'temp': 19, 'wind': 16, 'humidity': 80},
    'IQ': {'temp': 30, 'wind': 10, 'humidity': 20},
    'US': {'temp': 23, 'wind': 10, 'humidity': 80}
}

class weather (Resource):
    def get(self, city):
        weather_city = weather_data.get(city)
        return ({city:weather_city})

api.add_resource(weather, '/weather/<city>')

if __name__ == '__main__':
    app.run(debug=True)