import numpy as np
from tensorflow import keras
import io
from PIL import Image
from fastapi import FastAPI, File, UploadFile
app = FastAPI()
model = keras.models.load_model("./app/dog_cat_model.h5")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    file_content = None
    try:
        file_content = file.file.read()
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    image = Image.open(io.BytesIO(file_content)).resize((100,100))
    pix_arr = np.array(image)
    pred = model.predict(pix_arr.reshape(1,100,100,3))[0,0]
    # acc = pred
    pred = "dog" if pred < 0.5 else "cat"
    return {
        "prediction": f"{pred}",
        #"accuracy" : f'{acc}'
        }

