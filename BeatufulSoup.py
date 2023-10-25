import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

while True:

    url = "https://finans.mynet.com/borsa/hisseler/"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.41"}
    connect = requests.get(url, headers=header)

    page = BeautifulSoup(connect.content, "html.parser")

    data = {}
    yazdır = []

    for search in page.find_all("tr"):
        try:
            firma_Kod = search.find("strong", {"class": "mr-4"}).text
            donustur = search.find_all("td", {"class": "text-center"})[1].string.replace(",", ".")
            firma_Tutar = float(donustur)
            data = {"firma Adı": firma_Kod, "firma Tutar": firma_Tutar}
            yazdır.append(data)
        except: AttributeError


    try:

        aktar = pd.DataFrame(yazdır)
        aktar.to_excel("aktarım1.xlsx")

    except: PermissionError

    print(yazdır)
    time.sleep(60)















