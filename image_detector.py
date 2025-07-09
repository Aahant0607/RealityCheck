from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch

processor = AutoImageProcessor.from_pretrained("mahendrapaipuri/fake-image-detector")
model = AutoModelForImageClassification.from_pretrained("mahendrapaipuri/fake-image-detector")

def detect_fake_image(image_path: str) -> float:
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)
    fake_prob = float(probs[0][1])
    return round(fake_prob * 100, 2)
