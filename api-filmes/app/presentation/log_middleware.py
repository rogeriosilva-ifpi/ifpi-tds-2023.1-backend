import time

from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware


class LogMiddleware(BaseHTTPMiddleware):

    def __init__(self, app: FastAPI):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):

        start = time.time()

        response = await call_next(request)

        total = (time.time() - start) * 1000

        response.headers['X-Process-Time'] = f'{total}ms'

        print(f'Log... time: {total:.0f}ms')

        return response
