
// Shell calls

function installButton()
{
  const button = $("#Install").click(function ()
  {
    $.get("/Shell/scripts/Start.sh", function ()
    {
      console.log("Starting install")
    })
    $.get("/Shell/scripts/deps_suricata.sh", function ()
    {
      console.log("Installing all dependencies")
    })
    $.get("/Shell/scripts/installSuricata.sh", function ()
    {
      console.log("Runnign install script")
    })
  })
}

function testButton()
{
  const button = $("#Test").click(function ()
  {
    $.get("/Shell/scripts/ls.sh", function ()
    {
      console.log("Testing")
    })
  })
}

// Control center

function controlCenter()
{
  const button = $("#Run").click(function ()
  {
    $.get("/Shell/scripts/startSuricata.sh", function ()
    {
      console.log("Starting install")
    })
  })
}

// Iframe clean button

function cleanButton()
{
  const button = $("#logClean").click(function ()
  {
    $.get("/Shell/clean", function()
    {
      console.log("Cleaning logs")
    })
  })
}

// Test buttons

function testScriptButton()
{
  const button = $("#lsTest").click(function ()
  {
    $.get("/Shell/tests/ls.sh", function ()
    {
      console.log("Starting ls test")
    })
  })
}

function testErrorButton()
{
  const button = $("#cdTest").click(function ()
  {
    $.get("/Shell/tests/cd.sh", function ()
    {
      console.log("Starting cd test")
    })
  })
}



// Calling all functions

installButton()

testButton()

controlCenter()

cleanButton()

testScriptButton()

testErrorButton()
