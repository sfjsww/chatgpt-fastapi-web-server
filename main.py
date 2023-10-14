from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router import api_router

app = FastAPI()

app.include_router(
    api_router,
    prefix="/api",
    tags=["api"],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.on_event("startup")
async def startup_event():
    pass


if __name__ == '__main__':
    import asyncio

    loop = asyncio.get_event_loop()
    from uvicorn import Server, Config

    config = Config(app="main:app", host="0.0.0.0", port=8080)
    server = Server(config)
    loop.run_until_complete(server.serve())
