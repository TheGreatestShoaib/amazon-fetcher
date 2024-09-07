
import json
from logging import error
from pprint import pprint 
from bs4 import BeautifulSoup
import json
import asyncio
import httpx


from fake_useragent import UserAgent
ua = UserAgent()

async def fetch(url):
    try:
        async with httpx.AsyncClient(http2=True) as client:
            # response = await client.get(url)
            # print(response.status_code)
            response = await client.get(url,headers={"User-Agent":ua.random})
            return(response.text)
    except:
        return 10




def name_grabber_not(doctext):  
    soup = BeautifulSoup(doctext, 'html.parser')
    main_container = "s-main-slot s-result-list s-search-results sg-row"
    small_container = "a-section a-spacing-none a-spacing-top-small s-title-instructions-style"
    
    mydiv = soup.find("div",class_=main_container)
    
    if mydiv is None:
        return []
     
    names_a_lot = []
    nextdiv = mydiv.findAll("div",class_=small_container)
    # print(nextdiv) 
    for my in nextdiv:
        name = soup.findAll("span",class_="a-size-base-plus a-color-base a-text-normal")
        # print(name)
        names_a_lot = names_a_lot + [n.text for n in name]
    return names_a_lot



def name_grabber_exact(doctext):  
    soup = BeautifulSoup(doctext, 'html.parser')
    main_container = "sg-col-20-of-24 s-matching-dir sg-col-16-of-20 sg-col sg-col-8-of-12 sg-col-12-of-16"
    small_container = "a-section a-spacing-none puis-padding-right-small s-title-instructions-style"

    mydiv = soup.find("div",class_=main_container)
    
    if mydiv is None:
        return [] 

    names_a_lot = []
    nextdiv = mydiv.findAll("div",class_=small_container)
    for my in nextdiv:
        name = soup.findAll("span",class_="a-size-medium a-color-base a-text-normal")
        names_a_lot = names_a_lot + [n.text for n in name]
    
    return names_a_lot


def finalizer(word):
    
    whole_list = []
    for i in range(0,3):

        url = f"https://www.amazon.com/s?k={word}&page={i}"
        doctext = asyncio.run(fetch(url))
        if doctext == 10:
            return {}
        item_list = name_grabber_exact(doctext)
        if len(item_list) == 0:
            item_list = name_grabber_not(doctext)
            # print("not goting there") 
        whole_list = whole_list + item_list
    
    return whole_list 


# print(finalizer("wall oven"))


# Open and read the JSON file
with open('fetched-cats.json', 'r') as file:
    data = json.load(file)

# Print the data
# print(data)

# false_data = {
#         "Apliance": {
#             "diswasher": {
#                 "baby products":{},
#                 "wall oven":{}
#             },
#             "TV ":{},
#             "Fashion": {},
#             "Food":{
#                 "SSD":{
#                     "Graphics Card":[1,2,3,4]
#
#                     }
#                 }
#
#             }
#     }
#
# data = false_data


data1 = {}
data2 = []
data3 = {"s":1}


def typer(key):

    if type(key) is list:
        return 2 # type list 
    elif type(key) is dict:
        if len(key) == 0:
            return 3 # "Dead End Dicitonary"
        else:
            return 4 # continue digging



for cat_1 in data.keys():
    # print("layer 1",cat_1)
    for cat_2 in data[cat_1].keys():
        typ = typer(data[cat_1][cat_2]) 

        if typ == 3:


            texty_data = data[cat_1][cat_2]
            # print("dead End",cat_2,texty_data) #Dead ENd
            # EKhane Ami texty_data niye request pathabo.   

            data[cat_1][cat_2] = finalizer(texty_data)
            continue

        else:
            # print("layer2",cat_2) 
            for cat_3 in data[cat_1][cat_2].keys():
                typ = typer(data[cat_1][cat_2][cat_3])

                if typ ==3:
                    texty_data = data[cat_1][cat_2][cat_3]
                    print(cat_1,": layer3 : ", cat_3)
                    # print("Another Dead End",cat_3) #Dead ENd
                    data[cat_1][cat_2][cat_3] = finalizer(texty_data) 
                    continue


                else:

                    for cat_4 in data[cat_1][cat_2][cat_3].keys():
                        texty_data = data[cat_1][cat_2][cat_3][cat_4]
                        data[cat_1][cat_2][cat_3][cat_4] = finalizer(texty_data)

#

# pprint(data)

with open('product_fetched.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# for cat_1 in data.keys():
#     print("layer 1:",cat_1)
#
#
#     if type(data[cat_1]) == list:
#         for x in data[cat_1]:
#             print(x)
#
#     else:
#
#         for cat_2 in data[cat_1].keys():
#             print("layer 2:",cat_2) 
#
#             if type(data[cat_1]) == list:
#                 for x in data[cat_1]:
#                     print(x)
#
#             else:
#                 for cat_3 in data[cat_1][cat_2].keys():
#                     print("layer 3:",cat_3)
#
#                     if type(data[cat_1]) == list:
#                         for x in data[cat_1]:
#                             print(x)
#
#                     else:
#                         for cat_4 in data[cat_1][cat_2][cat_3].keys():
#                             print("layer 4:",cat_4)

                            # if type(data[cat_1]) == list:
                            #     for x in data[cat_1]:
                            #         print(x)
                            #
                            # else:
                            #     for cat_5 in data[cat_1][cat_2][cat_3][cat_4].keys():
                            #         print("layer 5:",false_data[cat_5])
