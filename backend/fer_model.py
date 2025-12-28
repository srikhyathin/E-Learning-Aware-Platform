import cv2
import numpy as np

EMOTIONS = ["happy", "bored", "confused", "inactive"]

def predict_emotion(frame: np.ndarray) -> str:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # TODO: load your CNN + proper preprocessing
    # Dummy rule:
    avg = gray.mean()
    if avg > 160:
        return "happy"
    if avg > 120:
        return "bored"
    if avg > 80:
        return "confused"
    return "inactive"
