import sqlite3


from distutils.command.config import config
from xml.etree.ElementTree import tostring

from flask import Flask, jsonify, redirect, render_template, request, url_for
from importlib_metadata import NullFinder

catalogServer = Flask(__name__)

DATABASE = '/path/to/database.db'
AllBooks=[
    "This is A","This is B","This is C","This is D"
]
data = {'name': 'nabin khadka'}



@catalogServer.route("/", methods=['POST'])
@catalogServer.route("/home")
def home():
    data = request.get_json() 
    name = data['name']
    name+=" this is my name"
    return jsonify({'name':name})
    




if __name__== "__main__":
    catalogServer.run(debug=True,port=4040)

