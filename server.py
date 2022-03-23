from math import prod
from flask import Flask, abort
import json
from mock_data import catalog

app = Flask("Server")

@app.route("/")
def home():
    return "Hello from flask"

@app.route("/me")
def about_me():
    return "Guillermo Jimenez"


#######################################################
###############     API ENDPOINTS     #################
###############      RETURN JSONS     #################
#######################################################

@app.route("/api/catalog", methods=["get"])
def get_catalog():
    return json.dumps(catalog)

@app.route("/api/catalog", methods=["post"])
def save_product():
    pass

# GET /api/catalog/count -> how many products exist in the catalog
@app.route("/api/catalog/count")
def product_count():
    count = len(catalog)
    return json.dumps(count)

#get /api/catalog/total -> the sum o all the product's prices
@app.route("/api/catalog/total")
def total_of_catalog():
    total = 0
    for prod in catalog:
        total += prod["price"]

    return json.dumps(total)

@app.route("/api/product/<id>")
def get_by_id(id):
    #find the product with _id is equal to id
    for prod in catalog:
        if prod["_id"] == id:
            return json.dumps(prod)
    
    #not found, return an error 404
    return abort(404, "No product with such id")

#GET /api/product/cheapest
#should return the product with the lowest price
@app.route("/api/product/cheapest")
def cheapest_product():
    #create a variable with one of the elements from the list
    #create a for loop to travel catalog
    #if the price of your prod is lower than the price of your solutions
    solution = catalog[0]
    for prod in catalog:
        if prod["price"] < solution["price"]:
            solution = prod

    return json.dumps(solution)

#GET /api/categories
#should return a list of strings representing the unique categories

@app.get("/api/categories")
def unique_categories():
    categories = []
    for prod in catalog:
        category = prod["category"]
        if not category in categories:
            categories.append(category)
    
    return json.dumps(categories)



#ticket 2345
#create an endpoint that allows the client to get all the products
#form an unspecified category
#/api/catalog/fruit where fruit is the category in question
@app.get("/api/catalog/<category>")
def prods_by_pcategory(category):
    result = []
    for prod in catalog:
        if prod["category"] == category:
            result.append(prod)

    return json.dumps(result)



app.run(debug=True)