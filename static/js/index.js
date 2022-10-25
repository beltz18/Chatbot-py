function send_data() {
  const data  = document.getElementById("data").value
  const xhr = new XMLHttpRequest()
  xhr.open('POST', "/get-data/"+JSON.stringify(data))
  xhr.send()
  console.log(xhr.responseText)
}