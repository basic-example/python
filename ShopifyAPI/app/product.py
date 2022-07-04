import shopify
from init import app, get_auth_session


@app.route("/list_products")
def list_products():
    get_auth_session()
    products = shopify.Product.find(limit=2)
    return str(products)


@app.route("/list_products_page_2")
def list_products_page_2():
    get_auth_session()
    products = shopify.Product.find(limit=2)
    products2 = products.next_page()
    return str(products2)
