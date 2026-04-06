import bcrypt


class Account:
    def __init__(self, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    @staticmethod
    def hash_password(password: str, rounds=16) -> bytes:
        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=16))
        return password
