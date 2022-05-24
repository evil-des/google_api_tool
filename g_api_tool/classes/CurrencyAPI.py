import requests_cache
from lxml import etree


class CurrencyAPI:
    def __init__(self) -> None:
        self.USD_CODE = "R01235"
        self.url = "https://www.cbr.ru/scripts/XML_daily.asp"
        self.session = requests_cache.CachedSession('db/currency_cache')

    def get_rate(self) -> float or None:
        resp = self.session.get(self.url)

        if resp.status_code != 200:
            return None

        resp_xml_content = resp.content
        tree = etree.XML(resp_xml_content)
        value = tree.xpath(f"//Valute[@ID=\"{self.USD_CODE}\"]/Value"
                           )[0].text.strip("\r\n\t '")  # getting the value

        return float(value.replace(",", "."))

    def get_transformed_rate(self, value: float or int) -> float:
        return float(value) * self.get_rate()
