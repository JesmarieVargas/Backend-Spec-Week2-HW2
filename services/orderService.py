from database import db 
from models.order import Order 
from sqlalchemy import select 
from models.product import Product
from models.customer import Customer




def find_all(page=1, per_page=10):
    query = select(Order)
    all_orders = db.paginate(query, page=int(page), per_page=int(per_page))

    return all_orders


def find_by_id(order_id):
    query = select(Order).where(Order.id == order_id)
    order = db.session.execute(query).scalar()
    return order


def find_by_customer_id(customer_id):
    query = select(Order).where(Order.customer_id == customer_id)
    orders = db.session.execute(query).scalars().all()
    return orders

def find_by_email(email):
    query = select(Order).join(Customer).where(Customer.id==Order.customer_id).where(Customer.email == email)
    orders = db.session.execute(query).scalars().all()

    return orders