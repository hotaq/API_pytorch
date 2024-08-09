from flask import Flask, request, jsonify
import torch
import torchvision
from torchvision import transforms
from PIL import Image
import requests
from io import BytesIO
import torch.nn as nn
from pyngrok import ngrok

app = Flask(__name__)
ngrok.set_auth_token("2QKsbEXhnGc0P8WnoUgvlyZV74c_7PXhA6Z6wdaSYBHMicDYw")
public_url = ngrok.connect(5000).public_url
@app.route('/')
def home():
  return 'this is home'

print(public_url)
app.run(port=5000)