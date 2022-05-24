import asyncio
from g_api_tool.app.tasks import reminders, update_data


def run():
    loop = asyncio.get_event_loop()
    loop.create_task(update_data.updating_data())  # обновление информации в БД
    loop.create_task(reminders.reminding())  # отправка уведомлений в телеграмм
    loop.run_forever()
