import uvicorn
from fastapi import FastAPI, File, UploadFile
from starlette.responses import RedirectResponse
import shutil
from PIL import Image
from io import BytesIO
import numpy as np
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
    with open("api/destination.png", "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
        width, height = Image.open('api/destination.png').size
        RGBim = Image.open('api/destination.png').convert('RGB')
        HSVim = RGBim.convert('HSV')
        RGBna = np.array(RGBim)
        HSVna = np.array(HSVim)
        H = HSVna[:,:,0]
        lo,hi = 100,140
        lo = int((lo * 255) / 360)
        hi = int((hi * 255) / 360)
        
        green = np.where((H>lo) & (H<hi))

        count = green[0].size
        risk = (count*100)/(width*height)
        print("Pixels matched: {}".format(count))
    return {'risk': risk}


if __name__ == "__main__":
    uvicorn.run(app, debug=True)