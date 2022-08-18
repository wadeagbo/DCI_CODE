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
	Your Operator just activated the Alpha Command. Looks like he's in trouble.
	Be ready to escalate and wait for further commands. Remember: if you receive a
	simple check in now: That means all is good. But if it's the Hotel command:
	Not so good. Don't let him down. Sir.
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
