from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import langchain
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import time
from urllib.request import urlopen
import json


exp = ""
titles = list()



url = "https://xkcd.com/info.0.json"
response = urlopen(url)
data_json = json.loads(response.read())

total_sites = int(data_json['num'])





def extract_explanation(n):
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.explainxkcd.com/wiki/index.php/"+str(n))
    driver.implicitly_wait(1.5)

    exp = driver.find_element(By.ID,'content')
    with open("./xkcd_comic_data/comic_raw/comic_"+str(n)+"_raw.txt", "w") as f:
        f.write(str(exp.text))

    #print(exp.text)
    driver.quit()





def generate_embedding():
    loader = TextLoader('/Users/harshvardhanmestha/repos/relevant_xkcd/xkcd_comic_data/comic_raw/comic_1_raw.txt')
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=250, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = FAISS.from_documents(docs, embeddings)
    
    db.save_local("/Users/harshvardhanmestha/repos/relevant_xkcd/xkcd_comic_data/comic_1")

    query = "comics about optimism"
    docs = db.similarity_search(query)
    print(docs)


#extract_explanation()
#generate_embedding()

def extract_all_exp():
    for i in range(1178,total_sites+1):
        extract_explanation(i+1)

extract_all_exp()

#extract_explanation(792)