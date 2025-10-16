# CIFAR-10 ResNet Image Recognition Project

This project is a full-stack deep learning project using **ResNet-18** trained on **CIFAR-10**. 
It includes a proper **HTML/CSS/JS frontend** with a Flask backend API.

## Folder structure

- backend/ : Training and inference scripts + model checkpoint placeholder
- frontend/ : HTML/CSS/JS files for web interface
- app.py : Flask backend to serve frontend and API
- requirements.txt : Python dependencies
- README.md : This file

## Run the project

1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run backend server:
```bash
python app.py
```
3. Open browser at `http://127.0.0.1:5000`
4. Upload image and click Predict

**Note:** Replace `backend/checkpoint.pth` with trained ResNet18 weights for real predictions.
