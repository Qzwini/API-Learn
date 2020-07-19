from flask import Flask, jsonify, request

app=Flask(__name__)

@app.route('/me')
def index():
    return jsonify({'message':'Hellow API'})




# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         data = request.get_json()
#         name = data.get('name')
#         message = 'Hello {}!'.format(name)
#         return jsonify({'message': message})
#     else:  # GET
#         return jsonify({'message': 'hello from flask API!'})

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST': 
        data = request.get_json()
        name = data.get('name')
        message = 'Hello {}!'.format(name)
        return jsonify({'message': message})
    else:
        return jsonify({'message': 'hello from flask API!'})
    

# {'city': 'temp'}
temperature = {'iq': 23, 'uk': 26, 'us': 24, 'uae': 22}
@app.route('/weather/<city>', methods=['GET', 'POST'])
def get_temp(city):
    temp = temperature.get(city)
    return jsonify({'temp': temp})



    







if __name__ == '__main__':
    app.run(debug=True)