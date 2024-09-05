from faker import Faker
import random
import string

def generate_random_string_for_password(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def generate_user_data():
    fake = Faker()
    user_data = {
        "email": fake.email(),
        "password": generate_random_string_for_password(8),
        "name": fake.name(),
    }
    return user_data

def generate_user_data2():
    fake = Faker()
    user_data = {
        "email": fake.email(),
        "password": generate_random_string_for_password(8),
        "name": fake.name(),
    }
    return user_data

def generate_user_data_for_order_creation():
    fake = Faker()
    user_data = {
        "email": fake.email(),
        "password": generate_random_string_for_password(8),
        "name": fake.name(),
    }
    return user_data