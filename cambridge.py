import requests
from bs4 import BeautifulSoup
import sys
import sqlite3
import os

if not os.path.isfile("database.db"):
    exists = False
else:
    exists = True

conn = sqlite3.connect("database.db")
c = conn.cursor()

if exists == False:
    c.execute('''CREATE TABLE dictionary(word TEXT, meaning TEXT)''')

headers = {
    "Accept-Encoding": "gzip, deflate, br",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Sec-Gpc": "1",
    "Accept-Language": "en-US,en;q=0.6",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Sec-Fetch-Mode": "navigate"
}

word = ' '.join([str(elem) for elem in sys.argv[1:]])
c.execute('''SELECT * FROM dictionary WHERE word  = ?''', (word,))
entry = c.fetchone()

def cambridge(word):
    url = "https://dictionary.cambridge.org/dictionary/english/" + word
    response = requests.get(url, headers=headers)
    remove = ["A1", "A2", "B1", "B2", "C1"]
    soup = BeautifulSoup(response.text, "html.parser")
    print(f'{soup.find(class_="ti fs fs12 lmb-0 hw superentry").get_text()}:')
    num = 0
    meaning_ = ""
    for item in soup.select(".ddef_h"):
        num += 1
        a = item.get_text().lstrip(" ").rstrip(": ").split()
        a_list = [word for word in a if word not in remove]
        actual = ' '.join(a_list)
        meaning_ = meaning_ + f'{num}. {actual}\n'
    print(meaning_) 
    c.execute('''INSERT INTO dictionary VALUES(?,?)''', (word, meaning_))

def indb(word):
    if entry:
        print(f"Meaning of {entry[0]} in English: ")
        print(entry[1])
    else:
        cambridge(word)

try:
    indb(word)
except:
    print("Something went wrong!")
    print("Possibly the word you entered is not in the dictionary or there's a connection issue")

conn.commit()
conn.close()
