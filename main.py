from fastapi import FastAPI, File, UploadFile
import uuid
app = FastAPI()


import boto3
from fastapi.middleware.cors import CORSMiddleware
# from test import detect_labels

app = FastAPI()

origins= ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET'],
    allow_headers=['*']
)

#WRITE THE FUNCTION
def detect_labels(photo):

    client=boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
    
    data = {
        'source': photo,
        'data': response.get('Labels')
    }

    for key, value in data.items():
        print(key)

    return data

@app.get("/")
async def root():
    return {"message": "Hello World"}

image = 'bananas.jpg'

@app.post("/calc")
async def label(image: UploadFile = File(...)):
    print(image)
   
    return {"message": "ggggg"}
