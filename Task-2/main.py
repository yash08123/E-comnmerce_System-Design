def process_orders(products, orders):
    restock_alerts = []
    for order in orders:
        for product_id, quantity in order.items():
            if products[product_id].stock >= quantity:
                products[product_id].stock -= quantity
                if products[product_id].stock < 10:
                    restock_alerts.append(product_id)
            else:
                raise Exception(f"Insufficient stock for Product ID: {product_id}")
    return restock_alerts


def restock_items(products, restock_list):
    for product_id, quantity in restock_list.items():
        products[product_id].stock += quantity
