url = "http://192.168.99.100:9000/orders";

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
    res = $.post(url, _ids);
    reloadModal();
} 

function reloadModal(){
    $("#createOrder").load(location.href + " #createOrder>*");
}

function fetchOrders(){
    orders = $.get(url);
    for(let i in orders){
        putIntoPage(orders[i]);
    }
}

function putIntoPage(order){
    if(order['status'] == 'open'){
        orders = $('#open_orders');
        var div = $('<div>');
        div.text(order['name']);
        orders.append(div);
    }
}