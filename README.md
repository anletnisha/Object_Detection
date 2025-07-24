# 🚘 Vehicle Detection and Tracking using YOLOv8

This project applies **YOLOv8** (from Ultralytics) for **real-time object detection and tracking** of vehicles in video footage. The Python script reads an input traffic video, detects cars and other objects frame-by-frame, and outputs an annotated video showing tracked objects with bounding boxes.

---

## 🧠 What It Does

- Loads a pretrained **YOLOv8n** model (`yolov8n.pt`)
- Processes an input video (e.g., road traffic)
- Detects and tracks vehicles (cars, buses, etc.)
- Displays the detection in real time
- Saves an annotated output video with bounding boxes

---

## 🗂️ Files

| File | Description |
|------|-------------|
| `car_detection.py` | Main Python script for detection & tracking |
| `driving.mp4` | Input video (user-provided) |
| `tracked_output.avi` | Output video with detection boxes |
| `README.md` | Project description |
| `requirements.txt` | (Optional) List of Python dependencies |

---

## 🛠️ How to Run

### 1. Clone the Repo (or download the script)
```bash
git clone https://github.com/anletnisha/Object_detection.git
cd vehicle-detection-yolov8
2. Install Required Packages
bash
Copy
Edit
pip install ultralytics opencv-python lap
Note: lap is required for object tracking to work.

3. Run the Detection Script
bash
Copy
Edit
python car_detection.py
Press q to quit the live video window.

📦 Requirements
Python 3.8+

OpenCV (opencv-python)

Ultralytics YOLOv8 (ultralytics)

LAP solver (lap)

📌 Output
Annotated video with tracked vehicles: tracked_output.avi

Real-time display of detection window

🙏 Acknowledgments
This project builds on the Ultralytics YOLOv8 framework.

Parts of the script are adapted from open-source examples by the ML community. Full credit to the original authors. This version is customized for personal/research/educational use.# Object_Detection
