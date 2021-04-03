import uvicorn
from fastapi import FastAPI, File, UploadFile
from starlette.responses import RedirectResponse
import shutil
from PIL import Image
from io import BytesIO
app = FastAPI()

def predict():
    return "helllllo"

@app.get("/", include_in_schema=False)
async def index():
    return 'hello'

def read_imagefile(image):
    image = Image.open(image)
    return image


@app.post("/predict/image")
async def predict_api(image: UploadFile = File(...)):
    extension = image.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    with open("destination.png", "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    width, height = Image.open('destination.png').size
    return width*height


if __name__ == "__main__":
    uvicorn.run(app, debug=True)