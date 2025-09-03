import secrets

# Generate a 32-byte (256-bit) random key and print it in hexadecimal format
secret_key = secrets.token_hex(32)
print(secret_key)