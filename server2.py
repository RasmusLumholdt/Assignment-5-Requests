from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    pass = request.get_json()