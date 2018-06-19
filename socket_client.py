from websocket import create_connection


def send_to(data):
    ws = create_connection("ws://localhost:8080/websocket")
    ws.send(data)
    result =  ws.recv()
    print ("Result '%s'" % result)
    ws.close()