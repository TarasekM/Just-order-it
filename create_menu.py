import requests
import json
url = "http://localhost:9000/menu"

# Main Meals
pizza1 = {
    "name" : "Pizza Prosciutto",
    "price" : 22.00,
    "tags" : ["Main Meal"],
    "ingredients" : ["prosciutto", "cheese", "tomato souce"]
}
response = requests.post(url, pizza1, verify=False)

pizza2 = {
    "name" : "Pizza Funghi",
    "price" : 20.00,
    "tags" : ["Main Meal"],
    "ingredients" : ["mashrooms", "cheese", "tomato souce"]
}
response = requests.post(url, pizza2, verify=False)

pizza3 = {
    "name" : "Pizza Pepperoni",
    "price" : 22.00,
    "tags" : ["Main Meal"],
    "ingredients" : ["spicy salami", "cheese", "tomato souce"]
}
response = requests.post(url, pizza3, verify=False)

meal1 = {
    "name" : "Devolay",
    "price" : 25.00,
    "tags" : ["Main Meal"],
    "ingredients" : ["pork", "butter", "potatos", "salad"]
}
response = requests.post(url, meal1, verify=False)

meal2 = {
    "name" : "Chicken Risotto",
    "price" : 18.00,
    "tags" : ["Main Meal"],
    "ingredients" : ["chicken", "rise", "olive", "vegetables"]
}
response = requests.post(url, meal1, verify=False)

# Soups
soup1 = {
    "name" : "Tomato Soup",
    "price" : 10.00,
    "tags" : ["Soup"],
    "ingredients" : ["tomatos", "onion", "spices", "rice"]
}
response = requests.post(url, soup1, verify=False)

soup2 = {
    "name" : "Broth Soup",
    "price" : 10.00,
    "tags" : ["Soup"],
    "ingredients" : ["chicken broth", "noodles", "carrot"]
}
response = requests.post(url, soup2, verify=False)

#Appetizers
appetizer1 = {
    "name" : "Bread with lard",
    "price" : 15.00,
    "tags" : ["Appetizer"],
    "ingredients" : ["bread", "lard", "salt", "pickle"]
}
response = requests.post(url, appetizer1, verify=False)

appetizer2 = {
    "name" : "Stuffed Cucumber",
    "price" : 13.00,
    "tags" : ["Appetizer"],
    "ingredients" : ["cucumber", "vegetables", "spices"]
}
response = requests.post(url, appetizer2, verify=False)