# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, render_template


from pydantic import BaseModel
from ast import literal_eval
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


import langchain
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings



# creating a Flask app
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/r', methods = ['GET','POST'])
def home():
    if(request.method == 'GET'):
  
        data = "its up <GET>"
        return jsonify({'data': data})
    if(request.method == 'POST'):
        
        data = "its up <>"
        return jsonify({'data': data})