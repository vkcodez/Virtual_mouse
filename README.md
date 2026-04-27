# 🖱️ Virtual Mouse — AI Hand Gesture Control

> Control your computer mouse using **hand gestures** in real-time — no physical mouse required!  
> Built with Python, OpenCV, and MediaPipe.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?style=flat-square&logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Latest-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 📌 About the Project

**Virtual Mouse** is an AI-powered computer vision application that uses your **webcam** and **hand gestures** to control the mouse cursor on your screen — completely hands-free. Using real-time hand landmark detection via **MediaPipe**, your finger positions are mapped to screen coordinates, enabling full mouse functionality without any hardware device.

### ✨ Key Features

- 🖐️ Real-time hand detection and tracking
- 🖱️ Move the cursor with your index finger
- 👆 Left click using index + thumb pinch gesture
- ✌️ Scroll using two-finger gesture
- 🔒 Smooth cursor movement with frame interpolation
- ⚡ Low-latency response using PyAutoGUI
- 💻 Works on Windows, macOS, and Linux

---

## 🧠 How It Works

```
Webcam Feed → MediaPipe Hand Detection → Finger Landmark Extraction
     → Map to Screen Coordinates → PyAutoGUI Mouse Control
```

| Gesture | Action |
|---|---|
| ☝️ Index finger up | Move cursor |
| 🤏 Index + Thumb pinch | Left click |
| ✌️ Index + Middle fingers | Scroll mode |
| ✊ Closed fist | Stop / idle |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.8+** | Core programming language |
| **OpenCV** | Webcam capture & frame processing |
| **MediaPipe** | Hand landmark detection (21 key points) |
| **PyAutoGUI** | OS-level mouse control |
| **NumPy** | Coordinate math & smoothing |

---

## 📁 Project Structure

```
virtual-mouse/
│
├── main.py        # Main application file
├── py.txt        # code python 
├──python_setup.py   # Full comments & virtual mapping guide
├── requirements.txt        # All dependencies
└── README.md               # Project documentation 
```

---

## ⚙️ Setup & Installation

### ✅ Prerequisites

- Python 3.8 or 3.10
- Webcam / built-in camera
- pip (Python package manager)

---

### 📥 Step 1 — Clone the Repository

```bash
git clone https://github.com/vkcodez/virtual_mouse.git
cd virtual_mouse
```

---

### 📦 Step 2 — Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 📋 Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install opencv-python mediapipe pyautogui numpy
```

---

### 🚀 Step 4 — Run the Application

```bash
python virtual_mouse.py
```

Your webcam will open. Hold your hand in front of the camera and start controlling!

> 💡 **Tip:** Make sure you are in a well-lit environment for best hand detection accuracy.

---

## 📄 requirements.txt

```
opencv-python>=4.5.0
mediapipe>=0.9.0
pyautogui>=0.9.53
numpy>=1.21.0
```

---

## 🖥️ System Requirements

| Component | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 / macOS 10.14 / Ubuntu 18.04 | Windows 11 / macOS 12+ / Ubuntu 22.04 |
| Python | 3.8 | 3.10+ |
| RAM | 4 GB | 8 GB |
| Camera | 720p webcam | 1080p webcam |
| CPU | Dual Core | Quad Core |

---

## 🐛 Troubleshooting

**Camera not detected:**
```bash
# Check camera index — change 0 to 1 if built-in camera is not working
cap = cv2.VideoCapture(1)
```

**PyAutoGUI permission error on macOS:**
> Go to System Preferences → Security & Privacy → Accessibility → Enable Terminal / IDE

**Hand not detecting properly:**
- Improve lighting in your environment
- Keep hand 30–60 cm from camera
- Use a plain background for better contrast

**Laggy cursor movement:**
- Lower the webcam resolution in code: `cap.set(3, 640)` and `cap.set(4, 480)`
- Close other background applications

---

## 🔮 Future Improvements

- [ ] Right-click gesture support
- [ ] Double-click gesture
- [ ] Drag and drop functionality
- [ ] Multi-hand support
- [ ] GUI settings panel for sensitivity adjustment
- [ ] Voice command integration

---

## 👤 Author

**Vetri Kumar S**  
B.Sc. Information Technology | AI/ML Enthusiast  
📧 vetrikumarvel@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/vkcodez)  
🐙 [GitHub](https://github.com/vkcodez)

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

## ⭐ Show Your Support

If you found this project helpful, please consider giving it a **⭐ star** on GitHub — it means a lot!

```
git clone https://github.com/vkcodez/virtual_mouse.git
```
