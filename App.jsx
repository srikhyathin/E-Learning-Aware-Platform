import { useEffect, useRef, useState } from "react";
import LessonPane from "./components/LessonPane";

export default function App() {
  const videoRef = useRef();
  const [engagement, setEngagement] = useState(null);

  useEffect(() => {
    async function start() {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });
      videoRef.current.srcObject = stream;

      const ws = new WebSocket("ws://localhost:8000/ws/engagement");

      const canvas = document.createElement("canvas");
      const ctx = canvas.getContext("2d");

      setInterval(() => {
        ctx.drawImage(videoRef.current, 0, 0, 320, 240);
        canvas.toBlob((blob) => {
          blob.arrayBuffer().then((buf) => ws.send(buf));
        }, "image/jpeg");
      }, 1500);

      ws.onmessage = (e) => setEngagement(JSON.parse(e.data));
    }

    start();
  }, []);

  return (
    <div className="p-6">
      <video ref={videoRef} autoPlay className="rounded-xl shadow mb-4" />
      <LessonPane engagement={engagement} />
    </div>
  );
}
