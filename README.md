
---

# 🛡️ RealityCheck

**Multi-Modal AI Content & Deepfake Detection MVP**

[![Streamlit App](https://img.shields.io/badge/Live%20App-Click%20Here-brightgreen)](https://realitycheck-kzofedkmztvdbpp9ehdmxb.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> RealityCheck is a unified AI-based platform that detects synthetic or manipulated content across **text**, **images**, **audio**, and **video** using state-of-the-art machine learning models.

---

## 📌 Overview

As generative AI content becomes more prevalent, distinguishing between real and AI-generated media is increasingly critical. **RealityCheck** addresses this by offering a **modular, multi-modal deepfake detection system** for:

* 📝 **Text** – Detection of AI-generated writing
* 🖼️ **Images** – Classification of deepfake and synthetic visuals
* 🔊 **Audio** – Detection of voice cloning or audio synthesis
* 🎥 **Video** – Frame-wise analysis to identify deepfake manipulations

Accessible via an intuitive **Streamlit** interface, RealityCheck is designed as a proof of concept (MVP) for fact-checking tools, journalists, forensics experts, and the general public.

---

## 🔗 Try It Live

👉 **[Launch the App](https://realitycheck-kzofedkmztvdbpp9ehdmxb.streamlit.app/)**
No installation required — works directly in your browser.

---

## 🧠 Model Architecture

| Modality  | Methodology                                                                             |
| --------- | --------------------------------------------------------------------------------------- |
| **Text**  | Fine-tuned `roberta-base-openai-detector` model for binary classification (AI vs Human) |
| **Image** | `SigLIP` model via Hugging Face (`open-deepfake-detection`)                             |
| **Audio** | Heuristic energy-based analysis using `torchaudio`                                      |
| **Video** | Frame sampling + image-level fake detection using the same vision pipeline              |

---

## 🧪 Features

✅ Real-time predictions
✅ Lightweight and fast model inferences
✅ Dynamic upload interface per modality
✅ Visual confidence feedback with result labeling
✅ Deployed and shareable via Streamlit Cloud

---

## 🛠️ Tech Stack

**Frontend:**

* [Streamlit](https://streamlit.io) for UI/UX
* [Pillow](https://python-pillow.org) for image handling

**ML/Inference:**

* [Transformers](https://huggingface.co/transformers/) by Hugging Face
* [PyTorch](https://pytorch.org) & [torchaudio](https://pytorch.org/audio/)
* [OpenCV](https://opencv.org) for video frame extraction
* [librosa](https://librosa.org) for audio analysis

**Video & Media:**

* `moviepy`, `ffmpeg-python` for video handling
* `opencv-python-headless` for server-safe image/video operations

---

## ⚙️ Installation (Local Setup)

```bash
# Clone the repo
git clone https://github.com/yourusername/realitycheck.git
cd realitycheck

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📁 Project Structure

```
realitycheck/
├── app.py                       # Streamlit UI
├── text_detector.py            # Text analysis logic
├── image_detector.py           # Image classification model
├── audio_detector.py           # Audio feature analysis
├── video_detector.py           # Frame sampling and video analysis
├── requirements.txt
└── README.md

```

## 🚀 Future Improvements

* Replace heuristic audio model with deep learning-based speech detection
* Expand video analysis to support live stream and real-time feeds
* Add explanation features (e.g., Grad-CAM for images, attention maps for text)
* Build API endpoints for integration with third-party tools

---

Certainly! Here's a **professional and concise "🤝 Collaboration"** section you can include in your README:

---

## 🤝 Collaboration

We welcome contributions from researchers, developers, and domain experts passionate about AI safety and media integrity. Whether it's improving model performance, enhancing UI/UX, or integrating new detection techniques — your expertise can help evolve RealityCheck into a powerful open-source tool.

Feel free to fork the repo, open issues, or submit pull requests!

---

## 📄 License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for more details.

---
