from app import authenticate, order, product, shop
from init import app

app.run(host="127.0.0.1", port="8000", debug=True)
