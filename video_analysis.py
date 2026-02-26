import cv2
import numpy as np

def normalize(values):
    if not values:
        return [0]
    min_val = min(values)
    max_val = max(values)
    return [(v - min_val) / (max_val - min_val + 1e-6) for v in values]


def extract_video_data(video_path):
    cap = cv2.VideoCapture(video_path)

    brightness_values = []
    motion_values = []
    timestamps = []

    prev_gray = None
    frame_count = 0
    fps = cap.get(cv2.CAP_PROP_FPS)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Timestamp (seconds)
        if fps > 0:
            timestamps.append(frame_count / fps)
        else:
            timestamps.append(frame_count)

        # Brightness
        brightness = np.mean(gray)
        brightness_values.append(brightness)

        # Motion
        if prev_gray is not None:
            diff = cv2.absdiff(prev_gray, gray)
            motion = np.mean(diff)
            motion_values.append(motion)
        else:
            motion_values.append(0)

        prev_gray = gray
        frame_count += 1

    cap.release()

    return {
        "brightness": normalize(brightness_values),
        "motion": normalize(motion_values),
        "timestamps": timestamps
    }