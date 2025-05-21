import sys
import time
from src.video_capture import VideoCapture

def test_single_frame():
    cap = VideoCapture()
    frame = cap.get_frame()
    print(f"[TEST] Single frame captured: {len(frame)} bytes")
    assert isinstance(frame, bytes) and len(frame) > 1000
    del cap

def test_streaming_frames(count=5, delay=0.2):
    cap = VideoCapture()
    gen = cap.frame_generator()
    for i in range(count):
        frame = next(gen, None)
        print(f"[TEST] Frame {i+1}: {len(frame) if frame else 0} bytes")
        assert frame is not None and len(frame) > 1000
        time.sleep(delay)
    del cap

if __name__ == "__main__":
    print("Running VideoCapture tests...")
    try:
        test_single_frame()
        test_streaming_frames()
    except AssertionError as e:
        print("Test failed:", e)
        sys.exit(1)
    except Exception as e:
        print("Error during tests:", e)
        sys.exit(1)
    print("All VideoCapture tests passed!")
