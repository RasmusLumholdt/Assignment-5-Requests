from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    
    
    if(request.get_json()['password'] == 'ab'):
        return Response('{"Message": "Logged in"}', status=200, mimetype='application/json')
    else:
        return Response('{"Message": "Failed"}', status=403, mimetype='application/json')
