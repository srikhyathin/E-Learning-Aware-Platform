from fastapi import FastAPI, UploadFile, WebSocket
import cv2
import numpy as np

from fer_model import predict_emotion
from engagement_engine import adapt_content

app = FastAPI()

@app.post("/analyze")
async def analyze(image: UploadFile):
    contents = await image.read()
    nparr = np.frombuffer(contents, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    emotion = predict_emotion(frame)
    decision = adapt_content(emotion)

    return decision

@app.websocket("/ws/engagement")
async def engagement_socket(ws: WebSocket):
    await ws.accept()
    while True:
        data = await ws.receive_bytes()
        frame = np.frombuffer(data, np.uint8)
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

        emotion = predict_emotion(frame)
        decision = adapt_content(emotion)

        await ws.send_json(decision.dict())
