from distutils.command.config import config
from functools import cache
import json
from urllib import response
from flask import Flask, Request,redirect,request,render_template, url_for
import requests
app = Flask(__name__)

cache = {}
robin = False 
catalog1 ="http://catalog:5000" 
catalog2 ="http://catalog2:5000"
order1 = "http://order:5000"
order2 = "http://order2:5000"

@app.route("/")
@app.route("/home")
def home():
    return "BAZAR.COM ---- please write on URL what you need"

@app.route("/search", methods=['GET'])
def allBooks():
    global robin
    robin = not robin
    return requests.get((catalog1 if robin else catalog2)+"/search").content
    
@app.route("/search/<category>", methods=['GET'])
def searchCatagory(category):
    global robin
    robin = not robin
    url = catalog1 if robin else catalog2 +"/search/"+category
    if (category not in cache):
        cache[category] = requests.get(url).content
    return cache[category]


@app.route("/info/<item_number>", methods=['GET'])
def bookInfo(item_number):

    global robin
    robin = not robin
    url = catalog1 if robin else catalog2 +"/info/"+item_number
    if(item_number not in cache):
        cache[item_number] = requests.get(url).content
    return cache[item_number] 

@app.route("/purchase/<item_number>", methods=['GET'])
def purchase(item_number):
    if (item_number in cache):
        cache.pop(item_number)
    global robin
    robin = not robin

    url = order1+"/purchase/"+item_number
    url2 = order2+"/purchase/"+item_number
    requests.get(url).content 
    return requests.get(url2).content  

#if __name__== "__main__":
#    app.run(debug=True , port = 5000)

    """
    global robin
    robin = not robin
    url = catalog1 if robin else catalog2 +"/info/"+item_number
    
    if (item_number not in Cache):
        req=requests.get(url)
        if req.status_code == 200 :
            Cache[item_number]= req.content
            return req.content  
        else :
            return req.content 

    return  Cache[item_number]
"""