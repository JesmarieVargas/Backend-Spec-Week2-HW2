from database import db #services interact directly with the db
from models.customer import Customer #need this to create customer objects
from sqlalchemy import select #so we can query our db
from utils.util import encode_role_token 
from models.product import Product
from datetime import date
from models.order import Order


def save(customer_data):

    new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'], username=customer_data['username'], password=customer_data['password'], admin=customer_data['admin'])
    db.session.add(new_customer)
    db.session.commit() #adding our new customer to our db
    print("Commited new product to our db")
    db.session.refresh(new_customer)
    return new_customer


def find_all(page=1, per_page=10):
    query = select(Customer)
    all_customers = db.paginate(query, page=int(page), per_page=int(per_page)) #our paginated query is dependant on a page number and how many we wish to show per page

    return all_customers

def login(credentials):
    query = select(Customer).where(Customer.email == credentials['email'])
    customer = db.session.execute(query).scalar_one_or_none()

    if customer and customer.password == credentials['password']: #if there is a customer, check their password
        auth_token = encode_role_token(customer.id, customer.admin)
        return auth_token
    
    return None

def add_item_to_cart(item_data):
    #query customer and item and db.session.add and commit
    query = select(Customer).where(Customer.id==item_data['customer_id'])
    customer = db.session.execute(query).scalar()
    query2 = select(Product).where(Product.id==item_data['product_id'])
    item = db.session.execute(query2).scalar()
    customer.cart.append(item)
    
    db.session.add(customer)
    db.session.commit()
    db.session.refresh(customer)

    return customer



def remove_item_from_cart(item_data):
    query = select(Customer).where(Customer.id==item_data['customer_id'])
    customer = db.session.execute(query).scalar()
    query2 = select(Product).where(Product.id==item_data['product_id'])
    item = db.session.execute(query2).scalar()
    customer.cart.remove(item)
    
    db.session.add(customer)
    db.session.commit()
    db.session.refresh(customer)

    return customer


def view_cart(customer_id):
    query = select(Customer).where(Customer.id==customer_id)
    customer = db.session.execute(query).scalar()
    return customer


def empty_cart(item_data):
    query = select(Customer).where(Customer.id==item_data['customer_id'])
    customer = db.session.execute(query).scalar()
    customer.cart = []
    
    db.session.add(customer)
    db.session.commit()
    db.session.refresh(customer)
    
    return customer.cart



def place_order(item_data):
    query = select(Customer).where(Customer.id==item_data['customer_id'])
    customer = db.session.execute(query).scalar()
    order = Order(customer_id=customer.id, order_date=date.today())
    for item in customer.cart:
        order.products.append(item)

    db.session.add(order)
    db.session.commit()
    db.session.refresh(order)

    customer.cart = []

    db.session.add(customer)
    db.session.commit()
    db.session.refresh(customer)
    
    return order