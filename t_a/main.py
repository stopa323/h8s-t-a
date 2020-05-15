import uvicorn

from fastapi import FastAPI

from t_a.client import TerraformClient


TF_DIR = "../tests/terraform_cfgs"
app = FastAPI()


@app.on_event("startup")
async def startup():
    client = TerraformClient(TF_DIR)
    # client.init()
    client.plan()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
