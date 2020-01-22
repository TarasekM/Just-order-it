order_url = "http://192.168.99.100:9000/orders";
menu_url = "http://192.168.99.100:9000/menu"

function closeOrder(id){
    var close_url = "http://192.168.99.100:9000/orders/" + id + '/ready';
    res = createCORSRequest('POST', close_url);
    res.onload = function (){
        timeoutFetch();
    }
    res.send();
} 


function getIDs(){
    var checkboxes = $('input:checked');
    var _ids = []
    for(let i in checkboxes){
        if(checkboxes[i].checked == true){
            var _id = $(checkboxes[i]).siblings("input").val();
            _ids.push(_id);
        }
    }
    return _ids;
}

function sendOrder(){
    var _ids = getIDs();
    var postStr = getPostStr(_ids);
    var post_url = order_url + postStr;
    res = createCORSRequest('POST', post_url);
    res.onload = function (){
        reloadModal();
        timeoutFetch();
    }
    res.send();
}

function getPostStr(_ids){
    var postStr = "?";
    for (let i in _ids){
        postStr = postStr + "items=" + _ids[i] + "&";
    }
    postStr = postStr.substring(0, postStr.length - 1);
    return postStr;
}

function reloadModal(){
    $("#createOrder").load(location.href + " #createOrder>*");
}

function fetchOrders(){
    var xhr = createCORSRequest('GET', order_url);
    xhr.responseType = 'json';
    xhr.onload = function () {
        var json = xhr.response;
        var menu = fetchMenu(json);
    }
    xhr.send();
}


function putIntoPage(order, menu){
    var container = $('<div class = "container">');
    var ul = $('<ul class = "list-group">');
    var li = $('<li class = "list-group-item">');
    var div = $('<div class="d-flex w-100 justify-content-between">');
    var h3 = $('<h3 class = "list-group-item-heading">');
    var h3_id = $('<h3 class = "list-group-item-heading">');
    var button = $('<button type="button" class="btn btn-warning">');
    button.click(function(){
        closeOrder(order["_id"]);
    });

    h3.text('Order:');
    h3_id.text(order["order_id"]);
    button.text('Close Order');

    div.append(h3);
    div.append(h3_id);
    li.append(div);

    var items = order['items'];
    for(let i in items){
        var item = getItem(items[i], menu);
        var child = $('<p class = "list-group-item-text">');
        child.text(item['name']);
        li.append(child);
    }

    var orders;
    if(order['status'] == 'making'){
        orders = $('#open_orders');
        li.append(button);
        ul.append(li);
        container.append(ul);
    }else{
        orders = $('#closed_orders');
        ul.append(li);
        container.append(ul);
    }
    orders.append(container);
}


function getItem(id, menu){
    for(let i in menu){
        if(id == menu[i]['_id']){
            return menu[i];
        }
    }
    return false;
}

function fetchMenu(json){
    var xhr = createCORSRequest('GET', menu_url);
    xhr.responseType = 'json';
    xhr.onload = function () {
        var menu = xhr.response;
        for( let i in json){
            putIntoPage(json[i], menu);
        }
    }
    xhr.send();
}

// Create the XHR object.
function createCORSRequest(method, url) {
    var xhr = new XMLHttpRequest();
    if ("withCredentials" in xhr) {
        // XHR for Chrome/Firefox/Opera/Safari.
        xhr.open(method, url, true);
    } else if (typeof XDomainRequest != "undefined") {
        // XDomainRequest for IE.
        xhr = new XDomainRequest();
        xhr.open(method, url);
    } else {
        // CORS not supported.
        xhr = null;
    }
    return xhr;
}


// Make the actual CORS request.
function makeCorsOrder(url, _ids) {
    // This is a sample server that supports CORS.

    var xhr = createCORSRequest('POST', url);
    xhr.setRequestHeader('Access-Control-Allow-Origin', url);
    if (!xhr) {
        alert('CORS not supported');
        return;
    }


    xhr.onerror = function () {
        alert('Woops, there was an error making the request.');
    };

    xhr.send();
}

// setInterval(() => {
//     fetchOrders();
//   }, 2000);


function timeoutFetch(){
    $("#orders").load(location.href + " #orders>*");
    setTimeout(function(){
        fetchOrders();    
    }, 1000);
}

timeoutFetch();