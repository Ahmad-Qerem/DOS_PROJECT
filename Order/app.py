
from flask import Flask
import requests
import json
import os 
app = Flask(__name__)

#query to try and purchase a book by its ID if it is available in stock
@app.route("/purchase/<item_number>", methods=['GET'])
def purchaseCatServer(item_number):
	# check quantity in stock
    
    url = os.environ['CATALOG']+"/info/"+item_number
      
    msg =requests.get(url)

    if msg.content.decode() == "Item not found :(":
        return msg.content
    quantity = int(msg.json()['quantity'])
    if quantity > 0:
		#if available in stock, update the quantity from the catalog server
        url = os.environ['CATALOG']+"/update/"+item_number
        #url2=os.environ['CATALOG2']+"/update/"+item_number
        
        bookName =requests.get(url).content
        
        s = "Purchase complete" + bookName.decode('UTF-8')
        return json.dumps(s), 200, {'ContentType': 'application/json'}
    else:
		#if not in stock, return failure message
        return json.dumps("Purchase failed out of stock"), 400, {'ContentType': 'application/json'}


#if __name__== "__main__":
#    app.run(host="0.0.0.0")        