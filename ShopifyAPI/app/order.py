import shopify
from init import app, get_auth_session


@app.route("/list_orders")
def list_orders():
    get_auth_session()
    orders = shopify.Order.find(
        limit=250,
        fields="""
            id,
            financial_status,
            current_total_tax_set,
            created_at,
            billing_address222
        """,
    )
    print(orders)
    for order in orders:
        print("###", order, order.to_dict())
    return str(orders)


@app.route("/list_orders_page_2")
def list_orders_page_2():
    get_auth_session()
    orders = shopify.Order.find(limit=2)
    orders2 = orders.next_page()
    return str(orders2)
