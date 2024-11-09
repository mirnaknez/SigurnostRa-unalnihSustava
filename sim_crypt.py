import sys
import json
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import HMAC, SHA256

def init(master_password):
    salt = get_random_bytes(16)
    key = scrypt(master_password, salt, 32, N=16384, r=8, p=1)
    iv, encrypted_flag = encrypt_data(key, "initialized")
    hmac = generate_hmac(key, encrypted_flag)
    data = {
        "salt": salt.hex(),
        "init_iv": iv.hex(),
        "init_data": encrypted_flag.hex(),
        "init_hmac": hmac.hex(),
        "passwords": {}
    }
    with open("passwords.json", "w") as f:
        json.dump(data, f)
    print("Password manager initialized")

def encrypt_data(key, data):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    return cipher.iv, ct_bytes

def decrypt_data(key, iv, ct):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size).decode()
    return pt

def generate_hmac(key, data):
    return HMAC.new(key, data, SHA256).digest()

def verify_master_password(key, data):
    try:
        iv = bytes.fromhex(data['init_iv'])
        encrypted_flag = bytes.fromhex(data['init_data'])
        hmac_stored = bytes.fromhex(data['init_hmac'])
        if not verify_hmac(key, encrypted_flag, hmac_stored):
            return False
        decrypted_flag = decrypt_data(key, iv, encrypted_flag)
        return decrypted_flag == "initialized"
    except (ValueError, KeyError):
        return False

def verify_hmac(key, data, hmac_to_verify):
    hmac = HMAC.new(key, data, SHA256)
    try:
        hmac.verify(hmac_to_verify)
        return True
    except ValueError:
        return False

def put(master_password, address, password):
    with open("passwords.json", "r") as f:
        data = json.load(f)
    salt = bytes.fromhex(data['salt'])
    key = scrypt(master_password, salt, 32, N=16384, r=8, p=1)
    if not verify_master_password(key, data):
        print("Master password incorrect or integrity check failed")
        return

    address_hash = SHA256.new(address.encode()).hexdigest()

    address_iv, address_ct_bytes = encrypt_data(key, address)
    password_iv, password_ct_bytes = encrypt_data(key, password)

    address_hmac = generate_hmac(key, address_ct_bytes)
    password_hmac = generate_hmac(key, password_ct_bytes)

    data['passwords'][address_hash] = {
        "address_iv": address_iv.hex(),
        "address_ct": address_ct_bytes.hex(),
        "address_hmac": address_hmac.hex(),
        "password_iv": password_iv.hex(),
        "password_ct": password_ct_bytes.hex(),
        "password_hmac": password_hmac.hex()
    }

    with open("passwords.json", "w") as f:
        json.dump(data, f)

    print(f"Stored password for {address}")


def get(master_password, address):
    with open("passwords.json", "r") as f:
        data = json.load(f)
    salt = bytes.fromhex(data['salt'])
    key = scrypt(master_password, salt, 32, N=16384, r=8, p=1)

    if not verify_master_password(key, data):
        print("Master password incorrect or integrity check failed")
        return

    address_hash = SHA256.new(address.encode()).hexdigest()

    if address_hash in data['passwords']:
        entry = data['passwords'][address_hash]
        password_iv = bytes.fromhex(entry['password_iv'])
        password_ct = bytes.fromhex(entry['password_ct'])
        password_hmac_stored = bytes.fromhex(entry['password_hmac'])

        if verify_hmac(key, password_ct, password_hmac_stored):
            decrypted_password = decrypt_data(key, password_iv, password_ct)
            print(f"Password for {address} is: {decrypted_password}")
    else:
        print("Password does not exist for the given address")



action = sys.argv[1]
master_password = sys.argv[2]
if action == "init":
    init(master_password)
elif action == "put":
    address = sys.argv[3]
    password = sys.argv[4]
    put(master_password, address, password)
elif action == "get":
    address = sys.argv[3]
    get(master_password, address)
