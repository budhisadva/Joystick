const url = `ws://${window.location.host}/ws/socket-server/`;

window.onload = () => {
  const picoSocket = new WebSocket(url);

  picoSocket.onmessage = (e) => {
    let data = JSON.parse(e.data);
    let ejes = data.message.split(",");
    let cuadro = document.getElementById('cuadro');
    let btn = parseInt(ejes[2].substr(1,1));
    let x = parseInt(ejes[0].substr(1,3));
    let y = parseInt(ejes[1].substr(1,3));
    document.getElementById('ejes').innerHTML = `X: ${122-y},Y: ${122-x}, B: ${btn}`;
    if (btn == 1) {
      cuadro.style.backgroundColor = 'violet';
    } else {
      cuadro.style.backgroundColor = 'cyan';
    }
    cuadro.style.left = `${112-y}`+'px';
    cuadro.style.bottom = `${112-x}`+'px';
  }

  picoSocket.onopen = function() {
    console.log('ws conectado');
  };

  picoSocket.onclose = function() {
    console.log('ws desconectado');
  };

  document.getElementById('desconectar').onclick = function() {
    picoSocket.close();
  }
}
