import requests
import json
url = "http://localhost:9000/menu"


pizza1 = {
    "name" : "Pizza Prosciutto",
    "price" : 22.00,
    "tags" : ["Main Meals"],
    "ingredients" : ["prosciutto", "cheese", "tomato souce"]
}
response = requests.post(url, pizza1, verify=False)

pizza2 = {
    "name" : "Pizza Funghi",
    "price" : 20.00,
    "tags" : ["Main Meals"],
    "ingredients" : ["mashrooms", "cheese", "tomato souce"]
}
response = requests.post(url, pizza2, verify=False)

pizza3 = {
    "name" : "Pizza Pepperoni",
    "price" : 22.00,
    "tags" : ["Main Meals"],
    "ingredients" : ["spicy salami", "cheese", "tomato souce"]
}
response = requests.post(url, pizza3, verify=False)

meal1 = {
    "name" : "Devolay",
    "price" : 25.00,
    "tags" : ["Main Meals"],
    "ingredients" : ["pork", "butter", "potatos", "salad"]
}
response = requests.post(url, meal1, verify=False)

meal2 = {
    "name" : "Chicken Risotto",
    "price" : 18.00,
    "tags" : ["Main Meals"],
    "ingredients" : ["chicken", "rise", "olive", "vegetables"]
}
response = requests.post(url, meal1, verify=False)
