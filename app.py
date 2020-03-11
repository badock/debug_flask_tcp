from flask import Flask
from werkzeug.serving import WSGIRequestHandler, BaseWSGIServer

app = Flask(__name__)

# BaseWSGIServer.protocol_version = "HTTP/1.1"
WSGIRequestHandler.protocol_version = "HTTP/1.1"


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
