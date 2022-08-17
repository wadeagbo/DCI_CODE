from flask import Flask
from flask import request

app = Flask(__name__)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

@app.route('/', methods=['GET'])
def home():
    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
	<Response>
	<Say voice="man">Overwatch.
	Be advised that the Operator just activated the Hotel command. He needs your help.
	Now it is for you to decide wether it's a false alarm, or if it's not:
	Which steps to take. You got full authority to initialize the F Protocol.
	It's up to you how to proceed. Sir
	</Say>
</Response>'''
    return xml_content

@app.route('/end', methods=['GET'])
def end():
    return request.environ.get('werkzeug.server.shutdown')

if __name__ == "__main__":
    app.run(debug = True, port = 8000)


#  FOR SERVER SHUTDOWN
#import requests
#requests.get("http://127.0.0.1:8000/shutdown")
