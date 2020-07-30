from flask import *

app = Flask(__name__)

 
@app.route('/')  
def message():
	return "<html><body><h1>Hi, welcome to the website</h1></body></html>"

@app.route('/contacts')  
def mes():
	return '{ "name":"hello"}'

app.run(debug = True,port = 80,host = "0.0.0.0")  