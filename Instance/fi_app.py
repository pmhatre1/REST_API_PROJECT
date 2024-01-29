from flask import Flask


'''
Created a first file in the Flask app
First create a virtual environment
python3.10 -m venv .venv
source .venv/bin/activate
'''
fi_app = Flask(__name__)

# Creating the stores

stores =[{ "name":"My Store", "items": 
           [
                {
                "name":"my item",
                "price": 15.99
                }
            ]
        }]

''''
Now that we've got the data stored, we can go ahead and make a Flask route that, 
when accessed, will return all our data.'''

@fi_app.get("/store")
def get_stores():
    return {"stores":stores}

# Also update and paste the .flaskenv file in the folder where you want to run the flask app.