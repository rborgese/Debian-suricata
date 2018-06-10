

function installButton()
{
  const button = $("#Install").click(function ()
  {
    $.get("/Shell/scripts/Start.sh", function (data)
    {
      console.log("Starting install")
    })
    $.get("/Shell/scripts/deps_suricata.sh", function (data)
    {
      console.log("Installing all dependencies")
    })
    $.get("/Shell/scripts/installSuricata.sh", function (data)
    {
      console.log("Runnign install script")
    })
  })
}

function testButton()
{
  const button = $("#Test").click(function ()
  {
    $.get("/Shell/scripts/ls.sh", function (data)
    {
      console.log("Testing")
    })
  })
}

function controlCenter()
{
  const button = $("#Run").click(function ()
  {
    $.get("/Shell/scripts/startSuricata.sh", function (data)
    {
      console.log("Starting install")
    })
  })
}





installButton()

testButton()

controlCenter()
