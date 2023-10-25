import requests
from bs4 import BeautifulSoup
import pandas as pd



for change_page in range(1, 3):

    page_url_1 = "https://www.amazon.com.tr/gp/bestsellers/computers/12601898031/ref=zg_bs_pg_2_computers?ie=UTF8&pg="+str(change_page)
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.43"}
    request_1 = requests.get(page_url_1, headers=header)
    connect_1 = BeautifulSoup(request_1.content, "html.parser")


    page_1 = connect_1.find_all("div", {"class": "p13n-gridRow _cDEzb_grid-row_3Cywl"})

    name_Table = []
    amount_Table = []
    table = {}

    for i in page_1:
        name = i.find_all("div", {"class": "_cDEzb_p13n-sc-css-line-clamp-3_g3dy1"})
        amount = i.find_all("span", {"class": "_cDEzb_p13n-sc-price_3mJ9Z"})


        for x in name:
            name_Table.append(x.text)
        for c in amount:
            amount_Table.append(int(c.text[0:-6].replace(".", "")))



    data = []

    for j in range(len(name_Table)):
        table = {"name": name_Table[j], "amount": amount_Table[j]}
        data.append(table)


    excel_transfer = pd.DataFrame(data)
    excel_transfer.to_excel("BeatufulSoup3.xlsx")

    print(excel_transfer)















































# for i in page_1:
#     link_1 = i.find("a", {"class": "s-no-outline"}).get("href")
#     link_2 = "https://www.amazon.com.tr"
#     link_3 = link_2 + link_1
#
#     print(link_3)


    # page_url_2 = link_3
    # header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.43"}
    # request_2 = requests.get(page_url_2, headers=header)
    # connect_2 = BeautifulSoup(request_2.content, "html.parser")
    #
    # page_2 = connect_2.find_all("div", {"class": "a-column a-span6"})
    #
    # # for x in page_2:
    # #     link_4 = x.find_all("h1")
    # #     for c in link_4:
    # #         link_5 = c.find("span", {"class": "product-title-word-break"})
    # #         print(link_5)
    #
    # for x in page_2:
    #     link_4 = x.find_all("tr")
    #     for c in link_4:
    #         link_5 = c.find("th", {"class": "a-color-secondary a-size-base prodDetSectionEntry"}).string[0:-1]
    #         link_6 = c.find("td", {"class": "a-size-base prodDetAttrValue"}).string[-6:-1]
    #         print(link_5, "=", link_6)
    # print("********************************************")























