import re

from utils.soup import getSoup
from utils.caesar_cipher_enc_dec import decode
page = f"http://127.0.0.1:5000/caesar/"
soup = getSoup(page)

soup.find("p", id_ = "row_1475320103840")
#soup.find_all("p", class_ = "CDt4Ke") #from MDST website
#can do len() around

[x.text for x in soup.find_all()]