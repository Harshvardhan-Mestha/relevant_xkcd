
import langchain
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import time

st = time.time()



def generate_embedding(n):
    loader = TextLoader('/Users/harshvardhanmestha/repos/relevant_xkcd/xkcd_comic_data/comic_raw/comic_'+str(n)+'_raw.txt')
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=250, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = FAISS.from_documents(docs, embeddings)
    db.save_local("/Users/harshvardhanmestha/repos/relevant_xkcd/xkcd_comic_data/comic_faiss/comic_"+str(n))


def build_all_faiss():
    
    for i in range(0,772+1):
        st = time.time()
        generate_embedding(i+1)
        print("comic "+str(i+1)+"complete")
        et = time.time()
        elapsed_time = et - st
        print('Execution time:', elapsed_time, 'seconds')

build_all_faiss()