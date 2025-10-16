# backend/infer.py

import torch
from torchvision import transforms, models
from PIL import Image

LABELS = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

def load_model(checkpoint):
    """
    Load ResNet18 model from checkpoint.
    """
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = models.resnet18(pretrained=False, num_classes=10)
    checkpoint_data = torch.load(checkpoint, map_location=device)
    model.load_state_dict(checkpoint_data['model_state_dict'])
    model.to(device).eval()
    return model, device

def predict(model, device, img):
    """
    Predict class label for a given image.
    img: PIL Image object or image file path
    """
    transform = transforms.Compose([
        transforms.Resize((32,32)),
        transforms.ToTensor(),
        transforms.Normalize((0.4914,0.4822,0.4465),(0.2023,0.1994,0.2010))
    ])
    
    # Agar img string path ho toh open karo
    if not isinstance(img, Image.Image):
        img = Image.open(img).convert('RGB')
    
    img_tensor = transform(img).unsqueeze(0).to(device)
    
    model.eval()
    with torch.no_grad():
        out = model(img_tensor)
        _, pred = out.max(1)
    
    return LABELS[pred.item()]
