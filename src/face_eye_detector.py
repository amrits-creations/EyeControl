import cv2
import mediapipe as mp

class FaceEyeDetector:
    """
    Uses MediaPipe Face Mesh to detect face and eye landmarks in images.
    """
    def __init__(self, static_mode=False, max_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=static_mode,
            max_num_faces=max_faces,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )
        self.mp_drawing = mp.solutions.drawing_utils
        self.drawing_spec = self.mp_drawing.DrawingSpec(thickness=1, circle_radius=1, color=(0,255,0))

        # Eye landmark indices for MediaPipe Face Mesh
        # (These are standard indices for left/right eyes)
        self.left_eye_indices = list(range(33, 42)) + list(range(133, 144))
        self.right_eye_indices = list(range(362, 371)) + list(range(263, 274))

    def detect(self, frame, draw_landmarks=False):
        """
        Detects face and eyes in a BGR frame.
        Returns a dict with 'face_landmarks', 'left_eye', 'right_eye',
        containing all 468 landmarks, left-eye points, and right-eye points respectively,
        in (x,y) pixel coordinate format.
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)
        output = {
            "face_landmarks": [],
            "left_eye": [],
            "right_eye": []
        }
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                h, w, _ = frame.shape
                # All face landmarks
                output["face_landmarks"] = [
                    (int(lm.x * w), int(lm.y * h)) for lm in face_landmarks.landmark
                ]
                # Left and right eye landmarks
                output["left_eye"] = [
                    (int(face_landmarks.landmark[i].x * w), int(face_landmarks.landmark[i].y * h))
                    for i in self.left_eye_indices
                ]
                output["right_eye"] = [
                    (int(face_landmarks.landmark[i].x * w), int(face_landmarks.landmark[i].y * h))
                    for i in self.right_eye_indices
                ]
                if draw_landmarks:
                    self.mp_drawing.draw_landmarks(
                        frame, face_landmarks,
                        self.mp_face_mesh.FACEMESH_CONTOURS,
                        self.drawing_spec, self.drawing_spec
                    )
        return output