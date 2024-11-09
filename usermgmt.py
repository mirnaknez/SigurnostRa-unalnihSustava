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

def add(user):
    password = getpass.getpass("Password: ")
    repeat_password = getpass.getpass("Repeat Password: ")
    
    if password != repeat_password:
        print("User add failed. Password mismatch.")
        return
    
    with open("user.json", "r") as f:
        data = json.load(f)
        
    
    data[hash_user(user)] = {'p': hash_password(password), 'f': False}
    
    with open("user.json", "w") as f:
        json.dump(data, f)
    
    print("User successfully added.")

def passwd(user):
    new_password = getpass.getpass("New Password: ")
    repeat_new_password = getpass.getpass("Repeat New Password: ")
    
    if new_password != repeat_new_password:
        print("Password change failed. Password mismatch.")
        return
    
    with open("user.json", "r") as f:
        data = json.load(f)
    
    if hash_user(user) not in data:
        print("User does not exist.")
        return
    
    data[hash_user(user)]['p'] = hash_password(new_password)
    
    with open("user.json", "w") as f:
        json.dump(data, f)
    
    print("Password change successful.")

def forcepass(user):
    with open("user.json", "r") as f:
        data = json.load(f)
    
    if hash_user(user) not in data:
        print("User does not exist.")
        return
    
    data[hash_user(user)]['f'] = True
    
    with open("user.json", "w") as f:
        json.dump(data, f)
    
    print("User will be requested to change password on next login.")

def delete(user):
    with open("user.json", "r") as f:
        data = json.load(f)
    
    if hash_user(user) not in data:
        print("User does not exist.")
        return
    
    del data[hash_user(user)]
    
    with open("user.json", "w") as f:
        json.dump(data, f)
    
    print("User successfully removed.")
    
try:
        with open("user.json", "r") as f:
            data = json.load(f)
except FileNotFoundError:
    with open("user.json", "w") as f:
        data = {}
        json.dump(data, f)
    
        
action = sys.argv[1]
user = sys.argv[2]

if action == "add":
    add(user)
elif action == "passwd":
    passwd(user)
elif action == "forcepass":
    forcepass(user)
elif action == "del":
    delete(user)
