from database import db #services interact directly with the db
from models.order import Order #need this to create order objects
from sqlalchemy import select #so we can query our db
from models.product import Product


def save(order_data):

    new_order = Order(customer_id=order_data['customer_id'], product_id=order_data['product_id'], quantity=order_data['quantity'])
    db.session.add(new_order)
    db.session.commit() 

    db.session.refresh(new_order)
    return new_order


def find_all():
    query = select(Order)
    all_orders = db.session.execute(query).scalars().all()

    return all_orders
