class User:
    def __init__(self, user_id, name, email, address):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.address = address
        self.orders = []

    def create_order(self, order):
        self.orders.append(order)


class Product:
    def __init__(self, product_id, name, description, price, stock):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock


class Order:
    def __init__(self, order_id, user, order_status="pending"):
        self.order_id = order_id
        self.user = user
        self.products = []
        self.order_status = order_status
        self.payment_status = "unpaid"

    def add_product(self, product):
        self.products.append(product)

    def process_payment(self, payment):
        self.payment_status = "paid"
        self.order_status = "completed"


class Payment:
    def __init__(self, payment_id, payment_type, order):
        self.payment_id = payment_id
        self.payment_type = payment_type
        self.order = order
        self.payment_date = None

    def make_payment(self, date):
        self.payment_date = date
        self.order.process_payment(self)
