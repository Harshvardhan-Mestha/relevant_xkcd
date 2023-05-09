import langchain
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import time
import re
import json
from urllib.request import urlopen
import json



embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
main = FAISS.load_local("xkcd_comic_data/comic_faiss/faiss_main", embeddings)

query = "Jokes about binary"
docs = main.similarity_search_with_score(query)
comic_list = list()
for doc in docs:
    comic_name = str(doc[0].metadata['source'])
    comic_name = str(re.search('comic_\d{1,4}_raw.txt', comic_name).group())
    comic_no = int(re.search('\d{1,4}',comic_name).group())
    comic_list.append(comic_no)

for comic in comic_list:
    url = "https://xkcd.com/"+str(comic)+"/info.0.json"
    response = urlopen(url)
    data_json = json.loads(response.read())
    print(data_json['img'])