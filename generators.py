from faker import Faker

fake = Faker()


def generate_user_creation_body():
    return {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name()
    }


def generate_update_info():
    return {
        "email": fake.email(),
        "name": fake.first_name()
    }
