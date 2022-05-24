from googleapiclient.discovery import build
import datetime


class SheetsAPI:
    DICT_KEYS = {"№": "id", "заказ №": "order_id", "стоимость,$":
                 "price_usd", "срок поставки": "delivery_date"}

    def __init__(self, token, sheet_id) -> None:
        """
        Creates an object representing a Google Sheets API
        :param token: api token
        :param sheet_id: id of Google Sheets document, e.g. https://docs.google.com/spreadsheets/d/<sheet_id>
        """
        self.token = token
        self.sheet_id = sheet_id

        self.service = None
        self.sheet = None

        if token and sheet_id:
            # Call the Sheets API
            self.service = build('sheets', 'v4', developerKey=self.token)
            self.sheet = self.service.spreadsheets()

    def get_all_cells(self) -> list or None:
        """
        Returns all cells from sheet
        :return: list of dictionaries
        """
        result = self.sheet.values().get(spreadsheetId=self.sheet_id,
                                         range="A1:D").execute()
        values = result.get('values', [])

        if not values:
            return None

        temp = []
        for row in values[1:]:
            dict_ = {}
            for i, key in enumerate(values[0]):
                value = row[i]
                key_ = self.DICT_KEYS.get(key)

                if key_ == "delivery_date":
                    value = datetime.datetime.strptime(row[i], "%d.%m.%Y")
                elif key_ in ["id", "order_id"]:
                    value = int(row[i])

                dict_[key_] = value

            temp.append(dict_)

        return temp
