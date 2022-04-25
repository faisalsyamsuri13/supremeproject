//bug: multiple downloads automatically

let btnDownload = document.querySelector('button');
let qr = document.getElementById('qrcode');
let img = qr.querySelector('img');

btnDownload.addEventListener('click', () => {
  let imagePath = img.getAttribute('src');
  saveAs(imagePath, 'QRCode');
});
