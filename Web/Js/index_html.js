

function Testbutton()
{
  const button = $("#Install").click(function ()
  {
    $.get("/Shell/Start.sh", function (data)
    {
      console.log("Starting install")
    })
  })
}

Testbutton()
