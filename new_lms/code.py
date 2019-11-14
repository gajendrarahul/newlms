import string,random
from django.contrib.auth.hashers import make_password

def randomcode():
    code = ''
    letters = string.ascii_letters + string.digits
    for i in range(10):
        code = code+str(random.choice(letters))
    return code