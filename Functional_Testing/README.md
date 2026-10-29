# Student Engagement Detection System

## Overview

Student Engagement Detection System is a computer vision and deep learning application that estimates student engagement by analyzing eye gaze and facial emotions from recorded videos or real-time webcam streams.

The system is designed to assist educators in understanding student attention levels during online or classroom learning environments through automated visual analysis.

---

## Features

- Eye gaze detection
- Facial emotion recognition
- Video file analysis
- Real-time webcam analysis
- Parallel processing for faster execution
- Generation of annotated output videos
- Generation of engagement analysis reports

---

## Project Structure

```
Student-Engagement-Detection/
│
├── cam/
├── models/
├── output/
├── eyegaze.py
├── emotion.py
├── eyegaze_cam.py
├── emotion_cam.py
├── requirements.txt
└── README.md
```

---

## Prerequisites

Before running the project, install the following:

- Python 3.8 or later
- pip
- GNU Parallel

Creating a virtual environment is recommended.

---

## Installation

Clone the repository.

```bash
git clone https://github.com/your-username/student-engagement-detection.git
```

Move into the project directory.

```bash
cd student-engagement-detection
```

Create a virtual environment.

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Existing Video

Place the input video in the root directory and rename it as:

```
input.mov
```

Execute:

```bash
parallel ::: "python eyegaze.py" "python emotion.py"
```

The program generates:

```
resultEyegaze.txt
resultEmotion.txt
output_eyegaze.mp4
output_emotion.mp4
```

---

### Real-Time Webcam

Navigate to the camera directory.

```bash
cd cam
```

Run:

```bash
parallel ::: "python eyegaze_cam.py" "python emotion_cam.py"
```

The webcam will start automatically and begin analyzing student engagement.

---

## Output

The application generates the following files.

| File | Description |
|------|-------------|
| resultEyegaze.txt | Eye gaze analysis results |
| resultEmotion.txt | Facial emotion analysis results |
| output_eyegaze.mp4 | Annotated eye gaze video |
| output_emotion.mp4 | Annotated emotion video |

---

## Technology Stack

- Python
- OpenCV
- TensorFlow
- Dlib
- NumPy
- GNU Parallel

---

## Applications

- Smart classrooms
- Online education
- Student engagement monitoring
- Educational analytics
- Human-computer interaction research

---

## Future Enhancements

- Gesture recognition
- Head pose estimation
- Blink detection
- Engagement score prediction
- Dashboard for real-time analytics
- Multi-student monitoring
- Database integration
- Report generation

---