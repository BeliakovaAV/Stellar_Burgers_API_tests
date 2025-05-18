from data import DataForUserCreation


def modify_create_user_body(key, value):
    body = DataForUserCreation.CREATE_USER_BODY.copy()
    body[key] = value
    return body


def update_payload(email=None, name=None):
    payload = {}
    if email is not None:
        payload["email"] = email
    if name is not None:
        payload["name"] = name
    return payload
