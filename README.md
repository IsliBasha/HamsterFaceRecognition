#  Hamster Face Recognition - Emotion Detection & Image Display

**Academic Project | Polis University**

A real-time emotion recognition application that uses advanced face recognition technology to detect human emotions from webcam feed and displays corresponding images based on the detected emotional state.

##  Project Information

- **Institution**: Polis University
- **Project Type**: Academic Project
- **Domain**: Computer Vision, Artificial Intelligence, Human-Computer Interaction
- **Technologies**: Python, Deep Learning, Computer Vision, GUI Development

##  Project Overview

**Hamster Face Recognition** is an intelligent Python application developed as an academic project for Polis University. This project demonstrates the practical application of computer vision and deep learning technologies to create an interactive emotion-based image display system. The application combines real-time video processing, facial expression analysis, and dynamic content display to showcase the capabilities of modern AI in understanding and responding to human emotions.

The project serves as a comprehensive exploration of:
- **Computer Vision**: Real-time face detection and tracking
- **Deep Learning**: Emotion recognition using pre-trained neural networks
- **Human-Computer Interaction**: Interactive GUI development
- **Software Engineering**: Modular code design and best practices

The application captures live video from a webcam, analyzes facial expressions using state-of-the-art emotion recognition models, and dynamically displays images that match the detected emotional state, creating an engaging and responsive user experience.

### Key Features

-  **Real-time Emotion Detection**: Continuous analysis of facial expressions from webcam feed
-  **Dynamic Image Display**: Shows random images from emotion-specific folders based on detected emotions
-  **User-Friendly GUI**: Clean interface with live camera feed, emotion display, and image viewer
-  **Advanced AI Models**: Uses pre-trained deep learning models for accurate emotion recognition
-  **Confidence Scoring**: Displays emotion detection confidence levels
-  **Multi-Emotion Support**: Recognizes 7 different emotions (happy, sad, angry, surprise, fear, disgust, neutral)
-  **Two Implementation Options**: Full-featured version and lightweight alternative

### Learning Objectives

This project demonstrates understanding and practical implementation of:

- **Computer Vision Fundamentals**: Image processing, face detection, and feature extraction
- **Deep Learning Applications**: Using pre-trained models for emotion classification
- **Real-time Processing**: Efficient video stream handling and frame-by-frame analysis
- **GUI Development**: Creating interactive user interfaces with Tkinter
- **Software Architecture**: Modular design, code organization, and best practices
- **AI Model Integration**: Working with TensorFlow, DeepFace, and FER libraries
- **Project Management**: Version control, documentation, and deployment

### Academic Applications

- **Computer Science Courses**: Demonstrates practical AI and computer vision concepts
- **Human-Computer Interaction**: Explores emotion-based interaction paradigms
- **Machine Learning**: Showcases real-world application of deep learning models
- **Software Engineering**: Demonstrates project structure and documentation practices
- **Research Projects**: Foundation for emotion recognition research and development

##  Repository Structure

```
HamsterFaceRecognition/
│
├── 📄 main.py                          # Main application (DeepFace version)
├── 📄 main_simple.py                   # Lightweight version (FER library)
├── 📄 requirements.txt                 # Dependencies for full version
├── 📄 requirements_simple.txt         # Dependencies for simple version
├── 📄 setup_images.py                  # Helper script to create emotion folders
├── 📄 setup_git.sh                    # Git repository setup script
├── 📄 run.sh                          # Application launcher script
├── 📄 .gitignore                      # Git ignore rules
├── 📄 README.md                       # Project documentation (this file)
├── 📄 GITHUB_SETUP.md                 # GitHub upload instructions
│
├── 📁 emotion_images/                 # Emotion-specific image folders
│   ├── happy/                         # Images displayed when happy emotion detected
│   ├── sad/                           # Images displayed when sad emotion detected
│   ├── angry/                         # Images displayed when angry emotion detected
│   ├── surprise/                      # Images displayed when surprise emotion detected
│   ├── fear/                          # Images displayed when fear emotion detected
│   ├── disgust/                       # Images displayed when disgust emotion detected
│   ├── neutral/                       # Images displayed when neutral emotion detected
│   └── .gitkeep                       # Keeps folder structure in git
│
└── 📁 venv/                           # Virtual environment (not in git)
    └── [Python packages and dependencies]
```

### File Descriptions

| File | Description |
|------|-------------|
| `main.py` | Full-featured application using DeepFace library for high-accuracy emotion detection |
| `main_simple.py` | Lightweight alternative using FER library, faster but slightly less accurate |
| `requirements.txt` | Python dependencies for the full version (DeepFace, TensorFlow, OpenCV, etc.) |
| `requirements_simple.txt` | Python dependencies for the simple version (FER, OpenCV, etc.) |
| `setup_images.py` | Utility script to create emotion image directory structure |
| `setup_git.sh` | Automated script to initialize git repository |
| `run.sh` | Convenient launcher that activates venv and runs the application |
| `.gitignore` | Excludes venv, user images, models, and cache files from version control |
| `GITHUB_SETUP.md` | Step-by-step guide for uploading project to GitHub |

##  Quick Start

### Prerequisites

- **Python 3.8+**
- **Webcam** (built-in or external)
- **Internet connection** (for first-time model download)
- **Linux**: `python3-tk` package for GUI support

### Installation

1. **Install system dependencies (Linux only):**
   ```bash
   sudo apt install python3-tk python3-venv python3-pip
   ```

2. **Clone the repository:**
   ```bash
   git clone https://github.com/IsliBasha/HamsterFaceRecognition.git
   cd HamsterFaceRecognition
   ```

3. **Choose your version and install dependencies:**

   **Option A: Full version (recommended for accuracy)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
   Uses DeepFace library. Note: First run will download pre-trained models (~500MB).

   **Option B: Simple version (lighter, faster)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements_simple.txt
   ```
   Uses FER library - lighter and faster but slightly less accurate.

4. **Set up emotion image directories:**
   ```bash
   python setup_images.py
   ```

5. **Add images to emotion folders:**
   - Place `.jpg` or `.png` images in each emotion folder
   - Example: Add happy images to `emotion_images/happy/`
   - The app will randomly select images from these folders

### Running the Application

**Using the launcher script:**
```bash
./run.sh
```

**Or manually:**
```bash
source venv/bin/activate
python main.py          # Full version
# OR
python main_simple.py   # Simple version
```

## 🎮 How It Works

### Architecture Overview

1. **Video Capture**: OpenCV captures live video frames from webcam
2. **Face Detection**: Detects faces in each frame using MTCNN or RetinaFace
3. **Emotion Analysis**: Deep learning models analyze facial expressions
4. **Emotion Classification**: Classifies into one of 7 emotion categories
5. **Image Selection**: Randomly selects image from corresponding emotion folder
6. **Display**: Updates GUI with detected emotion and selected image

### Technical Stack

- **Computer Vision**: OpenCV for video capture and image processing
- **Deep Learning**: TensorFlow/Keras for emotion recognition models
- **Face Detection**: MTCNN, RetinaFace, or OpenCV Haar Cascades
- **GUI Framework**: Tkinter for cross-platform interface
- **Image Processing**: PIL/Pillow for image manipulation and display

### Emotion Detection Models

- **Full Version**: Uses DeepFace with multiple backend models (VGG-Face, Facenet, etc.)
- **Simple Version**: Uses FER (Facial Expression Recognition) library
- **Supported Emotions**: Happy, Sad, Angry, Surprise, Fear, Disgust, Neutral

##  Configuration

### Customization Options

You can customize the application by modifying these parameters in `main.py`:

- **Emotion Confidence Threshold**: Minimum confidence to trigger emotion (default: 30%)
- **Emotion Change Delay**: Time before switching images (default: 2 seconds)
- **Camera Resolution**: Adjust video capture size
- **Image Display Size**: Control image viewer dimensions
- **Detection Frequency**: How often to analyze emotions (default: every 0.5 seconds)

### Adding Custom Emotions

To add new emotion categories:
1. Create a new folder in `emotion_images/` (e.g., `excited/`)
2. Add images to the folder
3. Update the emotion list in `main.py` or `main_simple.py`

##  Troubleshooting

| Issue | Solution |
|-------|----------|
| **Camera not opening** | Ensure no other app is using the webcam. Check camera permissions. |
| **ModuleNotFoundError: tkinter** | Install `python3-tk`: `sudo apt install python3-tk` |
| **Slow performance** | Use `main_simple.py` for faster detection, or reduce detection frequency |
| **No emotion detected** | Ensure good lighting, face camera directly, remove obstructions |
| **Model download fails** | Check internet connection. Models download on first run (~500MB) |
| **GPU not detected** | Application runs on CPU by default. GPU support requires CUDA setup |

##  Dependencies

### Full Version (`requirements.txt`)
- `opencv-python>=4.8.0` - Computer vision and video processing
- `deepface>=0.0.79` - Advanced face recognition and emotion detection
- `tensorflow>=2.13.0` - Deep learning framework
- `tf-keras>=2.20.0` - Keras for TensorFlow
- `pillow>=10.0.0` - Image processing
- `numpy>=1.24.0` - Numerical computing

### Simple Version (`requirements_simple.txt`)
- `opencv-python>=4.8.0` - Computer vision
- `fer>=22.5.0` - Facial Expression Recognition library
- `pillow>=10.0.0` - Image processing
- `numpy>=1.24.0` - Numerical computing

##  Contributing

Isli Basha
Sidrit Halili
Serxhio Lekgegaj
Helena Petro
Miken Shpati

##  Academic Context

This project was developed as part of the academic curriculum at **Polis University**. It serves as a demonstration of:

- Practical application of theoretical computer vision and AI concepts
- Integration of multiple technologies and libraries
- Software development best practices and documentation
- Real-world problem-solving using modern tools and frameworks

### Project Scope

The project encompasses:
- **Research**: Understanding emotion recognition algorithms and models
- **Implementation**: Building a functional application from scratch
- **Integration**: Combining multiple libraries and frameworks
- **Documentation**: Comprehensive documentation for academic and practical use
- **Testing**: Ensuring functionality across different environments

##  References & Resources

### Technologies Used
- **OpenCV**: Computer vision library for image and video processing
- **DeepFace**: Advanced face recognition and emotion detection framework
- **TensorFlow/Keras**: Deep learning framework for neural networks
- **FER**: Facial Expression Recognition library
- **Tkinter**: Python GUI framework

### Academic Resources
- Computer Vision and Pattern Recognition principles
- Deep Learning and Neural Network architectures
- Human-Computer Interaction design principles
- Software Engineering methodologies

##  License

This project is developed for academic purposes at Polis University and is available for educational use.

##  Acknowledgments

- **Polis University** - For providing the academic framework and support
- **DeepFace** - For advanced face recognition capabilities
- **FER** - For lightweight emotion detection
- **OpenCV** - For computer vision tools
- **TensorFlow** - For deep learning framework
- **Python Community** - For excellent libraries and documentation

##  Contact

For academic inquiries or project-related questions, please contact islibasha1@gmail.com or open an issue on GitHub.

---

**Developed for Polis University | Academic Project 2026**

**Made with ❤️ for advancing computer vision and human-computer interaction research**
