from fastapi import FastAPI, File, UploadFile, Body, Form
import boto3
from requests_toolbelt.multipart import decoder
import sys
import io
from typing import List

import json
import cv2

app = FastAPI()


from fastapi.middleware.cors import CORSMiddleware
# from test import detect_labels

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

def detect_labels(base):

    client=boto3.client('rekognition')

  
    response = client.detect_labels(Image={'Bytes': base})
    
    data = {
        'data': response.get('Labels')
    }

    return data

@app.get("/")
async def root():
    return {"message": "Hello World"}

image = 'bananas.jpg'

@app.post("/calc/")
async def label(data: str):
    res = await detect_labels(data)
    # await detect_labels(data)
    print(res)
    return {"message": res}

@app.post("/test")
# image: bytes = File(...)
async def upload_image(image: bytes = File(...)):
    # print(type(image))
    # d = image.decode()
    # p = d.encode(utf8)
    # print(dir(d))
    # print(type(p))
    # print(dir(image.decode))
    # print(image.format_map)
    data = detect_labels(image)
    # print(res)
    num_of_bananas = len(data["data"][0]["Instances"])
    price_of_bananas = 4.0

    print("Total price for", num_of_bananas, "bananas:", price_of_bananas * num_of_bananas)
    dict = {'bananas': num_of_bananas, 'price': price_of_bananas * num_of_bananas}
    return {"filename": 'hhh'}
