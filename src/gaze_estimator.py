import numpy as np

class GazeEstimator:
    """
    Estimates gaze direction and normalized screen coordinates from eye landmarks.
    """
    def __init__(self):
        pass
    @staticmethod
    def estimate_gaze(left_eye, right_eye, frame_shape):
        """
        Given left/right eye landmarks and frame shape, estimate normalized gaze (x, y).
        Returns values between 0 and 1 for both axes.
        """
        if not left_eye or not right_eye:
            return None

        # Use the center of each eye as the reference point
        left_center = np.mean(left_eye, axis=0)
        right_center = np.mean(right_eye, axis=0)
        eyes_center = (left_center + right_center) / 2

        h, w = frame_shape[:2]
        norm_x = eyes_center[0] / w
        norm_y = eyes_center[1] / h

        return float(norm_x), float(norm_y)
