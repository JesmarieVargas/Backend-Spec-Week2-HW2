from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from models.order import order_products
from typing import List
from models.order import Order
from models.shoppingCart import cart

class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True) #primary keys auto increment
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    price: Mapped[str] = mapped_column(db.Float(12), nullable=False)

    orders: Mapped[List['Order']] = db.relationship(secondary=order_products)
    cart: Mapped[List['Product']] = db.relationship(secondary=cart)