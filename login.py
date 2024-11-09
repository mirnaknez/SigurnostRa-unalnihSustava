import sys
import getpass
import json
import bcrypt
from Crypto.Hash import SHA256

def hash_user(d):
    h = SHA256.new(d.encode('utf-8'))
    return h.hexdigest()

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))
    
def login(user):
    with open("user.json", "r") as f:
        data = json.load(f)
    
    for a in range(3): 
        password = getpass.getpass("Password: ")
        if hash_user(user) not in data:
            print("Username or password incorrect.")
            return
        if check_password(data[hash_user(user)]['p'], password):
            if data[hash_user(user)]['f']: 
                n_password = getpass.getpass("New password: ")
                r_password = getpass.getpass("Repeat new password: ")
                if n_password == r_password:
                    data[hash_user(user)]['p'] = hash_password(n_password)
                    data[hash_user(user)]['f'] = False 
                    with open("user.json", "w") as f:
                        json.dump(data, f)
                    print("Password changed successfully.")
                else:
                    print("Username or password incorrect.")
                    return
            print("bash$")
            return
        else:
            print("Username or password incorrect.")

user = sys.argv[1]
login(user)