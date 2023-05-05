# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, render_template


# creating a Flask app
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.

from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings 

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")



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
      
        db = FAISS.load_local("world_facts", embeddings)
        query = request.form["prompt"]
        docs = db.similarity_search_with_score(query)

        #return jsonify({'data': data})
        return render_template('index.html',prompt=docs)
    
