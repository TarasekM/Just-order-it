import requests
import json
from flask import Flask, render_template
just_order = Flask(__name__, template_folder='templates')
url = 'http://192.168.99.100:9000/menu'

@just_order.route('/')
def index():
    res = requests.get(url)
    menu = res.json()
    return render_template("index.html", menu=menu)


if __name__ == '__main__':
      just_order.run(host='0.0.0.0', port=5000)