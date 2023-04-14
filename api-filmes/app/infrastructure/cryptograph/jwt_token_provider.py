import jwt
from decouple import config


class JWTTokenProvider():

    def __init__(self):
        self.secret = config('JWT_SECRET')

    def sign(self, payload: dict) -> str:
        token = jwt.encode(payload, self.secret, algorithm="HS256")
        return token

    def decode(self, token) -> dict:
        payload = jwt.decode(token, self.secret, algorithms=["HS256"])
        return payload
