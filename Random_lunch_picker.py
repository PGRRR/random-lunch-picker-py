import random
import bs4
import webbrowser
from ast import keyword
from bs4 import BeautifulSoup
from html.entities import name2codepoint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import *
from tkinter import *

menu = ["한식","양식","중식","일식"]
random_menu = random.choice(menu)
location = "미금역"
URL = "https://www.google.co.kr/maps/search/" + location + random_menu

options = Options()
options.add_argument('headless')
options.add_argument('incognito')
options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome("/Users/iseon-u/Document/chromedriver/chromedriver", options=options)
driver.get(url=URL)
driver.implicitly_wait(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
sleep(1)
result = soup.find_all('a', class_="a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")

storelist = []
storelink = []

for i in result:
    storelist.append(i['aria-label'])
for i in result:
    storelink.append(i['href'])


print(len(storelist))

random_num = random.randrange(0,len(storelist))

print(random_num)
print(storelist[random_num])
print(storelink[random_num])

root = Tk()
root.title("오늘은 이게 땡겨요")

root.geometry("150x150")
root.resizable(False, False)

label1 = Label(root, text="오늘은")
label1.pack()

label2 = Label(root, text="{ 😋 }")
label2.pack()

label3 = Label(root, text="🎉")

def btncmd():
    print("클릭")
    label2.config(text=storelist[random_num])
    label3.pack()
    btn2.pack()

btn1 = Button(root, text="땡겨요", command=btncmd)
btn1.pack()

def btnmap():
    webbrowser.open(storelink[random_num])

btn2 = Button(root, text="지도 바로가기", command=btnmap)

root.mainloop()