from typing import List
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class AsciiImage(BaseModel):

    name: str


@router.get("/images", tags=["images"], response_model=List[AsciiImage])
async def list_images():
    return [AsciiImage(name="first image")]


@router.get("/images/{image_id}", tags=["images"], response_model=AsciiImage)
async def get_image(image_id: str):
    return AsciiImage(name="first image")


# @router.post("/images", tags=["images"])
# async def create_image(image):
# return "image created"
