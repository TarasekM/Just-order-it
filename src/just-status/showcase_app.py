from random import randint

from flask import Flask, jsonify, make_response, request

app = Flask(__name__)


@app.route('/orders', methods=['GET'])
def get_orders():
    orders = []
    for i in range(1, (randint(7, 15))):
        orders.append(
            {'id': i, 'status': 'making' if randint(0, 1) else 'ready'})
    resp = make_response(jsonify(orders), 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
