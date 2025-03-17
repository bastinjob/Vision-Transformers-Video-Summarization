from processing.frame_extractor import extract_keyframes
from models.vision_transformer import classify_frame
from models.gpt_summarizer import generate_summary
from PIL import Image

video_path = "data/sample_videos/example.mp4"
keyframes = extract_keyframes(video_path)

scene_descriptions = []
for frame in keyframes:
    image = Image.fromarray(frame)
    scene_label = classify_frame(image)
    scene_descriptions.append(f"Scene {scene_label}")

summary = generate_summary(" ".join(scene_descriptions))
print("Video Summary:", summary)
