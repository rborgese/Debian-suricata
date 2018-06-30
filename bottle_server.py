from bottle import route, run, static_file, request, Bottle, abort
from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler
from Shell import shell_calls
import json

app = Bottle()


# Reading html files
def read_file(theFile):
    file = open(theFile, "r")
    html = file.read()
    file.close()
    return html


# The websocket
@app.route("/websocket")
def handle_websocket():
    if request.environ.get("wsgi.websocket"):
        wsock = request.environ["wsgi.websocket"]
        if not wsock:
            abort(400, "Expected a websocket request")

        if wsock:
            try:
                message = wsock.receive()
                print(message)
                if message == "lsTest":
                    response = shell_calls.call_ls()
                    wsock.send(response)
                elif message == "cdTest":
                    wsock.send(message)
                else:
                    wsock.send("Unrecognized message")
            except WebSocketError as e:
                print(e)




# Serve static Js and Css files
@app.route("/Web/CSS/Bootstrap/<filename>")
def serve_bootstrap(filename):
    return static_file(filename, root="Web/CSS/Bootstrap/")

@app.route("/Web/Jquery/<filename>")
def serve_jquery(filename):
    return static_file(filename, root="Web/Jquery/")

@app.route("/Web/Js/<filename>")
def serve_js(filename):
    return static_file(filename, root="Web/Js/")

# Iframe for logs
@app.route("/Web/html/outputs/<filename>")
def serve_iframe(filename):
    shell_out = read_file("Web/html/outputs/{}".format(filename))
    return shell_out

# Shell calls
@app.route("/Shell/clean")
def clean_iframe():
    shell_calls.reset_soup()

@app.route("/Shell/scripts/Start.sh")
def start_install():
    shell_calls.call_start()
    #shell_calls.call_deps()
    #shell_calls.call_install()

# Shell Tests
@app.route("/Shell/tests/ls.sh")
def test_ls():
    shell_calls.call_ls()

@app.route("/Shell/tests/cd.sh")
def test_cd():
    shell_calls.call_cd()
    shell_calls.call_bad_cd()


# User Interface
@app.route('/')
@app.route('/home')
def hello():
    index = read_file("Web/index.html")
    return index


server = WSGIServer(("127.0.0.1", 2890), app, handler_class=WebSocketHandler)

try:
    server.serve_forever()
except KeyboardInterrupt:
    server.close()



#run(host='localhost', port=8080, debug=True)
