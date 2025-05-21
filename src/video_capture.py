import cv2
from typing import Generator

class VideoCapture:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)
        if not self.cap.isOpened():
            raise RuntimeError("Could not open webcam")

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

    def get_frame(self) -> bytes:
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Failed to capture frame")
        # Encode frame as JPEG
        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            raise RuntimeError("Failed to encode frame")
        return jpeg.tobytes()

    def frame_generator(self) -> Generator[bytes, None, None]:
        while True:
            try:
                frame = self.get_frame()
                yield frame
            except RuntimeError:
                break