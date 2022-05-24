from g_api_tool.data import db_session
import logging
from g_api_tool.app import app

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    db_session.global_init("db/database.db")
    app.run()
