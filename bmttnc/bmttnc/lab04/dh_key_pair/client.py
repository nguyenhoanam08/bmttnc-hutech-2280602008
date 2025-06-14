from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC  # (chưa dùng)
from cryptography.hazmat.primitives import hashes  # (chưa dùng)

# Tạo cặp khóa phía client
def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

# Tính khóa chung giữa client và server
def derive_shared_secret(private_key, server_public_key):
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    # Tải khóa công khai của server từ file
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())

    # Lấy tham số DH từ khóa công khai của server
    parameters = server_public_key.parameters()

    # Sinh cặp khóa client
    private_key, public_key = generate_client_key_pair(parameters)

    # Tính khóa bí mật chung
    shared_secret = derive_shared_secret(private_key, server_public_key)

    print("Shared Secret:", shared_secret.hex())

if __name__ == "__main__":
    main()
