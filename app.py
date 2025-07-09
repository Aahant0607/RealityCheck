import streamlit as st
from text_detector import detect_ai_text
from image_detector import detect_fake_image
from audio_detector import detect_fake_audio
from video_detector import detect_fake_video
from PIL import Image
import tempfile

st.title("🛡️ RealityCheck - AI Content & Deepfake Detector MVP")

media_type = st.sidebar.selectbox("Select Content Type", ["Text", "Image", "Audio", "Video"])

if media_type == "Text":
    st.subheader("📝 Text AI Detection")
    text_input = st.text_area("Paste text here")
    if st.button("Detect AI Text"):
        if not text_input.strip():
            st.warning("Please enter text")
        else:
            prob = detect_ai_text(text_input)
            st.success(f"AI-Generated Probability: {prob}%")
            st.markdown("**Likely AI**" if prob > 50 else "**Likely Human**")

elif media_type == "Image":
    st.subheader("🖼️ Image Deepfake Detection")
    uploaded_file = st.file_uploader("Upload Image", type=["png","jpg","jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        if st.button("Detect Fake Image"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                tmp.write(uploaded_file.getbuffer())
                tmp_path = tmp.name
            prob = detect_fake_image(tmp_path)
            st.success(f"Fake Image Probability: {prob}%")
            st.markdown("**Likely Fake**" if prob > 50 else "**Likely Real**")

elif media_type == "Audio":
    st.subheader("🔊 Audio Deepfake Detection")
    uploaded_file = st.file_uploader("Upload Audio", type=["wav","mp3","flac"])
    if uploaded_file:
        if st.button("Detect Fake Audio"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(uploaded_file.getbuffer())
                tmp_path = tmp.name
            prob = detect_fake_audio(tmp_path)
            st.success(f"Fake Audio Probability: {prob}%")
            st.markdown("**Likely Fake**" if prob > 50 else "**Likely Real**")

elif media_type == "Video":
    st.subheader("🎥 Video Deepfake Detection")
    uploaded_file = st.file_uploader("Upload Video", type=["mp4","mov","avi"])
    if uploaded_file:
        if st.button("Detect Fake Video"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
                tmp.write(uploaded_file.getbuffer())
                tmp_path = tmp.name
            prob = detect_fake_video(tmp_path)
            st.success(f"Fake Video Probability: {prob}%")
            st.markdown("**Likely Fake**" if prob > 50 else "**Likely Real**")
