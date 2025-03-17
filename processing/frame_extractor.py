import cv2

def extract_keyframes(video_path, interval=30):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    keyframes = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % interval == 0:
            keyframes.append(frame)
        frame_count += 1
    
    cap.release()
    return keyframes
