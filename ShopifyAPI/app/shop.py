import shopify
from init import app, get_auth_session


@app.route("/get_current_shop")
def get_current_shop():
    get_auth_session()

    return str(shopify.Shop.current())
