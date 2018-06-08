

function Testbutton()
{
  const button = $("#Install").click(function ()
  {
    $.get("/Shell/ls.sh", function (data)
    {
      console.log("Starting install")
    })
  })
}

Testbutton()
