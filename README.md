# Vision-Transformers-Video-Summarization


##  Project Overview
The **Video Content Summary Generator** is an AI-powered pipeline that extracts meaningful information from videos and generates concise summaries. It combines **OpenCV** for video processing, **Vision Transformers (ViT)** for scene understanding, and **GPT models** for text-based summarization.

### 🔹 Key Features
- **Keyframe Extraction**: Identifies important frames using OpenCV.
- **Scene Understanding**: Uses Vision Transformers to classify and describe scenes.
- **Text Summarization**: Converts extracted descriptions into a human-readable summary using GPT.
- **Scalability**: Can be extended to work with multiple video formats and optimized for real-time processing.

---
##  Methodology
This project follows a structured pipeline:

### 1️⃣ **Frame Extraction** (OpenCV)
- Loads a video file and extracts frames at scene changes or set intervals.
- Filters redundant frames to reduce computational load.

### 2️⃣ **Scene Classification** (Vision Transformers)
- Converts keyframes into image embeddings.
- Uses a pre-trained **ViT model** to classify frames into semantic categories.

### 3️⃣ **Summarization** (GPT-based NLP Model)
- Takes scene descriptions as input.
- Generates a natural language summary using GPT models (e.g., `facebook/bart-large-cnn`).

---
##  System Architecture
```
+-------------------+
|  Video Input     |
+-------------------+
        |
        v
+-------------------+
|  OpenCV          |  <-- Frame Extraction
+-------------------+
        |
        v
+-------------------+
|  Vision Transformer |  <-- Scene Understanding
+-------------------+
        |
        v
+-------------------+
|  GPT Summarizer    |  <-- Text Summary Generation
+-------------------+
        |
        v
+-------------------+
|  Summary Output    |
+-------------------+
```

---
##  Getting Started

### 🔧 Prerequisites
Ensure you have Python installed. Recommended version: **Python 3.8+**.

Install dependencies:
```bash
pip install -r requirements.txt


---
## Usage Guide

### 🔹 Extract Keyframes from Video
```python
from processing.frame_extractor import extract_keyframes
video_path = "data/sample_videos/example.mp4"
keyframes = extract_keyframes(video_path)
```

### 🔹 Classify Scenes using Vision Transformer
```python
from models.vision_transformer import classify_frame
from PIL import Image
image = Image.fromarray(keyframes[0])
scene_label = classify_frame(image)
print("Scene Classification:", scene_label)
```

### 🔹 Generate Summary using GPT
```python
from models.gpt_summarizer import generate_summary
scene_descriptions = ["Scene 1: A busy street", "Scene 2: A quiet park"]
summary = generate_summary(" ".join(scene_descriptions))
print("Video Summary:", summary)
```

### 🔹 Run Full Pipeline
```bash
python run_pipeline.py
```

---
## Future Enhancements
- **Real-time Processing**: Implement live video summarization.
- **Fine-tuned GPT Model**: Use domain-specific training for better summaries.
- **Multi-Modal Summarization**: Incorporate audio and subtitles for richer insights.
- **Cloud Deployment**: Deploy as an API service for remote processing.

---
## Contributing
Feel free to fork this repository and contribute!
1. Clone the repo: `git clone https://github.com/bastinjob/video-summary-generator.git`
2. Create a new branch: `git checkout -b feature-branch`
3. Commit changes: `git commit -m "Add new feature"`
4. Push branch: `git push origin feature-branch`
5. Create a Pull Request

---


