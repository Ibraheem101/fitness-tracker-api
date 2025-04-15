from passlib.context import CryptContext #type:ignore

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) ->str:
    return password_context.hash(password)
def verify_password(plaintext: str, ciphertext: str) -> bool:
    return password_context.verify(plaintext, ciphertext)