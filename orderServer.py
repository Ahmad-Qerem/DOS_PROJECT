from distutils.command.config import config
from flask import Flask,redirect,request,render_template
myLibrary = Flask(__name__)

@myLibrary.route("/")
@myLibrary.route("/home")
def home():
    return render_template('index.html')


    




if __name__== "__main__":
    myLibrary.run(debug=True)

