import cv2
import numpy as np
from src.video_capture import VideoCapture
from src.face_eye_detector import FaceEyeDetector
from src.gaze_estimator import GazeEstimator

def main():
    cap = VideoCapture()
    detector = FaceEyeDetector()
    estimator = GazeEstimator()
    cv2.namedWindow("Gaze Estimation", cv2.WINDOW_NORMAL)

    try:
        while True:
            frame_bytes = cap.get_frame()
            np_arr = np.frombuffer(frame_bytes, np.uint8)
            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            result = detector.detect(frame, draw_landmarks=True)
            gaze = estimator.estimate_gaze(result["left_eye"], result["right_eye"], frame.shape)

            # Show gaze coordinates on the frame
            if gaze:
                x, y = gaze
                text = f"Gaze: x={x:.2f}, y={y:.2f}"
                cv2.putText(frame, text, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

            cv2.imshow("Gaze Estimation", frame)
            if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
                break
    finally:
        cv2.destroyAllWindows()
        del cap

if __name__ == "__main__":
    main()
