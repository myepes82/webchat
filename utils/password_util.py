import bcrypt

DEFAULT_SALT_PASSWORD = 12

def encrypt_password(*, password: str = None) -> str: 
    password_salts = bcrypt.gensalt(rounds=DEFAULT_SALT_PASSWORD)
    return bcrypt.hashpw(password=password, salt=password_salts)


def compare_passwords(*, password: str = None, hashed_password: str = None) -> bool:
    return bcrypt.checkpw(password=password, hashed_password=hashed_password)
