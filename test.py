from flask import Flask, request, jsonify
import torch
import torchvision
from torchvision import transforms
from PIL import Image
import requests
from io import BytesIO
import torch.nn as nn

app = Flask(__name__)

@app.route('/test')
def main():
    return 'if this succeed, fuck you bits'

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)
    