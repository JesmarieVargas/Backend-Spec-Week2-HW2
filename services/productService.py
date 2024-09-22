from database import db 
from models.product import Product
from sqlalchemy import select 


def save(product_data):

    new_product = Product(name=product_data['name'], price=product_data['price'])
    db.session.add(new_product)
    db.session.commit() 

    db.session.refresh(new_product)
    return new_product


def find_all(page=1, per_page=10):
    query = select(Product)
    all_products = db.paginate(query, page=int(page), per_page=int(per_page))

    return all_products

# def search_product(search_term):
#     query = select(Product).where(Product.name.like(f'%{search_term}%'))
#     search_products = db.session.execute(query).scalars().all()
    
#     return search_products