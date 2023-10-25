import requests
from bs4 import BeautifulSoup
import pandas as pd

for page_count in range(1, 298):
    link1 = "https://www.amazon.com.tr/s?i=toys&rh=n%3A12924005031&fs=true&page="
    link2 = "&qid=1696582933&ref=sr_pg_"

    url = link1 + str(page_count) + link2 + str(page_count)
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"}
    page_reguest = requests.get(url, headers=header)
    soup = BeautifulSoup(page_reguest.content, "html.parser")


    content = {}

    title_1 = []
    amount_1 = []


    data = []



    product_class = soup.find_all("div", {"class": "a-section a-spacing-small puis-padding-left-small puis-padding-right-small"})


    for product in product_class:
            title = product.find_all("span", {"class": "a-text-normal"})
            amount = product.find_all("span", {"class": "a-offscreen"})

            for i in title:
                title_1.append(i.text)
            for x in amount:
                amount_1.append(x.text[0:-6].replace(".", ""))

    try:

        for c in range(len(title_1)):
            content = {"adı": title_1[c], "ücret": int(amount_1[c])}
            data.append(content)

    except: IndexError


    for ara in data:
        if "Hot Wheels" in ara["adı"]:
            print(ara)


















