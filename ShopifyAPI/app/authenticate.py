import binascii
import os

import shopify
from flask import redirect, request
from init import app, get_session, redirect_url

scopes = [
    "read_assigned_fulfillment_orders",
    "write_assigned_fulfillment_orders",
    "read_checkouts",
    "write_checkouts",
    "read_content",
    "write_content",
    "read_customers",
    "write_customers",
    # "read_customer_payment_methods",
    "read_discounts",
    "write_discounts",
    "read_draft_orders",
    "write_draft_orders",
    "read_files",
    "write_files",
    "read_fulfillments",
    "write_fulfillments",
    "read_gift_cards",
    "write_gift_cards",
    "read_inventory",
    "write_inventory",
    "read_legal_policies",
    "read_locales",
    "write_locales",
    "read_locations",
    "read_marketing_events",
    "write_marketing_events",
    # "read_merchant_approval_signals",
    "read_merchant_managed_fulfillment_orders",
    "write_merchant_managed_fulfillment_orders",
    "read_orders",
    "write_orders",
    # "read_payment_mandate",
    # "write_payment_mandate",
    "read_payment_terms",
    "write_payment_terms",
    "read_price_rules",
    "write_price_rules",
    "read_products",
    "write_products",
    "read_product_listings",
    # "read_publications",
    # "write_publications",
    "read_purchase_options",
    "write_purchase_options",
    "read_reports",
    "write_reports",
    "read_resource_feedbacks",
    "write_resource_feedbacks",
    "read_script_tags",
    "write_script_tags",
    "read_shipping",
    "write_shipping",
    "read_shopify_payments_disputes",
    "read_shopify_payments_payouts",
    # "read_own_subscription_contracts",
    # "write_own_subscription_contracts",
    "read_themes",
    "write_themes",
    "read_translations",
    "write_translations",
    "read_third_party_fulfillment_orders",
    "write_third_party_fulfillment_orders",
    # "read_users",
    "read_order_edits",
    "write_order_edits",
    # "write_payment_gateways",
    # "write_payment_sessions",
]


@app.route("/authorize")
def authorize():
    session = get_session()
    state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
    permission_url = session.create_permission_url(scopes, redirect_url, state)
    return redirect(permission_url)


@app.route("/callback")
def callback():
    session = get_session()
    access_token = session.request_token(request.args)
    return access_token
