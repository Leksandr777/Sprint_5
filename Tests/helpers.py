import random

def generate_email():
    text_mail = 'new_user'
    return f"{text_mail}{random.randint(1, 10000)}@testmail.com"