import uvicorn

from fastapi import FastAPI


app = FastAPI()


@app.on_event("startup")
async def startup():
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
