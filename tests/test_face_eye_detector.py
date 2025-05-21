import cv2
from src.video_capture import VideoCapture
from src.face_eye_detector import FaceEyeDetector

def main():
    cap = VideoCapture()
    detector = FaceEyeDetector()
    cv2.namedWindow("Face & Eye Detection", cv2.WINDOW_NORMAL)

    try:
        while True:
            frame_bytes = cap.get_frame()
            np_arr = np.frombuffer(frame_bytes, np.uint8)
            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            result = detector.detect(frame, draw_landmarks=True)

            # Draw left and right eye landmarks in red and blue
            for (x, y) in result["left_eye"]:
                cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)
            for (x, y) in result["right_eye"]:
                cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)

            cv2.imshow("Face & Eye Detection", frame)
            if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
                break
    finally:
        cv2.destroyAllWindows()
        del cap

if __name__ == "__main__":
    import numpy as np
    main()