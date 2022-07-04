import os

import shopify
from dotenv import load_dotenv
from flask import Flask

load_dotenv(os.path.join(os.path.dirname(__file__)))

api_version = "2022-04"
client_id = os.getenv("CLIENT_ID")
secret_id = os.getenv("SECRET_ID")
shop_url = os.getenv("SHOP_URL")
redirect_url = os.getenv("REDIRECT_URL")
access_token = os.getenv("ACCESS_TOKEN")
app = Flask(__name__)


def get_auth_session():
    shopify.Session.setup(api_key=client_id, secret=secret_id)
    session = shopify.Session(shop_url, api_version, access_token)
    shopify.ShopifyResource.activate_session(session)
    return session


def get_session():
    shopify.Session.setup(api_key=client_id, secret=secret_id)
    session = shopify.Session(shop_url, api_version)
    shopify.ShopifyResource.activate_session(session)
    return session
