
function listen_websocket()
{
  var socket = new WebSocket("ws://127.0.0.1:8080/websocket")
  const the_div = $("#shellout")
  socket.onmessage =  function (event)
  {
    the_div.append("<p>" + event.data + "</p>")
  }
}


listen_websocket()
