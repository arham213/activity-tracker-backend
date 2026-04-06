from fastapi import APIRouter, UploadFile, File
from transformers import VisionEncoderDecoderModel, AutoImageProcessor, AutoTokenizer
import torch
from PIL import Image
from io import BytesIO
import asyncio
from functools import partial

router = APIRouter(prefix="/image-to-text", tags=["image-to-text"])

# Load once when server starts
model_name = "bipin/image-caption-generator"
model = VisionEncoderDecoderModel.from_pretrained(model_name)
feature_extractor = AutoImageProcessor.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained("gpt2")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


def generate_caption(img: Image.Image) -> str:
    """Run in thread to avoid blocking event loop"""
    if img.mode != "RGB":
        img = img.convert("RGB")
    pixel_values = feature_extractor(images=img, return_tensors="pt").pixel_values.to(device)
    output_ids = model.generate(pixel_values, num_beams=4, max_length=128)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)


@router.post('/with-file/')
async def imageToTextFromUpload(file: UploadFile = File(...)):
    contents = await file.read()
    img = Image.open(BytesIO(contents))
    loop = asyncio.get_event_loop()
    caption = await loop.run_in_executor(None, generate_caption, img)
    return {"caption": caption}