from distutils.command.config import config
import json
from urllib import response
from flask import Flask, Request,redirect,request,render_template, url_for
import requests
app = Flask(__name__)




@app.route("/")
@app.route("/home")
def home():
    return "BAZAR.COM ---- please write on URL what you need"

@app.route("/search", methods=['GET'])
def allBooks():
    return requests.get("http://127.0.0.1:5000/search").content

@app.route("/search/<category>", methods=['GET'])
def searchCatagory(category):
    url = "http://127.0.0.1:5000/search/"+category
    return requests.get(url).content

@app.route("/info/<item_number>", methods=['GET'])
def bookInfo(item_number):
    url = "http://127.0.0.1:5000/info/"+item_number
    return requests.get(url).content  

if __name__== "__main__":
    app.run(debug=True , port = 3000)