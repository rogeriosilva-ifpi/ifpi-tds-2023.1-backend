import bcrypt


class HashProvider():

    def hash(self, senha: str):
        senha_encoded = str.encode(senha)
        hashed = bcrypt.hashpw(senha_encoded, bcrypt.gensalt())
        return hashed

    def verify(self, senha: str, senha_hashed: str):
        senha_encoded = str.encode(senha)
        senha_hashed_encoded = str.encode(senha_hashed)

        return bcrypt.checkpw(senha_encoded, senha_hashed_encoded)
