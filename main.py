import preprocessing as pp
import open_ai

text = """@brstnhrz @albyrkaysnrr #depremadres 
https://t.co/r9F70fbOL5

Abdurrahman Albayrak
Pınar İlkay Albayrak
Ruşen Ali Albayrak

Emek Rüstem Tümer Paşa Cd. No:31 Gözde Servis üstü Hatay/Antakya 

44 saattir haber alınamıyor"""

clean_text = pp.clean_hash_ment(text)
result = open_ai.data_extractor(clean_text)

print(result["choices"][0]["text"])

