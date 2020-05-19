import json
import os
import stripe

# This is your real test secret API key.
stripe.api_key = "sk_test_tAmci4gVQozuaWoWyxsCxEXg00UbHmVlzw"


def calculate_order_amount(items):
    # Replace this constant with a calculation of the order's amount
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client
    return 1400
