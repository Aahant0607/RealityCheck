import torchaudio
import torch

def load_audio(file_path):
    waveform, sample_rate = torchaudio.load(file_path)
    return waveform, sample_rate

def detect_fake_audio(file_path: str) -> float:
    waveform, sample_rate = load_audio(file_path)
    energy = waveform.abs().mean().item()
    fake_score = min(max((energy - 0.01) * 10000, 0), 100)
    return round(fake_score, 2)
