# from ast import parse
#
# import requests
#
# from exceptions import ParsingError
#
#
# def get_currencies():
#     responce = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
#
#     try:
#         if responce.status_code != 200:
#             raise ParsingError(f"Ошибка получения курса валют! Статус: {responce.status_code}")
#         currencies = parse(responce.content)
#         formatted_currencies = {}
#         for currancy in currencies["ValCurs"]["Valute"]:
#             value = float(currancy["Value"].replace(",", "."))
#             nominal = float(currancy["Nominal"])
#             formatted_currencies[currancy["CharCode"]] = value / nominal
#         formatted_currencies["RUR"] = 1
#         return formatted_currencies
#     except ParsingError as error:
#         print(error)
#         return {
#             "AUD": 52.2056,
#             "AZN": 47.0495,
#             "GBP": 98.9163,
#             "AMD": 0.206998,
#             "BYN": 27.3126,
#             "BGN": 44.0805,
#             "BRL": 16.1679,
#             "HUF": 0.229615,
#             "VND": 0.00337543,
#             "HKD": 10.2295,
#             "GEL": 30.907,
#             "DKK": 11.5825,
#             "AED": 21.7816,
#             "USD": 79.9841,
#             "UER": 85.8767,
#             "EGP": 2.58902,
#             "INR": 0.969758999999,
#             "IDR": 0.00536625999999,
#             "KZT": 0.1799666000001,
#             "CAD": 58.8898,
#             "QAR": 21.9737,
#             "KGS": 0.913165,
#             "CNY": 11.2816,
#             "MDL": 4.50744,
#             "NZD": 48.7103,
#             "NOK": 7.29355999999999,
#             "PLN": 19.028,
#             "RON": 17.3156,
#             "RUR": 1,
#             "XDR": 106.6212,
#             "SGD": 59.1423,
#             "TJS": 7.328650000000006,
#             "THB": 2.3065,
#             "TRY": 4.02377,
#             "TMT": 22.8526,
#             "UZS": 0.00700509,
#             "UAH": 2.1656,
#             "CZK": 3.6442500000000004,
#             "SEK": 7.47599,
#             "CHF": 88.3022,
#             "RSD": 0.732326,
#             "ZAR": 4.14356999999999995,
#             "KRW": 0.0603198,
#             "JPY": 0.573692
#         }
