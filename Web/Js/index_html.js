

function Testbutton()
{
  const button = $("#Test").click(function ()
  {
    $.get("Shell/Start.sh", function (data)
    {
      alert("Data: " + data)
    })
  })
}

Testbutton()
