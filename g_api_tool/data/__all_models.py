import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Form(SqlAlchemyBase):
    __tablename__ = "sheet_data"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    order_id = sqlalchemy.Column(sqlalchemy.BigInteger)
    price_usd = sqlalchemy.Column(sqlalchemy.Float, default=0)
    price_rub = sqlalchemy.Column(sqlalchemy.Float, default=0)
    delivery_date = sqlalchemy.Column(sqlalchemy.Date)

    update_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
