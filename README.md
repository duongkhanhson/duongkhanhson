# Python Computer Vision Portfolio

This repository showcases Python-based computer vision and camera stream projects, with a polished featured project designed for GitHub presentation.

## Featured Project

### Phone Camera Face Recognition UI

- Folder: `phone-camera-face-recognition`
- Main script: `phone-camera-face-recognition/phone_cam_face_gui.py`
- Purpose: Connects to a phone camera stream and detects faces in real time using OpenCV and Tkinter.
- Documentation: `phone-camera-face-recognition/README.md`

## Repository Overview

This repository is structured to support GitHub visibility and easy browsing:

- `phone-camera-face-recognition/` — dedicated project folder with source, dependencies, and project README
- `docs/` — GitHub Pages landing content for the project
- `.gitignore` — excludes virtual environments, caches, and local IDE files

## Quick Start

```bash
pip install -r phone-camera-face-recognition/requirements.txt
python phone-camera-face-recognition/phone_cam_face_gui.py
```

## GitHub Pages

The `docs/` folder contains a ready-to-use GitHub Pages landing page. Enable Pages in repository settings and set the source to the `docs/` folder.

## Notes

- Use a phone camera streaming app to generate an MJPEG URL, such as `http://192.168.1.100:8080/video`.
- The app includes a live preview, face-detection toggle, and snapshot capture.
- For a stronger GitHub presentation, the project includes a vector illustration screenshot at `phone-camera-face-recognition/screenshot.svg`.

## Other content

Additional scripts and experiments remain at the repository root for quick reference and future expansion.
