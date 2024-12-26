import requests
from bs4 import BeautifulSoup



url = requests.get("https://www.pttavm.com/arama/zeytinyagi?q=zeytin+ya%C4%9F&order=sell_count_desc")
if url.status_code ==200:
    print("Siteden Veri Çekilebilir")
else:
    print("Siteden Veri Çekilemez")

soup = BeautifulSoup(url.content,"html.parser")


sayı = 1

for i in soup.find("ul", {"class": "catalog-view"}).find_all("li", {"class": "gg-w-6"}):
    başlık_al = i.find("div", {"class": "gg-w-24"}).span.text
    fiyat_al = i.find("p", {"class": "fiyat"}).text.strip().replace(" ", "").replace(".", "")
    kargo_durumu_al = i.find("li", {"class": "shippingFree"}).text.strip().replace("Ücretsiz Kargo", "Ücretsiz Kargo-Aynı Gün Kargolama")
    
    
    print(f"{sayı}: Ürün Adı: {başlık_al}\nFiyat: {fiyat_al}\nKargo Durumu: {kargo_durumu_al}\n")
    sayı += 1

print("--"*55)
    