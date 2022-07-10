from distutils.command.config import config
import json
from urllib import response
from flask import Flask, Request,redirect,request,render_template, url_for
import requests
myLibrary = Flask(__name__)




@myLibrary.route("/")
@myLibrary.route("/home")
def home():
    
    dictToSend = {'name':'ahmad'}
    response = requests.post('http://localhost:4040/', json=dictToSend)
    #data = response.text
    name = response.__getattribute__()
    return render_template('index.html',name=name)





#@myLibrary.route("/search")
#def search():
#    return redirect("http://localhost:4040/",code=302)
    


""" @myLibrary.route("/info")
def info():
   return render_template('index.html')
    
@myLibrary.route("/purchase")
def purchase():
    return render_template('index.html') 
 """




if __name__== "__main__":
    myLibrary.run(debug=True)

