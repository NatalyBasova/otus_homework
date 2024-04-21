from typing import Union

import uvicorn

from fastapi import FastAPI


app = FastAPI()


@app.head("/")
@app.get("/")
def read_root():
    return {"message": "ok"}


@app.get("/ping/")
def pong():
    return {"ping": "pong!"}


def main():
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
