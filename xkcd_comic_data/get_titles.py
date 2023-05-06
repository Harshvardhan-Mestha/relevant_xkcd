from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


titles = list()

def get_comic_titles():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("https://xkcd.com/archive/")
    middle = driver.find_element(By.ID,'middleContainer')
    title_elements = middle.find_elements(By.CSS_SELECTOR,'a')
    for title_element in title_elements:
        titles.append(title_element.text)

    with open('./xkcd_comic_data/comic_titles.txt', 'w') as f:
        for i in range(0,len(titles)):
            titles[i] = titles[i].replace(" ","_")
            f.write(str(len(titles)+1-i)+":_"+str(titles[i])+"\n")