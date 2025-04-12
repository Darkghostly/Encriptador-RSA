from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Gerando chaves RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Função para criptografar
def encrypt_rsa(message, public_key):
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

# Função para descriptografar
def decrypt_rsa(encrypted_message, private_key):
    decrypted = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode()

# Exemplo de uso
mensagem = "Mensagem secreta"
criptografado = encrypt_rsa(mensagem, public_key)
print("Texto Criptografado (RSA):", criptografado.hex())

descriptografado = decrypt_rsa(criptografado, private_key)
print("Texto Descriptografado (RSA):", descriptografado)
