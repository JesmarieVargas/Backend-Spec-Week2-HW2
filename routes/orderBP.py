from flask import Blueprint
from controllers.orderController import find_by_email, find_by_customer_id, find_by_id, save, find_all


order_blueprint = Blueprint('order_bp', __name__)

#url_prefix for this blueprint is /orders

order_blueprint.route('/', methods=['POST'])(save) #triggers the save function on POST request to /customers
order_blueprint.route('/', methods=['GET'])(find_all)
order_blueprint.route('/<int:order_id>', methods=['GET'])(find_by_id)
order_blueprint.route('/customer/<int:customer_id>', methods=['GET'])(find_by_customer_id)
order_blueprint.route('/customer-email', methods=["POST"])(find_by_email)