// Function for sending and receiving data trough WebSocket

const log_div = $("#newFrame")

function sendTroughSocket(string_command) {
  var socket = new WebSocket("ws://127.0.0.1:2890/websocket")
  socket.onopen = function () {
    socket.send(string_command)
    socket.onmessage = function (event)
    {
      log_div.append("<p>" + event.data + "</p>")
    }
  }
}




// Shell calls

function installButton() {
  const passwd_input = $("#the_passwd")
  const button = $("#Install").click(function() {
    $("#modal1").modal("show")
    $("#passwd_send").click(function() {
      $("#modal1").modal("hide")
      sendTroughSocket("installNow " + passwd_input.val())
    })
  })
}



// Control center

function controlCenter() {
  const button = $("#Run").click(function ()
  {
    $.get("/Shell/scripts/startSuricata.sh", function ()
    {
      console.log("Starting install")
    })
  })
}

// Div clean button

function cleanButton() {
  const cleanButton = $("#logClean").click(function () {
    log_div.empty()
  })
}

// Test buttons


function testScriptButton() {
  const ls_test = $("#lsTest").click(function () {
    sendTroughSocket("lsTest")
    log_div.scrollTop(log_div[0].scrollHeight)
  })
}

function testErrorButton() {
  const cd_test = $("#cdTest").click(function () {
    sendTroughSocket("cdTest")
    log_div.scrollTop(log_div[0].scrollHeight)
  })
}

function testSudoButton() {
  const passwd_input = $("#the_passwd_test")
  const button = $("#sudoTest").click(function() {
    $("#modal2").modal("show")
    $("#passwd_send_test").click(function() {
      $("#modal2").modal("hide")
      sendTroughSocket("sudoTest " + passwd_input.val())
    })
  })
}



// Calling all functions

installButton()

controlCenter()

cleanButton()

testScriptButton()

testErrorButton()

testSudoButton()
