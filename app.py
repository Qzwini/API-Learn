from flask import Flask, jsonify

app=Flask(__name__)

@app.route('/me')
def index():
    return jsonify({'message':'Hellow API'})


if __name__ == '__main__':
    app.run(debug=True)