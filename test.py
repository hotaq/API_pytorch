from flask import Flask, request, jsonify
import torch
from torchvision import transforms
from PIL import Image
import requests
from io import BytesIO
import torch
import torchvision
import os
import torchvision.transforms as transforms
import torch.nn as nn 
# Import Flask API
from flask import Flask, request
import numpy as np
url = "https://res.cloudinary.com/dsui0fihb/image/upload/v1723184588/shoes.jpg"
def read_tensor_from_image_url(url,
                               input_height=224,
                               input_width=224,
                               input_mean=0,
                               input_std=255):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content)).convert('RGB')
    
    transform = transforms.Compose([
        transforms.Resize((input_height, input_width)),
        transforms.ToTensor(),
    ])
    
    tensor = transform(image).unsqueeze(0)
    return tensor
tensor = read_tensor_from_image_url(url)
print(tensor)