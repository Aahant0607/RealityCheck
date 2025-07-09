import cv2
import os
from image_detector import detect_fake_image

def detect_fake_video(video_path: str, frame_sample_rate=5) -> float:
    cap = cv2.VideoCapture(video_path)
    fake_scores = []
    idx = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if idx % frame_sample_rate == 0:
            frame_path = f"temp_frame_{idx}.jpg"
            cv2.imwrite(frame_path, frame)
            fake_prob = detect_fake_image(frame_path)
            fake_scores.append(fake_prob)
            os.remove(frame_path)
        idx += 1
    cap.release()
    
    if not fake_scores:
        return 0.0
    avg_fake_prob = sum(fake_scores) / len(fake_scores)
    return round(avg_fake_prob, 2)
