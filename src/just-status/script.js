const Http = new XMLHttpRequest();
const url = 'http://localhost:9000/orders';

function update_orders(orders) {
  let not_ready_orders = document.getElementById('not-ready-orders');
  while (not_ready_orders.firstChild) {
    not_ready_orders.removeChild(not_ready_orders.firstChild);
  }
  let ready_orders = document.getElementById('ready-orders');
  while (ready_orders.firstChild) {
    ready_orders.removeChild(ready_orders.firstChild);
  }
  for (let order of JSON.parse(orders)) {
    if (order['status'] == 'making') {
      let new_order = document.createElement('div');
      new_order.classList.add('order-card');
      new_order.classList.add('not-ready-order-card');
      new_order.innerText = order['order_id'];
      not_ready_orders.appendChild(new_order);
    }
    else if (order['status'] == 'ready') {
      let new_order = document.createElement('div');
      new_order.classList.add('order-card');
      new_order.classList.add('ready-order-card');
      new_order.innerText = order['order_id'];
      ready_orders.appendChild(new_order);
    }
  }
}

Http.onreadystatechange = () => {
  if (Http.readyState == 4 && Http.status == 200) {
    update_orders(Http.responseText);
  }
}


Http.open('GET', url);
Http.send();

setInterval(() => {
  Http.open('GET', url);
  Http.send();
}, 5000);
