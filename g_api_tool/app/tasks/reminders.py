from g_api_tool.data import db_session
from g_api_tool.data.__all_models import SheetData
from g_api_tool.misc import config
import datetime
import asyncio
import logging
import requests


async def reminding():
    while True:
        db_sess = db_session.create_session()
        sheet_data = db_sess.query(SheetData).all()
        for item in sheet_data:
            if datetime.datetime.today() == item.delivery_date:
                requests.post(
                    f"https://api.telegram.org/bot{config['reminders']['telegram_api_token']}/sendMessage",
                    data={
                        "chat_id": config['reminders']['chat_id'],
                        "text": f"Для заказа №{item.order_id} истек срок поставки ({item.delivery_date})!"
                    }
                )
                logging.info(f"[!] [{datetime.datetime.now()}] [#{item.order_id}] - "
                             f"Отправлено уведомление в телеграмм для {config['reminders']['chat_id']}")
            await asyncio.sleep(2)

        await asyncio.sleep(60 * 60)
