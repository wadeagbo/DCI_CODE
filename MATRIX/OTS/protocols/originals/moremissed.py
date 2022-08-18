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
	<Say voice="man">Good day sir, this is 41.
	The Operator missed more than three Checkpoints. Check in with him immediately.
	If he does not respond to any contact attempts, he is most likely in trouble. You are cleared to initiate Protocols.  Sir
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
