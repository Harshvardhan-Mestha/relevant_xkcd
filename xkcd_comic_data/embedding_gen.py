from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import langchain
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS






# def test_eight_components():
#     driver = webdriver.Chrome()

#     driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#     title = driver.title
#     assert title == "Web form"

#     driver.implicitly_wait(0.5)

#     text_box = driver.find_element(by=By.NAME, value="my-text")
#     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

#     text_box.send_keys("Selenium")
#     submit_button.click()

#     message = driver.find_element(by=By.ID, value="message")
#     value = message.text
#     assert value == "Received!"

#     driver.quit()

# test_eight_components()
exp = ""

def extract_explanation():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.explainxkcd.com/wiki/index.php/1:_Barrel_-_Part_1")
    exp = driver.find_element(By.ID,'content')
    with open('./xkcd_comic_data/temp.txt', 'w') as f:
        f.write(str(exp.text))

    #print(exp.text)
    driver.quit()


def generate_embedding():
    loader = TextLoader('/Users/harshvardhanmestha/repos/relevant_xkcd/xkcd_comic_data/temp.txt')
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=250, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = FAISS.from_documents(docs, embeddings)
    
    db.save_local("/Users/harshvardhanmestha/repos/relevant_xkcd/xkcd_comic_data/comic_1")

    query = "comics about optimism"
    docs = db.similarity_search(query)
    print(docs)



extract_explanation()
generate_embedding()

