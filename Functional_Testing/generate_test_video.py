#!/usr/bin/env python3
"""Generate a short synthetic MP4 for upload/playback/decoder tests.

This fixture contains graphics only, not a face; it cannot validate AI accuracy.
"""
from pathlib import Path
import cv2
import numpy as np

OUT = Path(__file__).resolve().parent / "test_inputs" / "synthetic_test_video.mp4"
OUT.parent.mkdir(parents=True, exist_ok=True)
WIDTH, HEIGHT, FPS, SECONDS = 640, 360, 20, 8
writer = cv2.VideoWriter(str(OUT), cv2.VideoWriter_fourcc(*"mp4v"), FPS, (WIDTH, HEIGHT))
if not writer.isOpened():
    raise SystemExit("Could not create MP4. Check that your OpenCV build supports mp4v encoding.")
try:
    total = FPS * SECONDS
    for i in range(total):
        frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
        # Smoothly changing background provides distinct frames for decoder testing.
        frame[:] = (25 + (i * 2) % 80, 35 + (i * 3) % 90, 65 + (i * 4) % 100)
        cv2.rectangle(frame, (35, 55), (605, 305), (235, 235, 235), 2)
        cv2.putText(frame, "FUNCTIONAL TEST VIDEO", (75, 135), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, f"Frame {i + 1:03d} / {total}", (190, 195), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "Synthetic input - no real person", (125, 245), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (230, 230, 230), 1, cv2.LINE_AA)
        x = 55 + (i * 7) % 500
        cv2.circle(frame, (x, 80), 9, (80, 220, 255), -1)
        writer.write(frame)
finally:
    writer.release()
print(f"Generated: {OUT} ({OUT.stat().st_size:,} bytes)")
