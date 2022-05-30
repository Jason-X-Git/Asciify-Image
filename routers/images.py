import os
from typing import List
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import PlainTextResponse
from utils import asciify_png, get_ascii_image, list_ascii_images

router = APIRouter()


@router.get("/images", tags=["images"], summary="List saved ascii image ids")
async def list_images(limit: int = None):
    image_ids = await list_ascii_images(limit=limit)
    return {"images": image_ids}


@router.get(
    "/images/{image_id}",
    summary="Get ascii image by its id",
    tags=["images"],
    response_class=PlainTextResponse,
)
async def get_image(image_id: str):
    ascii_txt = get_ascii_image(image_id)
    return ascii_txt


@router.post("/images", tags=["images"], status_code=201)
async def create_ascii_art(png: UploadFile = File(...)):
    print(type(png))
    image_id = await asciify_png(png)
    return {"image id": image_id}
