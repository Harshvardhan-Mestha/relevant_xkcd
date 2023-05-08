import langchain
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import time



embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

main = FAISS.load_local("xkcd_comic_data/comic_faiss/faiss_main", embeddings)

for i in range(0,2772):
    st = time.time()
    add = FAISS.load_local("xkcd_comic_data/comic_faiss/comic_"+str(i+1), embeddings)
    main.merge_from(add)
    print("comic "+str(i+1)+"complete")
    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

main.save_local("xkcd_comic_data/comic_faiss/faiss_main")



print(main.docstore._dict)
