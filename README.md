# DL ResNet Image Recognition Project

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)]()
[![Flask](https://img.shields.io/badge/Flask-2.3.4-lightgrey?logo=flask&logoColor=black)]()
[![PyTorch](https://img.shields.io/badge/PyTorch-2.1-red?logo=pytorch&logoColor=white)]()
[![TorchVision](https://img.shields.io/badge/TorchVision-0.16.1-orange?logo=pytorch&logoColor=white)]()
[![Pillow](https://img.shields.io/badge/Pillow-10.0-lightblue?logo=pillow&logoColor=white)]()
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)]()
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)]()
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)]()
[![ResNet](https://img.shields.io/badge/ResNet-DeepLearning-purple?logo=neural-network)]()

---

## **Project Overview**
This project is a **real-time deep learning image classification system** built using **ResNet18** (PyTorch) and served via **Flask**.  
It can classify images into **CIFAR-10 categories** and shows **10 detailed points** about each predicted class on a **modern, gradient-based UI**.

**Key Highlights:**
- Real-time image classification using a pre-trained ResNet18 model.
- Upload and preview images directly in the browser.
- Modular and extensible architecture for adding new models or classes.
- Modern, responsive, and visually appealing interface.

---

## **Technologies Used**
- **Python 3.11**  
- **Flask** (Web framework for serving the model)  
- **PyTorch & TorchVision** (Deep learning and ResNet18 model)  
- **Pillow** (Image preprocessing)  
- **HTML5, CSS3, JavaScript** (Frontend UI)  
- Deep learning & computer vision techniques  

---

## **Quickstart / Installation & Run**

### **1. Clone the repository**
```bash
git clone https://github.com/atharva18-hue/DL-ResNet-Image-Recognition-Project.git
cd DL-ResNet-Image-Recognition-Project
2. Create virtual environment
bash
Copy code
python -m venv venv
3. Activate virtual environment
bash
Copy code
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
4. Install dependencies
bash
Copy code
pip install -r requirements.txt
5. Download dataset & trained model
Place cifar-10-python.tar.gz in data/

Place checkpoint.pth in backend/

6. Run the Flask app
bash
Copy code
python app.py
7. Open in browser
cpp
Copy code
http://127.0.0.1:5000
Usage
Click Choose File to upload an image.

Preview the image immediately.

See predicted class & 10 detailed points about that class.

Click Try Another to test a new image.

Folder Structure
graphql
Copy code
DL-ResNet-Image-Recognition-Project/
│
├── backend/
│   ├── infer.py          # Image prediction logic
│   ├── train.py          # Model training script
│   └── checkpoint.pth    # Pre-trained ResNet model (excluded)
│
├── data/
│   └── cifar-10-python.tar.gz  # CIFAR-10 dataset (excluded)
│
├── frontend/
│   ├── index.html        # Web UI
│   ├── style.css         # CSS styling
│   └── script.js         # JS for image upload & prediction
│
├── requirements.txt      # Python dependencies
└── app.py                # Flask app entry point
Features (Detailed)
Feature	Description
Real-time Prediction	The system uses a pre-trained ResNet18 model to classify uploaded images instantly.
Interactive UI	Users can upload images directly from the browser and immediately preview them before prediction.
Detailed Class Info	For each predicted class, the app displays 10 key points including features, uses, and examples.
Responsive Design	Works smoothly across desktop, tablet, and mobile screens with adaptive layout.
Gradient UI	Modern, visually appealing gradient-based interface for better user experience.
Extensible Architecture	The modular design allows adding new models, datasets, or classes without changing core logic.
Fast Feedback Loop	Users can try multiple images quickly and see predictions in real-time.
Preprocessing Pipeline	Images are automatically resized and normalized for the ResNet model, ensuring accuracy.
Error Handling	Provides user-friendly feedback if the uploaded file is invalid or unsupported.
Educational Tool	Displays detailed points making it a great tool to understand characteristics of CIFAR-10 classes.

Future Work
Add support for all CIFAR-10 classes.

Deploy on Heroku / AWS for public access.

Implement drag-and-drop image upload.

Show prediction confidence scores alongside classes.

Option to compare multiple images side by side.

Author
Atharva Chavhan
Email: atharvachavhan18@gmail.com
GitHub: https://github.com/atharva18-hue
Contact: +91 8767242559
