import asyncio
from g_api_tool.misc import config
from g_api_tool.classes.SheetsAPI import SheetsAPI


def run():
    sheets_api = SheetsAPI(token=config["app"]["google_api_token"],
                           sheet_id=config["app"]["sheet_id"])
    c = sheets_api.get_all_cells()
    print(c)
