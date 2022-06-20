import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

USERNAME = "USERNAME"
PASSWORD = "PASSWORD"
driver = webdriver.Chrome()
driver.set_window_size(1000, 3000)
driver.get("https://read.amazon.com/kp/notebook")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ap_email"))
    )
finally:
    elem = driver.find_element(By.ID, value="ap_email")
    elem.clear()
    elem.send_keys(USERNAME)
    elem = driver.find_element(By.ID, value="ap_password")
    elem.send_keys(PASSWORD)
    elem.send_keys(Keys.RETURN)

print("logged in")

# Load list of books
elem = driver.find_element(
    By.XPATH, value="//*[@id=\"kp-notebook-library\"]")
books = elem.find_elements(By.XPATH, value="./child::*")

# Holds list of parsed books
parsedBooks = []

# For each book, find the list of highlights
for book in books:
    print("downloading highlights for: " + book.text)
    try:
        book.click()
        parsedHighlights = []
        time.sleep(1)
        highlightWrapper = elem.find_element(
            By.XPATH, value="//*[@id=\"kp-notebook-annotations\"]")
        highlights = highlightWrapper.find_elements(
            By.XPATH, value="./child::*")
        for highlight in highlights:
            if(len(highlight.text) > 0):
                text = re.sub(string=highlight.text,
                              pattern="^.* (Page|Location): .*\nOptions", repl="")
                parsedHighlights.append(text)
                print(text)
            else:
                print("fake")
        coverData = book.text.split("By:")
        newBook = {"title": coverData[0],
                   "Author": coverData[1],
                   "highlights": parsedHighlights}
        parsedBooks.append(newBook)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    except:
        "last book reached"

json_object = json.dumps(parsedBooks, indent=4)
with open("books.json", "w") as outfile:
    outfile.write(json_object)
print("test")
