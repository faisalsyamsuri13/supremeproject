var qrcode = new QRCode(document.getElementById("qrcode"), {
  width: 150,
  height: 150
});
function makeCode() {
  var elText = document.getElementById("url");
  elText.value = window.location.href;

  if (!elText.value) {
    alert("Input a text:");
    elText.focus();
    return;
  }
  qrcode.makeCode(elText.value);
}
