from transformers import AutoImageProcessor, SiglipForImageClassification
from PIL import Image
import torch

# Use a free, publicly available deepfake detection model
MODEL_NAME = "prithivMLmods/open-deepfake-detection"

processor = AutoImageProcessor.from_pretrained(MODEL_NAME)
model = SiglipForImageClassification.from_pretrained(MODEL_NAME)

# Label mapping (optional, but useful)
ID2LABEL = {"0": "Fake", "1": "Real"}

def detect_fake_image(image_path: str) -> float:
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1).squeeze().tolist()
    fake_prob = probs[0]  # Probability that it is "Fake"
    return round(fake_prob * 100, 2)
