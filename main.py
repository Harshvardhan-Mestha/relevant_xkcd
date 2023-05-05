# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, render_template


# creating a Flask app
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/prompt', methods = ['GET','POST'])
def prompt():
    if(request.method == 'GET'):
  
        data = "its up <GET>"
        
        return jsonify({'data': data})
    if(request.method == 'POST'):
        
        data = "its up <POST>"
        data = request.form["prompt"]

        #return jsonify({'data': data})
        return render_template('index.html',prompt=request.form["prompt"])
    
