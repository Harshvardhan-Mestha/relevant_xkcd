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


# @app.route('/')
# def home():
#     return render_template('index.html', query="",img1="",img2="",img3="",img4="")


@app.route('/', methods = ['GET','POST'])
def prompt():
    if(request.method == 'GET'):
  
        data = "its up <GET>"
        
        return render_template('index.html', query="",img1="",img2="",img3="",img4="")
    
    if(request.method == 'POST'):
        
        data = "its up <POST>"
      
        query = request.form["prompt"]
        docs = main.similarity_search_with_score(query)
        comics = list()
        imgs = list()



        for doc in docs:
            comic_name = str(doc[0].metadata['source'])
            if (comic_name == '/Users/harshvardhanmestha/repos/relevant_xkcd/xkcd_comic_data/comic_raw/blank.txt'):
                return render_template('index.html',query="No relevant comics were found, Please try a different prompt.",img1="",img2="",img3="",img4="")
            if (comic_name == '/Users/harshvardhanmestha/repos/relevant_xkcd/xkcd_comic_data/comic_raw/comic_404_raw.txt'):
                return render_template('index.html',query="The 404 comic leads to a 404 webpage instead of an image comic :)",img1="",img2="",img3="",img4="")
            comic_name = str(re.search('comic_\d{1,4}_raw.txt', comic_name).group())
            comic_no = int(re.search('\d{1,4}',comic_name).group())
            comics.append(comic_no)
            url = "https://xkcd.com/"+str(comic_no)+"/info.0.json"
            response = urlopen(url)
            data_json = json.loads(response.read())
            imgs.append(data_json['img'])
        print(imgs)
        if(len(imgs)==4):
            return render_template('index.html',query=request.form["prompt"],img1=imgs[0],img2=imgs[1],img3=imgs[2],img4=imgs[3])
        else:
            return render_template('index.html',query="No relevant comics were found, Please try a different prompt.",img1="",img2="",img3="",img4="")

# driver function
if __name__ == '__main__':
    app.run(debug = False)
