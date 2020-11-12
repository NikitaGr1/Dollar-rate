import requests
from lxml import etree
xml_response = etree.fromstring(requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text.encode("1251"))
curs = xml_response.find("Valute[@ID='R01235']/Value").text
print(f"Один Доллар США равен {curs} рублей")