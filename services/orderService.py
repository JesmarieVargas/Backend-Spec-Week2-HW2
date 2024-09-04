from database import db 
from models.order import Order 
from sqlalchemy import select 
from models.product import Product


def save(order_data):

    new_order = Order(customer_id=order_data['customer_id'], product_id=order_data['product_id'], quantity=order_data['quantity'])
    db.session.add(new_order)
    db.session.commit() 

    db.session.refresh(new_order)
    return new_order


def find_all(page=1, per_page=10):
    query = select(Order)
    all_orders = db.paginate(query, page=int(page), per_page=int(per_page))

    return all_orders
