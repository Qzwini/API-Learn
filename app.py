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
    
    





if __name__ == '__main__':
    app.run(debug=True)