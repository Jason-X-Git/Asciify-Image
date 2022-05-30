from fastapi import FastAPI
from routers.images import router as images_router

app = FastAPI()

app.include_router(images_router)


@app.get("/status", tags=["Health"])
def status():
    return {"status": "ok"}
