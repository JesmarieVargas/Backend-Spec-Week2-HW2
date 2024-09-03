from . import ma
from marshmallow import fields

class OrderSchema(ma.Schema): #Inherting our instance of Marshmallow 
    id = fields.Integer(required=False) #This will be auto-incremented
    customer_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True) 

    class Meta:
        fields = ("id", "customer_id", "product_id", "quantity") #all fields that could be coming in and going out when validating data

order_schema = OrderSchema() #instantiate a single customer schema
orders_schema = OrderSchema(many=True, exclude=["password"])