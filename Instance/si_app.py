'''
How to create stores in our REST API

To create a store, we'll receive JSON from our client (in our case, Insomnia, but it could be another Python app, JavaScript, or any other language or tool).

Our client will send us the name of the store they want to create, and we will add it to the database!

For this, we will use a POST method. POST is usually used to receive data from clients and either use it, or create resources with it.

In order to access the JSON body of a request, we will need to import request from flask. Your import list should now look like this:
'''
from flask import Flask, request

si_app = Flask(__name__)

stores = [{
            "name":"My Store",
            "items":[{
                "name":"my item",
                "price": 15.99
            }]
           }]

@si_app.route('/store', methods=['GET'])
def get_stores():
    return {"stores":stores}

@si_app.route('/store', methods=['POST'])
def create_store():
    request_data =  request.get_json()
    new_store =  {"name":request_data["name"],
                  "items": []
                 }
    stores.append(new_store)
    return new_store, 201
# Reques data is request the json file and then adding that to the new_store dictionary with the items.