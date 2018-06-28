

// Shell calls

function installButton() {
  const button = $("#Install").click(function ()
  {
    $.get("/Shell/scripts/Start.sh", function ()
    {
      console.log("Starting install")
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
  const the_div = $("#newFrame")
  const cleanButton = $("#logClean").click(function () {
    the_div.empty()
  })
}

// Test buttons


function testScriptButton() {
  const the_div = $("#newFrame")
  const ls_test = $("#lsTest").click(function() {
    var socket = new WebSocket("ws://127.0.0.1:2890/websocket")
    console.log("lstest")
    socket.onopen = function () {
      socket.send("lsTest")
      socket.onmessage =  function (event)
      {
        console.log(event.data)
        the_div.append("<p>" + event.data + "</p>")
      }
    }
  })
}

function testErrorButton() {
  const the_div = $("#newFrame")
  const cd_test = $("#cdTest").click(function() {
    var socket = new WebSocket("ws://127.0.0.1:2890/websocket")
    console.log("lel test")
    socket.onopen = function () {
      socket.send("cdTest")
      socket.onmessage =  function (event)
      {
        console.log(event.data)
        the_div.append("<p>" + event.data + "</p>")
      }
    }
  })
}



// Calling all functions

installButton()

controlCenter()

cleanButton()

testScriptButton()

testErrorButton()
