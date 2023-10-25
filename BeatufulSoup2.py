import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

try:
    while True:

        url = "https://finans.mynet.com/borsa/hisseler/"
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.41"}
        connect = requests.get(url, headers=header)

        page = BeautifulSoup(connect.content, "html.parser")



        data = {}
        yazdır = []
        port_föy = ["AKSA AKSA",
                    "EREGL EREGLI DEMIR CELIK",
                    "FROTO FORD OTOSAN",
                    "ISDMR ISKENDERUN DEMIR CELIK",
                    "TBORG T.TUBORG",
                    "VESBE VESTEL BEYAZ ESYA"]

        port_Föy_Aktarım = []

        for search in page.find_all("tr"):
            try:
                firma_Kod = search.find("strong", {"class": "mr-4"}).text
                donustur = search.find_all("td", {"class": "text-center"})[1].string.replace(",", ".")
                firma_Tutar = float(donustur)
                data = {"firma Adı": firma_Kod, "firma Tutar": firma_Tutar}
                yazdır.append(data)
            except: AttributeError, PermissionError

        sayı = 0
        for i in yazdır:
            try:
                if port_föy[sayı] in i["firma Adı"]:
                    sayı += 1
                    port_Föy_Aktarım.append(i)
            except: IndexError, PermissionError


        aktarım = pd.DataFrame(port_Föy_Aktarım)
        aktarım.to_excel("port_föy_Aktarım.xlsx")

        print(port_Föy_Aktarım)
        time.sleep(60)
except: PermissionError















