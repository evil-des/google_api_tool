from googleapiclient.discovery import build


class SheetsAPI:
    def __init__(self, token, sheet_id):
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
                dict_[key] = row[i]
            temp.append(dict_)

        return temp
