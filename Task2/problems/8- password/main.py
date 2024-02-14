import random
import string
def generate_password():
    characters = " " + string.punctuation + string.digits + string.ascii_letters
    password = ''.join(random.choice(characters) for _ in range(8))
    return password

random_password = generate_password()
print(random_password)
