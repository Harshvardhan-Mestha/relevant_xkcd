# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, render_template


# creating a Flask app
app = Flask(__name__,static_folder='stylesheets')

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
import langchain
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings 
import re
import json
from urllib.request import urlopen


embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
main = FAISS.load_local("xkcd_comic_data/comic_faiss/faiss_main", embeddings)


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
      
        query = request.form["prompt"]
        docs = main.similarity_search_with_score(query)
        comics = list()
        imgs = list()



        for doc in docs:
            comic_name = str(doc[0].metadata['source'])
            comic_name = str(re.search('comic_\d{1,4}_raw.txt', comic_name).group())
            comic_no = int(re.search('\d{1,4}',comic_name).group())
            comics.append(comic_no)
            url = "https://xkcd.com/"+str(comic_no)+"/info.0.json"
            response = urlopen(url)
            data_json = json.loads(response.read())
            imgs.append(data_json['img'])
            
        return render_template('index.html',query=request.form["prompt"],img1=imgs[0],img2=imgs[1],img3=imgs[2],img4=imgs[3])
    

