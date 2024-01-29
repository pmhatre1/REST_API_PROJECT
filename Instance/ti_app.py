# This main file is used to add the items to the store.

'''
Here's how that's going to work:

  (1)  The client will send us the store name where they want their new item to go.
  (2)  They will also send us the name and price of the new item.
  (3)  We'll go through the stores one at a time, until we find the correct one (whose name matches what the user gave us).
  (4)  We'll append a new item dictionary to that store's items.

'''
from flask import Flask, request

ti_app = Flask(__name__)

stores = [{
            "name":"My Store",
            "items":[{
                "name":"my item",
                "price": 15.99
            }]
           }]

@ti_app.route('/store', methods=['GET'])
def get_stores():
    return {"stores":stores}

@ti_app.route('/store', methods=['POST'])
def create_store():
    request_data =  request.get_json()
    new_store =  {"name":request_data["name"],
                  "items": []
                 }
    stores.append(new_store)
    return new_store, 201
# Reques data is request the json file and then adding that to the new_store dictionary with the items.

@ti_app.route('/store/<string:name>/item',methods = ['POST'])
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name":request_data["name"],
                        "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item
    
    return {"message":"Store not found"},404

@ti_app.route('/store/<string:name>',methods = ['GET'])
def get_store(name):
    for store in stores:
        if store["name"]==name:
            return store
    return {"message":"Store not found"},404


# If Docker is having difficulty starting the image, Make sure that your Flask application file is 
# named either wsgi.py or app.py, as Flask looks for these filenames by default. If your file has a different name, 
# you may need to specify it using the --app option or set the FLASK_APP environment variable

# docker run -p 5005:5000 -e FLASK_APP=your_app_name.py rest-apis-flask-python   Use this command instead of the one mentioned in the tutorial.
