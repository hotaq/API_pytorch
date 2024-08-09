from flask import Flask, request, jsonify
import torch
import torchvision
from torchvision import transforms
from PIL import Image
import requests
from io import BytesIO
import torch.nn as nn
app = Flask(__name__)

class ResNet50(nn.Module):
    def __init__(self):
        super().__init__()
        self.transform = torchvision.models.ResNet50_Weights.IMAGENET1K_V2.transforms()
        self.resnet = torchvision.models.resnet50(weights=torchvision.models.ResNet50_Weights.IMAGENET1K_V2)
        self.resnet.fc = nn.Linear(in_features=2048, out_features=101)

    def forward(self, x):
        x = self.resnet(x)
        return x

# Load Keras Model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = ResNet50()
model.load_state_dict(torch.load('resnet50.pth', map_location=device))
model.to(device)
model.eval()  # Set model to evaluation mode

@app.route("/prediction", methods=['POST'])
def keras():
    apikey = request.args.get('apikey')
    image_url = request.args.get('url')

    if apikey == 'f69c02cc-5423-4285-9993-b42ecdec1c74':
        image_tensor = read_tensor_from_image_url(image_url)
        
        with torch.no_grad():  # Disable gradient calculation for inference
            prediction = model(image_tensor.to(device))  # Move tensor to device
            _, predicted_class = torch.max(prediction, 1)
        
        # Return the prediction and a 200 status
        return jsonify({'predicted_class': predicted_class.item()}), 200
    else:
        return "Not valid apikey", 400

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

if __name__ == "__main__":
    app.run(port=4000)  # Set host to 0.0.0.0 to listen on all interfaces
