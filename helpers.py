from data import DataForUserCreation


def modify_create_user_body(key, value):
    body = DataForUserCreation.CREATE_USER_BODY.copy()
    body[key] = value
    return body





