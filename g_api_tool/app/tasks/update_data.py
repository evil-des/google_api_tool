from g_api_tool.data import db_session
from g_api_tool.data.__all_models import SheetData
from g_api_tool.misc import config, currency_api, object_as_dict
from g_api_tool.classes.SheetsAPI import SheetsAPI
import datetime
import asyncio
import logging
import collections


async def updating_data():
    while True:
        sheets_api = SheetsAPI(token=config["app"]["google_api_token"],
                               sheet_id=config["app"]["sheet_id"])
        cells = sheets_api.get_all_cells()
        db_sess = db_session.create_session()
        msg_text = None

        for item in cells:
            sheet_data = db_sess.query(SheetData).filter(SheetData.order_id == item["order_id"]).first()

            if not sheet_data:  # if cell not in database
                new_cell = SheetData(id=item["id"], order_id=item["order_id"], price_usd=item["price_usd"],
                                     price_rub=currency_api.get_transformed_rate(item["price_usd"]),
                                     delivery_date=item["delivery_date"])
                db_sess.add(new_cell)
                msg_text = "Новая запись добавлена в базу данных"

            elif collections.Counter(object_as_dict(sheet_data)) == \
                    collections.Counter(item.values()):  # if cell is edited

                sheet_data.order_id = item["order_id"]
                sheet_data.price_usd = item["price_usd"]
                sheet_data.price_rub = currency_api.get_transformed_rate(item["price_usd"])
                sheet_data.delivery_date = item["delivery_date"]
                sheet_data.update_date = datetime.datetime.now()
                msg_text = "Запись отредактирована!"

            if msg_text:
                try:
                    db_sess.commit()
                    logging.info(f"[!] [{datetime.datetime.now()}] [#{sheet_data.order_id}] - {msg_text}")
                except Exception as e:
                    db_sess.rollback()

        # deleting unused cells
        all_sheet_data = db_sess.query(SheetData).all()
        for item in get_unused_cells(cells, all_sheet_data):
            db_sess.delete(item)
            db_sess.commit()
            logging.info(f"[!] [{datetime.datetime.now()}] [#{item.order_id}] - "
                         f"Запись удалена!")

        await asyncio.sleep(60 * 60)


def get_unused_cells(all_cells, all_sheet_data) -> list or None:
    order_ids = list(map(lambda x: x["order_id"], all_cells))
    deleted = list(filter(lambda x: x.order_id not in order_ids, all_sheet_data))
    return deleted
