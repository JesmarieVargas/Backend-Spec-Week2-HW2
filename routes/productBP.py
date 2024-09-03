from flask import Blueprint
from controllers.customerController import save, find_all


product_blueprint = Blueprint('product_bp', __name__)

#url_prefix for this blueprint is /products

product_blueprint.route('/', methods=['POST'])(save) #triggers the save function on POST request to /customers
product_blueprint.route('/', methods=['GET'])(find_all)