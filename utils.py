from functools import lru_cache
import io
from typing import List, Optional
from pathlib import Path
from uuid import uuid1

from PIL.PngImagePlugin import PngImageFile
from fastapi import UploadFile, HTTPException, status

ASCII_TEXT_FOLDER = Path("__file__").parent / "asciify_texts"


from PIL import Image


# Refactor pywhatkit method "image_to_ascii_art" to read UploadFile from fastapi
async def image_to_ascii_art(png: UploadFile, output_file: str) -> str:
    """Convert an Image to ASCII Art"""
    request_object_content = await png.read()
    with Image.open(io.BytesIO(request_object_content)) as img:

        img: PngImageFile = img.convert("L")

        width, height = img.size
        aspect_ratio = height / width
        new_width = 80
        new_height = aspect_ratio * new_width * 0.55
        img = img.resize((new_width, int(new_height)))

        pixels = img.getdata()

        chars = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
        new_pixels = [chars[pixel // 25] for pixel in pixels]
        new_pixels = "".join(new_pixels)

        new_pixels_count = len(new_pixels)
        ascii_image = [
            new_pixels[index : index + new_width]
            for index in range(0, new_pixels_count, new_width)
        ]
        ascii_image = "\n".join(ascii_image)

        with open(f"{output_file}.txt", "w") as f:
            f.write(ascii_image)
        return ascii_image


async def asciify_png(uploaded_png):
    """Convert png into ascii art, and saved it as text file"""
    image_id = uuid1().hex
    ascii_txt_path = ASCII_TEXT_FOLDER / image_id
    await image_to_ascii_art(uploaded_png, ascii_txt_path)
    return image_id


@lru_cache(maxsize=None)
def get_ascii_image(image_id: str):
    """Read ascii text file, and return ascii art content"""
    image_ascii_file = ASCII_TEXT_FOLDER / f"{image_id}.txt"
    if image_ascii_file.exists():
        with open(image_ascii_file, "r") as f:
            return f.read()
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid image id: {image_id}",
        )


async def list_ascii_images(limit: Optional[int] = None) -> List[str]:
    image_ascii_files = ASCII_TEXT_FOLDER.glob("*.txt")
    results = []
    for image_file in image_ascii_files:
        results.append(image_file.name[0:-4])
        if limit and len(results) == limit:
            break
    return results
