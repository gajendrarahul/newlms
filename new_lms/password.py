import string,random
from django.contrib.auth.hashers import make_password

def randomPassword():
    password = ''
    letters = string.ascii_letters + string.digits + string.punctuation
    for i in range(10):
        password = password+str(random.choice(letters))
    return password