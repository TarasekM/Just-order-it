import requests
import json
url = "http://192.168.99.100:9000/menu"

pizza = {
    "name" : "pepperoni",
    "price" : 21.99,
    "tags" : ["food"],
    "ingredients" : ["salami", "cheese", "tomato souce"]
}

response = requests.post(url, pizza, verify=False)