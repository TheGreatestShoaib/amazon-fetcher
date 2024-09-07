
from os import sched_get_priority_min
import time
from bs4 import BeautifulSoup
import requests
import json
import asyncio
import httpx


# from pprint import pprint
# from fake_useragent import UserAgent
# ua = UserAgent()
#
# print(ua.random)
# url = "https://www.daraz.com.bd/catalog/?spm=a2a0e.tm80335401.search.d_go&q=Bed"
# doc = requests.get(url,headers={"User-Agent":ua.random})
#
# print(doc)
# # with open("hello.html") as fp:
# #     soup = BeautifulSoup(fp, 'html.parser')

async def fetch(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        print(response.status_code)
        return(response.text)



def name_grabber(doctext):  
    soup = BeautifulSoup(doctext, 'html.parser')
    main_container = "sg-col-20-of-24 s-matching-dir sg-col-16-of-20 sg-col sg-col-8-of-12 sg-col-12-of-16"
    small_container = "a-section a-spacing-none puis-padding-right-small s-title-instructions-style"

    mydiv = soup.find("div",class_=main_container)
    nextdiv = mydiv.findAll("div",class_=small_container)

    for my in nextdiv:
        name = soup.findAll("span",class_="a-size-medium a-color-base a-text-normal")

    name_list = [n.text for n in name]
    return name_list



url= "https://www.amazon.com/s?k=Wall+Ovens"
doctext = asyncio.run(fetch(url))

print(name_grabber(doctext))
