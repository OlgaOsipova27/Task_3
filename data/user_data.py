import random
import string

TEST_EMAIL = "test_user1@yandex.ru"
TEST_PASSWORD = "password123!4354@#"


def generate_random_string(length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_user_data():
    random_part = generate_random_string()
    return {
        "name": f"user-{random_part}",
        "email": f"test-{random_part}@yandex.ru",
        "password": f"pass-{generate_random_string(8)}"
    }
