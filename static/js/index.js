var Socket = io()

Socket.on("connect", () => {
  console.log("connected!")
  
  $("#send").on("click", () => {
    let value = $("#data").val()
    Socket.emit("message", {value})
    $("#data").val("")
  })
  
  Socket.on("res", (data) => {
    $(".message").html(`<span><b>Chatbot responde:</b></span> ${data}`)
  })
})