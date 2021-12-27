from flask import Flask

app = Flask(__name__)

@app.route('/test_the_rest')
def test_the_rest():
    response = {    'str': 'x',
                    'int': 7,
                }
    return response #, 201, {'content-type': 'application/json'}

x = app.run(host='0.0.0.0', port=5080)

print(x)
    
