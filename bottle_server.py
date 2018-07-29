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


# The websocket route handler
@app.route("/websocket")
def handle_websocket():
    if request.environ.get("wsgi.websocket"):
        wsock = request.environ["wsgi.websocket"]
        if not wsock:
            abort(400, "Expected a websocket request")

        elif wsock:
            try:
                message = wsock.receive()
                print(message)
                # String_commands for installing testing and control center
                if message.startswith("installNow"):
                    passwd_rcv = message.replace("installNow ", "")
                    response1 = shell_calls.call_start()
                    for line in response1:
                        wsock.send(line)
                    response2 = shell_calls.call_deps(passwd_rcv)
                    for line in response2:
                        wsock.send(line)
                    response3 = shell_calls.call_install(passwd_rcv)
                    for line in response3:
                        wsock.send(line)
                elif message == "testNow":
                    response = ["lel", "wayne"]
                    for line in response:
                        wsock.send(line)

                # String_commands for testing websocket and shell output
                elif message == "lsTest":
                    response = shell_calls.call_ls()
                    for line in response:
                        wsock.send(line)
                elif message == "cdTest":
                    response1 = shell_calls.call_cd()
                    response2 = shell_calls.call_bad_cd()
                    for line in response1:
                        wsock.send(line)
                    for line in response2:
                        wsock.send(line)
                elif message.startswith("sudoTest"):
                    passwd_rcv = message.replace("sudoTest ", "")
                    print(passwd_rcv)
                    response = shell_calls.call_sudo_try(passwd_rcv)
                    for line in response:
                        wsock.send(line)
                # Refuse non implemented String_commands
                else:
                    abort(400, "Unrecognized command")
            except WebSocketError as e:
                print(e)
        else:
            print("Something bad probably happened")




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
