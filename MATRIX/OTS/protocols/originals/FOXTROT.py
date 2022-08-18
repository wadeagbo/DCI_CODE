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
	<Say voice="man" language="de">Guten Tag, es gibt einen Notfall. Ich wiederhole, es gibt einen Notfall.
	Ein deutscher Staatsbürger ist im Ausland und wurde höchstwahrscheinlich von Terroristen gefangen genommen. Dies ist kein Scherz. Sein Name ist
	Markus Bayer. Er programmierte mich um im Notfall die Behörden zu benachrichtigen, da er ein spezielles Verfahren für diesen Fall erstellt hat. Holen Sie sich etwas zum schreiben. Ich warte
	10 Sekunden. Eins. Zwei. Drei. Vier. Fünf. Sechs. Sieben. Acht. Neun. Zehn. Fahre fort.
	Ich wiederhole: Sein Name ist Markus. Bayer. M . a . r . k . u . s . Und: B . e . y . e . r . Er wohnt in der Frauenlobstrasse 41 . Frauen. Lob. Strasse. 41 .

	Sein Notfallkontakt hat alle für Sie wichtigen Informationen. Er heißt Jonathan Stratmann. Jonathan. Stratmann. Seine Telefonnummer ist die 0 1 7 6 . 4 3 3 . 9 0 3 . 6 4 . Ich wiederhole. 0 1 7 6 . 4 3 3 . 9 0 3 . 6 4 .
	
	Sagen Sie dass ich sie angerufen habe. Mein Name ist 41 . Wie die Zahl. Vielen Dank für Ihre Kooperation.
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
