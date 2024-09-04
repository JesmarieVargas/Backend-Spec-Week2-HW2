from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
# from models.customer import Customer
# from models.product import Product


order_products = db.Table(
    "order_products",
    Base.metadata, # allow this table to locate the foreign keys from the Base class
    db.Column('order_id', db.ForeignKey('orders.id'), primary_key= True),
    db.Column('product_id', db.ForeignKey('products.id'), primary_key= True)
)

class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True) #primary keys auto increment
    customer_id: Mapped[int] = mapped_column(db.ForeignKey("customers.id"))
    product_id: Mapped[int] = mapped_column(db.Integer(), nullable=False, unique=True)
    quantity: Mapped[str] = mapped_column(db.Integer(), nullable=False)

    # create our many-one relationship to the customer table
    customer: Mapped['Customer'] = db.relationship(back_populates='orders')
    # create a many-many relationship to Products through our association table order_products
    products: Mapped[List['Product']] = db.relationship(secondary=order_products)

