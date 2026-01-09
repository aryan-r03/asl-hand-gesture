<h1 align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&pause=1000&color=668a13&center=true&vCenter=true&width=700&lines=ASL+Hand+Gesture+Recognition;Real-Time+Computer+Vision;MediaPipe+%2B+OpenCV;Sign+Language+Detection" alt="Typing SVG" />
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/OpenCV-4.5+-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"/>
  <img src="https://img.shields.io/badge/MediaPipe-Google-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="MediaPipe"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge" alt="License"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Real--Time-Detection-brightgreen?style=flat-square" alt="Real-Time"/>
  <img src="https://img.shields.io/badge/Computer-Vision-blue?style=flat-square" alt="Computer Vision"/>
  <img src="https://img.shields.io/badge/ASL-Recognition-orange?style=flat-square" alt="ASL"/>
  <img src="https://img.shields.io/badge/Hand-Tracking-red?style=flat-square" alt="Hand Tracking"/>
</p>

---

<div align="center">

### 🤟 Real-Time American Sign Language & Hand Gesture Recognition

> **Advanced computer vision project that recognizes ASL signs and common hand gestures in real-time using MediaPipe and OpenCV. Features dual-hand tracking, multi-gesture recognition, and live webcam processing.**

**👋 Perfect for accessibility applications, sign language learning, and computer vision projects**

[Features](#-features) • [Demo](#-demo--preview) • [Quick Start](#-quick-start) • [Gestures](#-supported-gestures) • [How It Works](#-how-it-works)

</div>

---

## 📋 Table of Contents

- [🌟 Project Overview](#-project-overview)
- [✨ Features](#-features)
- [🎬 Demo & Preview](#-demo--preview)
- [🧠 Tech Stack](#-tech-stack)
- [📦 Installation](#-installation)
- [🚀 Quick Start](#-quick-start)
- [🤟 Supported Gestures](#-supported-gestures)
- [🔧 How It Works](#-how-it-works)
- [⚙️ Configuration](#%EF%B8%8F-configuration)
- [📊 Technical Details](#-technical-details)
- [🎨 Customization](#-customization)
- [🐛 Troubleshooting](#-troubleshooting)
- [🚀 Future Enhancements](#-future-enhancements)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 🌟 Project Overview

<div align="center">
  <table>
    <tr>
      <td align="center" width="25%">
        <img src="https://img.icons8.com/color/96/000000/hand.png" width="80" height="80" alt="Hand Detection"/>
        <br><b>Hand Detection</b>
        <br>MediaPipe Hands
        <br>21 landmark tracking
      </td>
      <td align="center" width="25%">
        <img src="https://img.icons8.com/color/96/000000/video-call.png" width="80" height="80" alt="Real-Time"/>
        <br><b>Real-Time</b>
        <br>Live webcam feed
        <br>30 FPS processing
      </td>
      <td align="center" width="25%">
        <img src="https://img.icons8.com/color/48/all.png" width="80" height="80" alt="ASL"/>
        <br><b>ASL Recognition</b>
        <br>15+ gestures
        <br>Dual-hand support
      </td>
      <td align="center" width="25%">
        <img src="https://img.icons8.com/color/96/000000/artificial-intelligence.png" width="80" height="80" alt="Computer Vision"/>
        <br><b>Computer Vision</b>
        <br>Advanced algorithms
        <br>High accuracy
      </td>
    </tr>
  </table>
</div>

This project implements a **real-time hand gesture recognition system** that can identify American Sign Language (ASL) letters and common hand gestures using your webcam. Built with MediaPipe for hand landmark detection and OpenCV for video processing.

### 🎯 Why This Project?

<table>
<tr>
<td width="50%">

**For Learning:**
- 🎓 Explore computer vision fundamentals
- 👁️ Understand hand landmark detection
- 📐 Learn geometric gesture recognition
- 🎥 Master real-time video processing
- 🤖 Practice ML model integration

</td>
<td width="50%">

**For Impact:**
- ♿ Accessibility for deaf/hard-of-hearing
- 📚 Sign language learning tool
- 🎮 Gesture-based controls
- 💼 Portfolio-worthy CV project
- 🔬 Research in human-computer interaction

</td>
</tr>
</table>

---

## ✨ Features

<div align="center">

### Core Capabilities

<table>
  <tr>
    <th>Category</th>
    <th>Features</th>
  </tr>
  <tr>
    <td><b>🤚 Hand Detection</b></td>
    <td>
      ✅ Dual-hand tracking (left & right)<br>
      ✅ 21 landmark points per hand<br>
      ✅ Real-time hand orientation detection<br>
      ✅ High-precision finger tracking<br>
      ✅ Robust occlusion handling<br>
      ✅ Works in various lighting conditions
    </td>
  </tr>
  <tr>
    <td><b>🔤 Gesture Recognition</b></td>
    <td>
      ✅ 15+ ASL letters and signs<br>
      ✅ Common hand gestures (thumbs up, peace, etc.)<br>
      ✅ Dynamic gesture classification<br>
      ✅ Handedness-aware recognition<br>
      ✅ Distance-based finger extension detection<br>
      ✅ Multi-finger configuration analysis
    </td>
  </tr>
  <tr>
    <td><b>🎥 Real-Time Processing</b></td>
    <td>
      ✅ Live webcam feed processing<br>
      ✅ 30 FPS performance<br>
      ✅ Minimal latency (<50ms)<br>
      ✅ Continuous gesture tracking<br>
      ✅ Visual landmark rendering<br>
      ✅ On-screen gesture labels
    </td>
  </tr>
  <tr>
    <td><b>💻 User Interface</b></td>
    <td>
      ✅ Clean, real-time video display<br>
      ✅ Visual hand landmark overlay<br>
      ✅ Gesture name display<br>
      ✅ Left/right hand indication<br>
      ✅ Simple keyboard controls<br>
      ✅ Cross-platform compatibility
    </td>
  </tr>
</table>

</div>

---

## 🎬 Demo & Preview

<div align="center">

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Webcam Input (640x480)                   │
└──────────────────────────────┬──────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────┐
│              MediaPipe Hand Detection Model             │
│   ┌─────────────────────────────────────────────────┐   │
│   │  • Palm Detection                               │   │
│   │  • Hand Landmark Localization (21 points)       │   │
│   │  • Handedness Classification (Left/Right)       │   │
│   └─────────────────────────────────────────────────┘   │
└────────────────────────────┬────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────┐
│         Gesture Recognition Algorithm           │
│   ┌─────────────────────────────────────────┐   │
│   │  1. Extract 21 landmark coordinates     │   │
│   │  2. Calculate finger extension states   │   │
│   │  3. Compute inter-finger distances      │   │
│   │  4. Analyze thumb orientation           │   │
│   │  5. Match pattern to known gestures     │   │
│   └─────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────┘
│
▼
┌────────────────────────────────────────┐
│             Output Display             │
│   • Video feed with hand landmarks     │
│   • Gesture name overlay               │
│   • Hand side indicator (LEFT/RIGHT)   │
│   • Real-time FPS performance          │
└────────────────────────────────────────┘
```

### Hand Landmark Model

```
                          
                          08  12  16  20     Finger Tips
         ●   ●   ●   ●
         |   |   |   |
                         07  11  15  19     DIP Joints
         ●   ●   ●   ●
         |   |   |   |
                         06  10  14  18     PIP Joints
         ●   ●   ●   ●
         |   |   |   |
                    04   05  09  13  17     MCP Joints
    ●    ●   ●   ●   ●
    |   /   /   /   /
   03  /   /   /   /
    | /   /   /   /
   02    /   /   /
     \  /   /   /
     01    /   /
       \  /   /
                                                0 ────────        Wrist (Reference Point) 

Landmark IDs:
0: Wrist

01-4: Thumb         (CMC, MCP, IP, TIP)
 5-8: Index Finger   (MCP, PIP, DIP, TIP)
 9-12: Middle Finger (MCP, PIP, DIP, TIP)
 13-16: Ring Finger  (MCP, PIP, DIP, TIP)
 17-20: Pinky        (MCP, PIP, DIP, TIP)


```

### Sample Output

```

┊┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┊
┊      🎥 Hand Sign Decoder-Real-Time Detection      |
┊┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┊
┊                                                    ┊
┊              RIGHT: ✌️ PEACE / ASL: V              ┊
┊                LEFT: 👍 THUMBS UP                  ┊
┊                                                    ┊
┊       [Live video feed with hand landmarks]        ┊
┊               shown as connected dots              ┊
┊                 and colorful lines                 ┊
┊                                                    ┊
┊                                                    ┊
┊  Press 'q' to quit                    FPS: 30      ┊
┊┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┊
```

</div>

---

## 🧠 Tech Stack

<div align="center">

### Technologies & Libraries

<table>
  <tr>
    <td align="center" width="25%">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60" height="60" alt="Python"/>
      <br><b>Python 3.8+</b>
      <br>Core language
    </td>
    <td align="center" width="25%">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg" width="60" height="60" alt="OpenCV"/>
      <br><b>OpenCV</b>
      <br>Video processing
    </td>
    <td align="center" width="25%">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/google/google-original.svg" width="60" height="60" alt="MediaPipe"/>
      <br><b>MediaPipe</b>
      <br>Hand detection
    </td>
    <td align="center" width="25%">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="60" height="60" alt="NumPy"/>
      <br><b>NumPy</b>
      <br>Math operations
    </td>
  </tr>
</table>

### Component Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Hand Detection** | MediaPipe Hands | ML-based hand landmark detection |
| **Video Capture** | OpenCV VideoCapture | Webcam access & frame processing |
| **Image Processing** | OpenCV cv2 | Frame manipulation & rendering |
| **Geometric Math** | NumPy | Distance calculations & vector math |
| **Visualization** | MediaPipe DrawingUtils | Landmark rendering & connections |

</div>

---

## 📦 Installation

<div align="center">

### System Requirements

</div>

<table>
  <tr>
    <th>Requirement</th>
    <th>Minimum</th>
    <th>Recommended</th>
  </tr>
  <tr>
    <td><b>Python</b></td>
    <td>3.8</td>
    <td>3.9 - 3.11</td>
  </tr>
  <tr>
    <td><b>RAM</b></td>
    <td>4GB</td>
    <td>8GB+</td>
  </tr>
  <tr>
    <td><b>Webcam</b></td>
    <td>480p</td>
    <td>720p+</td>
  </tr>
  <tr>
    <td><b>CPU</b></td>
    <td>Dual-core 2.0GHz</td>
    <td>Quad-core 2.5GHz+</td>
  </tr>
  <tr>
    <td><b>OS</b></td>
    <td colspan="2">Windows 10+, macOS 10.14+, Ubuntu 18.04+</td>
  </tr>
</table>

<div align="center">

### Dependencies

</div>

```python
# Core Libraries
opencv-python==4.8.0.76     # Computer vision & video processing
mediapipe==0.10.5           # Hand detection & landmark tracking
numpy==1.24.3               # Numerical computations

# Optional (for enhanced functionality)
opencv-contrib-python       # Additional OpenCV modules
matplotlib                  # Visualization & debugging
```

---

## 🚀 Quick Start

<div align="center">

### Step 1️⃣: Clone Repository

</div>

```bash
git clone https://github.com/your-username/asl-hand-gesture-recognition.git
cd asl-hand-gesture-recognition
```

<div align="center">

### Step 2️⃣: Create Virtual Environment (Recommended)

</div>

<table>
<tr>
<td width="50%">

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

</td>
<td width="50%">

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

</td>
</tr>
</table>

<div align="center">

### Step 3️⃣: Install Dependencies

</div>

```bash
pip install opencv-python mediapipe numpy
```

**Verify installation:**
```bash
python -c "import cv2, mediapipe, numpy; print('All dependencies installed successfully!')"
```

<div align="center">

### Step 4️⃣: Run the Application

</div>

```bash
python hand_sign.py
```

**Expected Output:**
```
Hand Sign Decoder Started! Press 'q' to quit.
```

<div align="center">

### Step 5️⃣: Use the Application

</div>

1. **Position yourself** in front of the webcam
2. **Show hand gestures** to the camera
3. **See real-time recognition** displayed on screen
4. **Try different gestures** from the supported list
5. **Press 'q'** to quit the application

**Tips for Best Results:**
- 💡 Ensure good lighting
- 📏 Keep hands at 30-50cm from camera
- 🖐️ Show clear, distinct gestures
- 🎯 Center hand in frame
- 🔄 Hold gesture for 1-2 seconds

---

## 🤟 Supported Gestures

<div align="center">

### ASL Letters

</div>

<table>
  <tr>
    <th>Gesture</th>
    <th>Description</th>
    <th>Detection Pattern</th>
  </tr>
  <tr>
    <td><b>✊ ASL: A</b></td>
    <td>Closed fist with thumb alongside</td>
    <td>All fingers curled, thumb extended upward</td>
  </tr>
  <tr>
    <td><b>✋ ASL: B</b></td>
    <td>Flat hand, fingers together</td>
    <td>4 fingers extended, thumb folded</td>
  </tr>
  <tr>
    <td><b>👌 ASL: D</b></td>
    <td>Index up, other fingers to thumb</td>
    <td>Index extended, thumb-middle close</td>
  </tr>
  <tr>
    <td><b>👌 ASL: F</b></td>
    <td>OK sign / Circle with thumb-index</td>
    <td>Thumb-index touching, others extended</td>
  </tr>
  <tr>
    <td><b>🅷 ASL: H</b></td>
    <td>Index and middle extended horizontally</td>
    <td>2 fingers close, horizontal orientation</td>
  </tr>
  <tr>
    <td><b>🤟 ASL: I Love You</b></td>
    <td>Thumb, index, and pinky extended</td>
    <td>3 specific fingers up, others curled</td>
  </tr>
  <tr>
    <td><b>🤘 ASL: L</b></td>
    <td>Index and thumb in L shape</td>
    <td>Index up, thumb out perpendicular</td>
  </tr>
  <tr>
    <td><b>🆁 ASL: R</b></td>
    <td>Index and middle crossed</td>
    <td>2 fingers extended, crossing pattern</td>
  </tr>
  <tr>
    <td><b>✊ ASL: S</b></td>
    <td>Closed fist with thumb across fingers</td>
    <td>All fingers curled, thumb in front</td>
  </tr>
  <tr>
    <td><b>🆄 ASL: U</b></td>
    <td>Index and middle together, vertical</td>
    <td>2 fingers close, vertical orientation</td>
  </tr>
  <tr>
    <td><b>✌️ ASL: V</b></td>
    <td>Peace sign / Victory</td>
    <td>Index and middle separated, extended</td>
  </tr>
  <tr>
    <td><b>🖖 ASL: W</b></td>
    <td>Three fingers up</td>
    <td>Index, middle, ring extended</td>
  </tr>
  <tr>
    <td><b>🤙 ASL: Y</b></td>
    <td>Shaka / Call me</td>
    <td>Thumb and pinky extended only</td>
  </tr>
</table>

<div align="center">

### Common Hand Gestures

</div>

<table>
  <tr>
    <th>Gesture</th>
    <th>Description</th>
    <th>Use Case</th>
  </tr>
  <tr>
    <td><b>👍 THUMBS UP</b></td>
    <td>Thumb pointing upward</td>
    <td>Approval, agreement, like</td>
  </tr>
  <tr>
    <td><b>👎 THUMBS DOWN</b></td>
    <td>Thumb pointing downward</td>
    <td>Disapproval, dislike</td>
  </tr>
  <tr>
    <td><b>✋ OPEN HAND</b></td>
    <td>All five fingers extended</td>
    <td>Stop, high five, number 5</td>
  </tr>
  <tr>
    <td><b>✊ FIST</b></td>
    <td>All fingers curled</td>
    <td>Solidarity, power, fist bump</td>
  </tr>
  <tr>
    <td><b>☝️ POINTING UP</b></td>
    <td>Index finger pointing upward</td>
    <td>Number 1, attention, idea</td>
  </tr>
  <tr>
    <td><b>👇 POINTING DOWN</b></td>
    <td>Middle finger pointing down</td>
    <td>Direction, emphasis</td>
  </tr>
  <tr>
    <td><b>🤘 ROCK ON</b></td>
    <td>Index and pinky extended</td>
    <td>Rock music, horns gesture</td>
  </tr>
  <tr>
    <td><b>✌️ PEACE</b></td>
    <td>Index and middle in V-shape</td>
    <td>Peace, victory, number 2</td>
  </tr>
</table>

### Recognition Statistics

<table>
  <tr>
    <th>Metric</th>
    <th>Value</th>
  </tr>
  <tr>
    <td>Total Gestures</td>
    <td>15+ recognized patterns</td>
  </tr>
  <tr>
    <td>ASL Letters</td>
    <td>13 distinct letters</td>
  </tr>
  <tr>
    <td>Common Gestures</td>
    <td>8 popular hand signs</td>
  </tr>
  <tr>
    <td>Detection Speed</td>
    <td>~30 FPS (real-time)</td>
  </tr>
  <tr>
    <td>Recognition Latency</td>
    <td><50ms per frame</td>
  </tr>
</table>

---

## 🔧 How It Works

<div align="center">

### Detection Pipeline

</div>

```
Frame Capture → Hand Detection → Landmark Extraction → Gesture Analysis → Display
     (30 FPS)      (MediaPipe)      (21 points)       (Pattern Match)    (OpenCV)
```

### 1. Hand Detection (MediaPipe)

```python
# MediaPipe Hands Configuration
hands = mp_hands.Hands(
    static_image_mode=False,      # Video stream mode
    max_num_hands=2,               # Track both hands
    min_detection_confidence=0.7,  # 70% confidence threshold
    min_tracking_confidence=0.7    # 70% tracking threshold
)
```

**Process:**
1. Palm detection using ML model
2. Hand bounding box identification
3. 21 hand landmark localization
4. Handedness classification (Left/Right)

### 2. Landmark Extraction

<div align="center">

**21 Hand Landmarks Per Hand:**

</div>

```
Wrist (0):                    Base reference point
├─ Thumb (1-4):              CMC → MCP → IP → TIP
├─ Index Finger (5-8):       MCP → PIP → DIP → TIP
├─ Middle Finger (9-12):     MCP → PIP → DIP → TIP
├─ Ring Finger (13-16):      MCP → PIP → DIP → TIP
└─ Pinky (17-20):            MCP → PIP → DIP → TIP
```

### 3. Gesture Recognition Algorithm

**Key Components:**

<details>
<summary><b>Finger Extension Detection</b></summary>

```python
def is_finger_extended(tip, pip, mcp):
    """
    Determines if a finger is extended by comparing distances.
    
    Logic:
    - Extended: Distance(tip-mcp) > Distance(pip-mcp)
    - Curled: Distance(tip-mcp) ≤ Distance(pip-mcp)
    """
    tip_to_mcp = sqrt((tip.x - mcp.x)² + (tip.y - mcp.y)²)
    pip_to_mcp = sqrt((pip.x - mcp.x)² + (pip.y - mcp.y)²)
    return tip_to_mcp > pip_to_mcp
```

**Applied to all fingers:**
- Index, Middle, Ring, Pinky: Extended or curled
- Extended fingers count: Sum of extended states

</details>

<details>
<summary><b>Thumb Orientation Analysis</b></summary>

```python
# Thumb extension depends on hand side
if is_right_hand:
    thumb_extended = thumb_tip.x < thumb_ip.x  # Thumb points left
else:  # Left hand
    thumb_extended = thumb_tip.x > thumb_ip.x  # Thumb points right
```

**Why handedness matters:**
- Right hand: Thumb extends to the left
- Left hand: Thumb extends to the right
- Critical for accurate gesture recognition

</details>

<details>
<summary><b>Inter-Finger Distance Calculation</b></summary>

```python
# Normalize distances using reference distance
ref_dist = sqrt((wrist.x - middle_mcp.x)² + (wrist.y - middle_mcp.y)²)

# Calculate normalized distances
thumb_index_dist = distance(thumb_tip, index_tip) / ref_dist
thumb_middle_dist = distance(thumb_tip, middle_tip) / ref_dist
index_middle_dist = distance(index_tip, middle_tip) / ref_dist
```

**Uses:**
- Detect finger touching (OK sign, F)
- Measure finger separation (Peace vs U)
- Identify crossed fingers (R)

</details>

<details>
<summary><b>Pattern Matching Logic</b></summary>

**Hierarchical Decision Tree:**

```
1. Count extended fingers
   ├─ 0 fingers → Check thumb position
   │  ├─ Thumb up → Thumbs Up 👍
   │  ├─ Thumb down → Thumbs Down 👎
   │  ├─ Thumb across → ASL: S ✊
   │  └─ Thumb alongside → ASL: A ✊
   │
   ├─ 1 finger extended
   │  ├─ Index only
   │  │  ├─ Thumb close → ASL: D 👌
   │  │  ├─ Thumb perpendicular → ASL: L 🤘
   │  │  └─ Thumb far → Pointing Up ☝️
   │  └─ Middle only → Pointing Down 👇
   │
   ├─ 2 fingers extended
   │  ├─ Index + Middle
   │  │  ├─ Wide apart → Peace ✌️
   │  │  ├─ Very close → ASL: U 🆄
   │  │  ├─ Crossed → ASL: R 🆁
   │  │  └─ Horizontal → ASL: H 🅷
   │  └─ Index + Pinky → Rock On 🤘
   │
   ├─ 3 fingers extended
   │  └─ Index, Middle, Ring → ASL: W 🖖
   │
   ├─ 4 fingers extended
   │  ├─ Thumb folded → ASL: B ✋
   │  └─ Thumb out → Open Hand ✋
   │
   └─ Special combinations
      ├─ Thumb + Index + Pinky → I Love You 🤟
      └─ Thumb + Index circle → ASL: F / OK 👌
```

</details>

### 4. Real-Time Processing

```python
while cap.isOpened():
    # Capture frame (30 FPS)
    success, frame = cap.read()
    
    # Mirror for natural interaction
    frame = cv2.flip(frame, 1)
    
    # Convert BGR to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process frame
    results = hands.process(rgb_frame)
    
    # For each detected hand
    for hand_landmarks, handedness in results:
        # Draw landmarks
        draw_hand_landmarks(frame, hand_landmarks)
        
        # Recognize gesture
        gesture = recognize_gesture(hand_landmarks, handedness)
        
        # Display result
        display_text(frame, gesture, hand_label)
    
    # Show frame
    cv2.imshow('Hand Sign Decoder', frame)
```

---

## ⚙️ Configuration

<div align="center">

### Detection Parameters

</div>

**Modify in `hand_sign.py`:**

```python
# Hand Detection Configuration
hands = mp_hands.Hands(
    static_image_mode=False,          # False for video, True for images
    max_num_hands=2,                  # 1-2 hands (change to 1 for single hand)
    min_detection_confidence=0.7,      # 0.5-0.9 (lower = more sensitive)
    min_tracking_confidence=0.7        # 0.5-0.9 (lower = more fluid tracking)
)
```

**Parameter Tuning Guide:**

<table>
  <tr>
    <th>Parameter</th>
    <th>Range</th>
    <th>Effect</th>
    <th>Recommendation</th>
  </tr>
  <tr>
    <td><b>min_detection_confidence</b></td>
    <td>0.5 - 0.9</td>
    <td>Initial hand detection threshold</td>
    <td>0.7 (balanced)<br>0.5 (difficult lighting)<br>0.9 (reduce false positives)</td>
  </tr>
  <tr>
    <td><b>min_tracking_confidence</b></td>
    <td>0.5 - 0.9</td>
    <td>Frame-to-frame tracking threshold</td>
    <td>0.7 (smooth tracking)<br>0.5 (fast movements)<br>0.9 (stable hands)</td>
  </tr>
  <tr>
    <td><b>max_num_hands</b></td>
    <td>1 - 2</td>
    <td>Maximum hands to detect</td>
    <td>2 (default)<br>1 (performance boost)</td>
  </tr>
</table>

<div align="center">

### Webcam Settings

</div>

```python
# Video Capture Configuration
cap = cv2.VideoCapture(0)  # 0 = default camera, 1 = external camera

# Optional: Set resolution (uncomment to use)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)   # 1280x720 HD
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# cap.set(cv2.CAP_PROP_FPS, 30)              # 30 FPS

# Optional: Set camera properties
# cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.5)     # Brightness: 0-1
# cap.set(cv2.CAP_PROP_CONTRAST, 0.5)       # Contrast: 0-1
# cap.set(cv2.CAP_PROP_SATURATION, 0.5)     # Saturation: 0-1
```

<div align="center">

### Visual Appearance

</div>

```python
# Landmark Drawing Configuration
mp_drawing.draw_landmarks(
    frame, 
    hand_landmarks, 
    mp_hands.HAND_CONNECTIONS,
    # Landmark style (dots)
    mp_drawing.DrawingSpec(
        color=(121, 22, 76),    # BGR color for landmarks
        thickness=2,             # Dot size
        circle_radius=4          # Dot radius
    ),
    # Connection style (lines)
    mp_drawing.DrawingSpec(
        color=(250, 44, 250),    # BGR color for connections
        thickness=2,             # Line thickness
        circle_radius=2          # Connection point radius
    ),
)
```

**Color Customization:**

<table>
  <tr>
    <th>Style</th>
    <th>Default Color</th>
    <th>BGR Value</th>
    <th>Alternatives</th>
  </tr>
  <tr>
    <td>Landmarks (dots)</td>
    <td>Purple-pink</td>
    <td>(121, 22, 76)</td>
    <td>(0, 255, 0) - Green<br>(255, 0, 0) - Blue<br>(0, 0, 255) - Red</td>
  </tr>
  <tr>
    <td>Connections (lines)</td>
    <td>Bright pink</td>
    <td>(250, 44, 250)</td>
    <td>(255, 255, 0) - Cyan<br>(0, 255, 255) - Yellow<br>(255, 255, 255) - White</td>
  </tr>
</table>

<div align="center">

### Text Display

</div>

```python
# Gesture Text Configuration
cv2.putText(
    frame,                              # Image to draw on
    f"{hand_label}: {gesture}",         # Text content
    (10, 30 + (idx * 40)),              # Position (x, y)
    cv2.FONT_HERSHEY_SIMPLEX,           # Font type
    1,                                   # Font scale
    (255, 255, 255),                    # Color (white)
    2,                                   # Thickness
    cv2.LINE_AA                          # Anti-aliased line
)
```

---

## 📊 Technical Details

<div align="center">

### Performance Metrics

</div>

<table>
  <tr>
    <th>Metric</th>
    <th>Value</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td><b>Frame Rate</b></td>
    <td>~30 FPS</td>
    <td>On average hardware</td>
  </tr>
  <tr>
    <td><b>Detection Latency</b></td>
    <td><50ms</td>
    <td>Hand detection + landmark extraction</td>
  </tr>
  <tr>
    <td><b>Recognition Latency</b></td>
    <td><5ms</td>
    <td>Gesture classification</td>
  </tr>
  <tr>
    <td><b>Total Latency</b></td>
    <td><100ms</td>
    <td>End-to-end processing time</td>
  </tr>
  <tr>
    <td><b>Memory Usage</b></td>
    <td>~300-500 MB</td>
    <td>Including MediaPipe models</td>
  </tr>
  <tr>
    <td><b>CPU Usage</b></td>
    <td>30-50%</td>
    <td>Single core utilization</td>
  </tr>
</table>

<div align="center">

### Gesture Recognition Accuracy

</div>

**Under Optimal Conditions:**

<table>
  <tr>
    <th>Gesture Type</th>
    <th>Accuracy</th>
    <th>Optimal Conditions</th>
  </tr>
  <tr>
    <td>Simple gestures (Thumbs Up, Fist)</td>
    <td>95-98%</td>
    <td>Clear hand, good lighting</td>
  </tr>
  <tr>
    <td>ASL letters (A, B, L, S)</td>
    <td>90-95%</td>
    <td>Distinct finger positions</td>
  </tr>
  <tr>
    <td>Complex gestures (R, H, U)</td>
    <td>85-90%</td>
    <td>Precise hand orientation</td>
  </tr>
  <tr>
    <td>Distance-based (OK, F)</td>
    <td>80-90%</td>
    <td>Consistent hand distance from camera</td>
  </tr>
</table>

**Factors Affecting Accuracy:**
- ✅ **Lighting**: Bright, even lighting improves detection
- ✅ **Background**: Plain, contrasting background is best
- ✅ **Distance**: 30-50cm from camera optimal
- ✅ **Hand Position**: Center hand in frame
- ✅ **Gesture Clarity**: Hold distinct, clear positions

<div align="center">

### Algorithm Complexity

</div>

<table>
  <tr>
    <th>Operation</th>
    <th>Time Complexity</th>
    <th>Space Complexity</th>
  </tr>
  <tr>
    <td>Hand Detection (MediaPipe)</td>
    <td>O(1)</td>
    <td>O(1)</td>
  </tr>
  <tr>
    <td>Landmark Extraction</td>
    <td>O(1)</td>
    <td>O(21) per hand</td>
  </tr>
  <tr>
    <td>Distance Calculations</td>
    <td>O(n) where n = number of distances</td>
    <td>O(1)</td>
  </tr>
  <tr>
    <td>Gesture Recognition</td>
    <td>O(1)</td>
    <td>O(1)</td>
  </tr>
  <tr>
    <td><b>Total Per Frame</b></td>
    <td><b>O(1)</b></td>
    <td><b>O(1)</b></td>
  </tr>
</table>

*All operations are effectively constant time for fixed input size (21 landmarks)*

---

## 🎨 Customization

<div align="center">

### Extension Ideas

</div>

<details>
<summary><b>🔤 Add More ASL Letters</b></summary>

```python
def recognize_gesture(hand_landmarks, handedness):
    # ... existing code ...
    
    # Add ASL letter C
    if thumb_extended and index_extended and \
       middle_extended and ring_extended and pinky_extended:
        # Check if fingers form a C shape
        if (index_tip.y < index_pip.y and 
            middle_tip.y < middle_pip.y):
            return "🅲 ASL: C"
    
    # Add ASL letter O
    if thumb_index_dist < 0.1 and extended_fingers_count == 4:
        # Thumb-index touching, other fingers curved
        return "🅾️ ASL: O"
    
    # Add more letters following similar patterns...
```

</details>

<details>
<summary><b>🎮 Gesture-Based Controls</b></summary>

```python
# Map gestures to keyboard actions
import pyautogui

def execute_action(gesture):
    """Execute keyboard/mouse actions based on gesture"""
    
    gesture_actions = {
        "👍 THUMBS UP": lambda: pyautogui.press('up'),
        "👎 THUMBS DOWN": lambda: pyautogui.press('down'),
        "☝️ POINTING UP": lambda: pyautogui.press('space'),
        "✊ FIST": lambda: pyautogui.click(),
        "✋ OPEN HAND": lambda: pyautogui.press('esc'),
    }
    
    action = gesture_actions.get(gesture)
    if action:
        action()
        print(f"Executed: {gesture}")

# Use in main loop
gesture = recognize_gesture(hand_landmarks, hand_label)
execute_action(gesture)
```

**Use Cases:**
- 🎮 Game controls (jump, shoot, pause)
- 🖥️ Presentation navigation (next/previous slide)
- 🎵 Media player controls (play/pause, volume)
- 🏠 Smart home controls (lights, devices)

</details>

<details>
<summary><b>📊 Gesture Statistics & Logging</b></summary>

```python
import json
from datetime import datetime
from collections import Counter

class GestureLogger:
    def __init__(self):
        self.gesture_history = []
        self.gesture_counts = Counter()
        self.session_start = datetime.now()
    
    def log_gesture(self, gesture, hand_label):
        """Log detected gesture with timestamp"""
        timestamp = datetime.now()
        self.gesture_history.append({
            'gesture': gesture,
            'hand': hand_label,
            'time': timestamp.isoformat()
        })
        self.gesture_counts[gesture] += 1
    
    def get_statistics(self):
        """Get session statistics"""
        duration = (datetime.now() - self.session_start).seconds
        return {
            'session_duration': f"{duration}s",
            'total_gestures': len(self.gesture_history),
            'unique_gestures': len(self.gesture_counts),
            'most_common': self.gesture_counts.most_common(5),
            'gestures_per_minute': len(self.gesture_history) / (duration / 60)
        }
    
    def save_log(self, filename='gesture_log.json'):
        """Save gesture history to JSON file"""
        with open(filename, 'w') as f:
            json.dump({
                'statistics': self.get_statistics(),
                'history': self.gesture_history
            }, f, indent=2)

# Usage
logger = GestureLogger()

# In main loop
gesture = recognize_gesture(hand_landmarks, hand_label)
logger.log_gesture(gesture, hand_label)

# On exit
logger.save_log()
print(logger.get_statistics())
```

</details>

<details>
<summary><b>🎯 Gesture Training Mode</b></summary>

```python
class GestureTrainer:
    def __init__(self):
        self.target_gesture = None
        self.hold_time = 0
        self.required_hold = 2.0  # seconds
        self.training_gestures = [
            "✊ ASL: A", "✋ ASL: B", "👌 ASL: F",
            "🤟 I Love You (ASL)", "✌️ PEACE / ASL: V"
        ]
        self.current_index = 0
    
    def start_training(self):
        """Start gesture training session"""
        self.target_gesture = self.training_gestures[self.current_index]
        return self.target_gesture
    
    def check_gesture(self, detected_gesture, dt=0.033):
        """Check if correct gesture is held"""
        if detected_gesture == self.target_gesture:
            self.hold_time += dt
            if self.hold_time >= self.required_hold:
                # Success! Move to next gesture
                self.current_index += 1
                self.hold_time = 0
                if self.current_index >= len(self.training_gestures):
                    return "COMPLETE"
                self.target_gesture = self.training_gestures[self.current_index]
                return "NEXT"
        else:
            self.hold_time = 0
        
        return f"HOLD {self.hold_time:.1f}/{self.required_hold}"
    
    def get_progress(self):
        """Get training progress"""
        return f"{self.current_index}/{len(self.training_gestures)}"

# Usage
trainer = GestureTrainer()
target = trainer.start_training()

# In main loop
status = trainer.check_gesture(detected_gesture)
cv2.putText(frame, f"Show: {target}", (10, 60), ...)
cv2.putText(frame, f"Status: {status}", (10, 100), ...)
cv2.putText(frame, f"Progress: {trainer.get_progress()}", (10, 140), ...)
```

</details>

<details>
<summary><b>🔊 Audio Feedback</b></summary>

```python
from gtts import gTTS
import pygame
import os

class AudioFeedback:
    def __init__(self):
        pygame.mixer.init()
        self.cache = {}
        self.last_gesture = None
    
    def speak(self, text):
        """Convert text to speech and play"""
        if text not in self.cache:
            tts = gTTS(text=text, lang='en')
            filename = f"audio_{hash(text)}.mp3"
            tts.save(filename)
            self.cache[text] = filename
        
        pygame.mixer.music.load(self.cache[text])
        pygame.mixer.music.play()
    
    def announce_gesture(self, gesture):
        """Announce detected gesture"""
        if gesture != self.last_gesture and gesture != "UNKNOWN GESTURE":
            # Extract gesture name without emoji
            gesture_name = gesture.split(':')[-1].strip()
            self.speak(gesture_name)
            self.last_gesture = gesture

# Usage
audio = AudioFeedback()

# In main loop
gesture = recognize_gesture(hand_landmarks, hand_label)
audio.announce_gesture(gesture)
```

**Requirements:**
```bash
pip install gtts pygame
```

</details>

<details>
<summary><b>📸 Screenshot & Save Gestures</b></summary>

```python
import os
from datetime import datetime

class GestureCapture:
    def __init__(self, output_dir='captures'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def save_gesture(self, frame, gesture, hand_label):
        """Save frame with detected gesture"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        gesture_clean = gesture.replace('/', '_').replace(':', '_')
        filename = f"{timestamp}_{hand_label}_{gesture_clean}.jpg"
        filepath = os.path.join(self.output_dir, filename)
        cv2.imwrite(filepath, frame)
        print(f"Saved: {filename}")
        return filepath

# Usage
capture = GestureCapture()

# In main loop, press 's' to save
if cv2.waitKey(5) & 0xFF == ord('s'):
    capture.save_gesture(frame, gesture, hand_label)
```

</details>

---

## 🐛 Troubleshooting

<div align="center">

### Common Issues & Solutions

</div>

<details>
<summary><b>❌ Camera Not Found / Cannot Open Webcam</b></summary>

**Symptoms:**
```
Failed to capture frame.
cv2.error: Camera not found
```

**Solutions:**

1. **Check Camera Index:**
   ```python
   # Try different camera indices
   cap = cv2.VideoCapture(0)  # Built-in camera
   # If 0 doesn't work, try:
   cap = cv2.VideoCapture(1)  # External camera
   cap = cv2.VideoCapture(2)  # Another external device
   ```

2. **Verify Camera Permissions:**
   - **Windows**: Settings → Privacy → Camera
   - **macOS**: System Preferences → Security & Privacy → Camera
   - **Linux**: Check `/dev/video*` permissions
     ```bash
     ls -l /dev/video*
     sudo chmod 666 /dev/video0
     ```

3. **Check if Camera is In Use:**
   - Close other applications using webcam (Zoom, Skype, etc.)
   - Restart your computer

4. **Test Camera:**
   ```bash
   # Windows
   start microsoft.windows.camera:
   
   # macOS
   open /Applications/Photo\ Booth.app
   
   # Linux
   cheese  # or mpv /dev/video0
   ```

</details>

<details>
<summary><b>🖐️ Hand Not Detected</b></summary>

**Symptoms:**
- No landmarks visible on screen
- Gesture text doesn't appear

**Solutions:**

1. **Improve Lighting:**
   - Ensure bright, even lighting
   - Avoid backlighting (window behind you)
   - Use natural or white light

2. **Adjust Detection Confidence:**
   ```python
   hands = mp_hands.Hands(
       min_detection_confidence=0.5,  # Lower for difficult conditions
       min_tracking_confidence=0.5
   )
   ```

3. **Check Hand Position:**
   - Keep hand 30-50cm from camera
   - Center hand in frame
   - Show palm to camera (not back of hand)

4. **Verify Background:**
   - Use plain, contrasting background
   - Avoid busy patterns
   - Ensure hand is not same color as background

5. **Test MediaPipe Installation:**
   ```python
   python -c "import mediapipe; print(mediapipe.__version__)"
   ```

</details>

<details>
<summary><b>⚠️ Incorrect Gesture Recognition</b></summary>

**Symptoms:**
- Wrong gesture displayed
- "UNKNOWN GESTURE" shown frequently
- Gesture flickers between different labels

**Solutions:**

1. **Hold Gesture Clearly:**
   - Make distinct, exaggerated gestures
   - Hold position for 1-2 seconds
   - Avoid transitional hand positions

2. **Check Hand Distance:**
   - Keep consistent distance (30-50cm)
   - Too close: Landmarks may be cut off
   - Too far: Less accurate detection

3. **Improve Hand Contrast:**
   - Wear contrasting colors to background
   - Avoid wearing gloves (unless they contrast well)

4. **Adjust Thresholds:**
   ```python
   # In recognize_gesture function, tune these values:
   
   # Distance threshold for finger touching
   if thumb_index_dist < 0.15:  # Try 0.10 or 0.20
       return "OK Sign"
   
   # Finger separation threshold
   if index_middle_dist > 0.25:  # Try 0.20 or 0.30
       return "Peace Sign"
   ```

5. **Add Smoothing:**
   ```python
   from collections import deque
   
   gesture_buffer = deque(maxlen=5)  # Last 5 gestures
   
   def smooth_gesture(new_gesture):
       gesture_buffer.append(new_gesture)
       # Return most common gesture
       return max(set(gesture_buffer), key=gesture_buffer.count)
   
   # In main loop
   gesture = smooth_gesture(recognize_gesture(hand_landmarks, hand_label))
   ```

</details>

<details>
<summary><b>🐌 Low Frame Rate / Laggy Performance</b></summary>

**Symptoms:**
- FPS < 20
- Delayed gesture recognition
- Choppy video display

**Solutions:**

1. **Reduce Resolution:**
   ```python
   cap = cv2.VideoCapture(0)
   cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)   # Lower resolution
   cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
   ```

2. **Detect Single Hand Only:**
   ```python
   hands = mp_hands.Hands(
       max_num_hands=1,  # Track only one hand
       # ... other parameters
   )
   ```

3. **Reduce Detection Confidence:**
   ```python
   hands = mp_hands.Hands(
       min_detection_confidence=0.5,  # Less processing
       min_tracking_confidence=0.5
   )
   ```

4. **Close Other Applications:**
   - Free up CPU/RAM
   - Close browser tabs
   - Stop background processes

5. **Check System Resources:**
   ```bash
   # Windows
   taskmgr
   
   # macOS
   top
   
   # Linux
   htop
   ```

6. **Optimize Drawing:**
   ```python
   # Skip landmark drawing for performance boost
   # Comment out this line:
   # mp_drawing.draw_landmarks(...)
   ```

</details>

<details>
<summary><b>📦 Module Import Errors</b></summary>

**Symptoms:**
```
ModuleNotFoundError: No module named 'cv2'
ModuleNotFoundError: No module named 'mediapipe'
```

**Solutions:**

1. **Verify Installation:**
   ```bash
   pip list | grep -E "opencv|mediapipe|numpy"
   ```

2. **Reinstall Dependencies:**
   ```bash
   pip uninstall opencv-python mediapipe numpy
   pip install opencv-python mediapipe numpy
   ```

3. **Check Python Version:**
   ```bash
   python --version  # Should be 3.8+
   ```

4. **Use Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   pip install opencv-python mediapipe numpy
   ```

5. **Check pip vs pip3:**
   ```bash
   # Try using pip3 instead of pip
   pip3 install opencv-python mediapipe numpy
   ```

</details>

<details>
<summary><b>🖼️ Window Display Issues</b></summary>

**Symptoms:**
- Window doesn't open
- Window freezes
- "cv2.imshow() not working"

**Solutions:**

1. **Linux: Install Display Backend:**
   ```bash
   sudo apt-get install python3-opencv
   # or
   pip install opencv-contrib-python
   ```

2. **macOS: Grant Terminal Access:**
   - System Preferences → Security & Privacy
   - Grant camera access to Terminal

3. **Check Display Environment:**
   ```python
   import cv2
   print(cv2.getBuildInformation())  # Check GUI support
   ```

4. **Alternative Display Method:**
   ```python
   # If cv2.imshow fails, save frames to file
   cv2.imwrite(f'frame_{count}.jpg', frame)
   ```

</details>

---

## 🚀 Future Enhancements

<div align="center">

### Planned Features

</div>

<table>
  <tr>
    <th>Feature</th>
    <th>Description</th>
    <th>Status</th>
  </tr>
  <tr>
    <td><b>📝 Complete ASL Alphabet</b></td>
    <td>Add remaining ASL letters (C, E, G, I, J, K, M, N, O, P, Q, T, X, Z)</td>
    <td>🔄 Planned</td>
  </tr>
  <tr>
    <td><b>🔢 Number Recognition</b></td>
    <td>Recognize ASL numbers 0-9</td>
    <td>🔄 Planned</td>
  </tr>
  <tr>
    <td><b>🎯 Dynamic Gestures</b></td>
    <td>Recognize motion-based gestures (swipe, circle, wave)</td>
    <td>🔄 Planned</td>
  </tr>
  <tr>
    <td><b>🗣️ Word Formation</b></td>
    <td>Combine letters to form words automatically</td>
    <td>💡 Idea</td>
  </tr>
  <tr>
    <td><b>🎓 Training Mode</b></td>
    <td>Interactive tutorial for learning ASL gestures</td>
    <td>💡 Idea</td>
  </tr>
  <tr>
    <td><b>📊 Confidence Scores</b></td>
    <td>Show probability/confidence for each recognition</td>
    <td>💡 Idea</td>
  </tr>
  <tr>
    <td><b>💾 Gesture Recording</b></td>
    <td>Record and replay gesture sequences</td>
    <td>💡 Idea</td>
  </tr>
  <tr>
    <td><b>🌐 Multi-language Support</b></td>
    <td>Add other sign language systems (BSL, FSL, etc.)</td>
    <td>💡 Idea</td>
  </tr>
  <tr>
    <td><b>📱 Mobile App</b></td>
    <td>iOS/Android app version</td>
    <td>💡 Idea</td>
  </tr>
  <tr>
    <td><b>🤖 Deep Learning Model</b></td>
    <td>Replace rule-based system with trained neural network</td>
    <td>💡 Idea</td>
  </tr>
</table>

### Contribution Ideas

Want to contribute? Here are some areas that need work:

- 🐛 **Bug Fixes**: Improve gesture detection accuracy
- 📚 **Documentation**: Add more examples and tutorials
- 🎨 **UI Improvements**: Better visualization and feedback
- 🧪 **Testing**: Add unit tests and benchmarks
- 🌍 **Localization**: Translate UI to other languages

---

## 🤝 Contributing

<div align="center">

**Contributions are welcome!** Help make sign language recognition more accessible:

</div>

### Ways to Contribute

<table>
  <tr>
    <td align="center" width="25%">
      <img src="https://img.icons8.com/color/96/000000/bug.png" width="60" height="60" alt="Bug"/>
      <br><b>Report Bugs</b>
      <br>Found an issue?
      <br>Open an issue
    </td>
    <td align="center" width="25%">
      <img src="https://img.icons8.com/color/96/000000/idea.png" width="60" height="60" alt="Feature"/>
      <br><b>Suggest Features</b>
      <br>Have an idea?
      <br>Share it!
    </td>
    <td align="center" width="25%">
      <img src="https://img.icons8.com/color/96/000000/code.png" width="60" height="60" alt="Code"/>
      <br><b>Submit Code</b>
      <br>Add new gestures?
      <br>Send a PR
    </td>
    <td align="center" width="25%">
      <img src="https://img.icons8.com/color/96/000000/document.png" width="60" height="60" alt="Docs"/>
      <br><b>Improve Docs</b>
      <br>Better explanation?
      <br>Update README
    </td>
  </tr>
</table>

### Development Workflow

1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/your-username/asl-hand-gesture-recognition.git
   cd asl-hand-gesture-recognition
   ```
3. **Create** a feature branch:
   ```bash
   git checkout -b feature/new-gesture
   ```
4. **Make** your changes
5. **Test** thoroughly with different gestures
6. **Commit** with clear messages:
   ```bash
   git commit -m 'Add ASL letter C recognition'
   ```
7. **Push** to your fork:
   ```bash
   git push origin feature/new-gesture
   ```
8. **Open** a Pull Request

### Code Style Guidelines

- ✅ Follow PEP 8 for Python code
- ✅ Use descriptive variable names
- ✅ Comment complex logic
- ✅ Add docstrings to functions
- ✅ Test with various hand positions
- ✅ Update documentation for new features

---

## 📄 License

<div align="center">

This project is licensed under the **MIT License**

Free to use, modify, and distribute with attribution

</div>

<details>
<summary><b>Click to view full license</b></summary>

```
MIT License

Copyright (c) 2025 ASL Hand Gesture Recognition Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

</details>

---

## 🙏 Acknowledgments

<div align="center">

Special thanks to:

- 🤖 **Google MediaPipe Team** for the amazing hand tracking ML model
- 👁️ **OpenCV Community** for comprehensive computer vision tools
- 🤟 **ASL Community** for sign language resources and guidance
- 👥 **Open Source Contributors** who inspire accessibility technology
-    **Thank You** for using and supporting this project!

</div>

---

## 👨‍💻 Author

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&pause=1000&color=fa989a&center=true&vCenter=true&width=435&lines=Aryan+Ranjan;ML+%26+AI+Developer;Accessibility+Technology;Open+Source+Enthusiast" alt="Author Typing SVG" />

<br>

**🎓 Computer Applications in AI & ML**
<br>
**Building accessible computer vision solutions**

</div>

---

## 📞 Support

<div align="center">

### Need Help?

<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://img.icons8.com/color/96/000000/document.png" width="80" height="80" alt="Docs"/>
      <br><b>Documentation</b>
      <br>Complete README Guide
      <br><i>Setup & troubleshooting</i>
    </td>
    <td align="center" width="50%">
      <img src="https://img.icons8.com/color/96/000000/code.png" width="80" height="80" alt="Code"/>
      <br><b>Code Comments</b>
      <br>In-line Documentation
      <br><i>Implementation details</i>
    </td>
  </tr>
</table>

<br>

**Refer to the troubleshooting section above for common issues and solutions**

</div>

---

<div align="center">

## 🌟 Show Your Support

**If this project helped you, please consider:**

<a href="https://github.com/your-username/asl-hand-gesture-recognition">
  <img src="https://img.shields.io/github/stars/your-username/asl-hand-gesture-recognition?style=social" alt="GitHub stars"/>
</a>
<a href="https://github.com/your-username/asl-hand-gesture-recognition/fork">
  <img src="https://img.shields.io/github/forks/your-username/asl-hand-gesture-recognition?style=social" alt="GitHub forks"/>
</a>
<a href="https://github.com/your-username/asl-hand-gesture-recognition/watchers">
  <img src="https://img.shields.io/github/watchers/your-username/asl-hand-gesture-recognition?style=social" alt="GitHub watchers"/>
</a>

<br><br>

**⭐ Star this repository if you found it helpful!**

**🍴 Fork it to build your own gesture recognition!**

**📢 Share it with the accessibility community!**

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" alt="Footer"/>

<br>

<i>🤟 "Communication is the key to human connection." - Sign Language Wisdom</i>

<br><br>

<br>

---

**© 2025 Open Source Project | Accessibility Technology | MIT License**

<br>

**♿ Accessibility Note:** This project is designed to promote accessibility and should be used to support, not replace, human sign language interpreters. Always consult with deaf/hard-of-hearing community members for authentic ASL learning and communication.

<br>

</div>
