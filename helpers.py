from data import DataForUserCreation


def modify_create_user_body(key, value):
    body = DataForUserCreation.CREATE_USER_BODY.copy()
    body[key] = value
    return body


def validate_user_orders_structure(orders, required_fields):
    for order in orders:
        for field in required_fields:
            if field not in order:
                return False
    return True
