# Hamster Face Recognition - Emotion Detection System

**Academic Project | Polis University**

A real-time emotion recognition application that uses face recognition technology to detect and analyze human emotions from webcam feed. The system provides detailed emotion breakdown with confidence scores and attention detection based on eye gaze, making it perfect for understanding how computers can interpret human facial expressions.

## About This Project

This project was developed as part of my academic work at Polis University. It's a practical exploration of how computer vision and deep learning can be used to understand human emotions in real-time. The application captures video from your webcam, analyzes facial expressions, and shows you exactly what emotions it detects along with how confident it is about each one.

The project demonstrates several important concepts:
- Real-time face detection and tracking using computer vision
- Emotion recognition through pre-trained deep learning models
- Eye gaze detection for attention monitoring
- Building interactive user interfaces for displaying complex data
- Software engineering practices like modular design and proper documentation

When you run the application, it continuously analyzes your facial expressions and displays the dominant emotion it detects, along with a complete breakdown showing confidence levels for all seven emotions it can recognize: happy, sad, angry, surprise, fear, disgust, and neutral. Additionally, it monitors your attention by detecting whether you're looking at the screen based on eye gaze direction.

## Features

- **Real-time Emotion Detection**: Continuous analysis of facial expressions from webcam feed
- **Attention Detection**: Monitors eye gaze to determine if user is looking at screen
- **User-Friendly GUI**: Clean interface with live camera feed, emotion display, and attention status
- **Advanced AI Models**: Uses pre-trained deep learning models for accurate emotion recognition
- **Confidence Scoring**: Displays emotion detection confidence levels
- **Multi-Emotion Support**: Recognizes 7 different emotions (happy, sad, angry, surprise, fear, disgust, neutral)
- **Two Implementation Options**: Full-featured version and lightweight alternative

## What You'll Learn

Working with this project helps you understand:

- How computer vision processes images and video in real-time
- How deep learning models can classify emotions from facial features
- Eye gaze detection and attention monitoring techniques
- The practical challenges of working with video streams and frame-by-frame analysis
- Building user interfaces that display complex data in an understandable way
- Integrating multiple libraries and frameworks into a cohesive application
- Managing dependencies and setting up development environments

This project is particularly useful for computer science courses covering artificial intelligence, machine learning, human-computer interaction, and software engineering. It provides a hands-on way to see theoretical concepts in action.

## Project Structure

Here's what you'll find in this repository:

```
HamsterFaceRecognition/
│
├── main.py                          # Main application using DeepFace
├── main_simple.py                   # Lightweight version using FER
├── requirements.txt                 # Dependencies for full version
├── requirements_simple.txt         # Dependencies for simple version
├── setup_git.sh                    # Script to initialize git repository
├── run.sh                          # Application launcher script
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
├── GITHUB_SETUP.md                 # GitHub upload instructions
│
└── venv/                           # Virtual environment (not in git)
    └── [Python packages and dependencies]
```

### File Descriptions

- **main.py**: The full-featured version that uses DeepFace for high-accuracy emotion detection. This version provides the most detailed analysis but requires more system resources. Includes attention detection based on eye gaze.

- **main_simple.py**: A lighter alternative that uses the FER library. It's faster and uses fewer resources, making it great for testing or systems with limited capabilities.

- **requirements.txt**: Lists all the Python packages needed for the full version, including DeepFace, TensorFlow, OpenCV, and related dependencies.

- **requirements_simple.txt**: A smaller set of dependencies for the simple version, including FER, OpenCV, and basic image processing libraries.

- **run.sh**: A convenient script that activates the virtual environment and launches the application for you.

- **setup_git.sh**: Helps you set up git version control for the project.

## Getting Started

### What You Need

Before you begin, make sure you have:
- Python 3.8 or newer installed
- A webcam (built-in or external)
- An internet connection (needed the first time to download pre-trained models)
- On Linux systems: the `python3-tk` package for the GUI interface

### Installation Steps

First, install the system dependencies if you're on Linux:

```bash
sudo apt install python3-tk python3-venv python3-pip
```

Next, clone this repository to your local machine:

```bash
git clone https://github.com/IsliBasha/HamsterFaceRecognition.git
cd HamsterFaceRecognition
```

Now you need to choose which version to use. I recommend starting with the full version for the best accuracy, but the simple version works great if you want something faster or have limited system resources.

**Option A: Full Version (Recommended)**

This version uses DeepFace and provides the most accurate emotion detection:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Note: The first time you run this, it will download pre-trained models (about 500MB). This only happens once, so be patient and make sure you have a good internet connection.

**Option B: Simple Version**

This version uses FER and is lighter and faster:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements_simple.txt
```

### Running the Application

Once everything is installed, you can run the application in two ways:

**Easy way - using the launcher script:**
```bash
./run.sh
```

**Manual way:**
```bash
source venv/bin/activate
python main.py          # For full version
# OR
python main_simple.py   # For simple version
```

When the application starts, you'll see a window with your camera feed on the left and an emotion analysis panel on the right. The system will continuously analyze your facial expressions and show you what emotions it detects, along with confidence scores for each emotion. The attention detection feature will also monitor whether you're looking at the screen based on your eye gaze direction.

## How It Works

The application follows a straightforward process:

1. **Video Capture**: The application uses OpenCV to continuously capture frames from your webcam.

2. **Face Detection**: Each frame is analyzed to find faces. The system uses advanced face detection algorithms (MTCNN or RetinaFace) to locate faces in the video stream.

3. **Eye Detection**: Once a face is detected, the system locates the eyes within the face region using OpenCV's eye cascade classifier.

4. **Attention Detection**: The system analyzes the position of the iris/pupil within each eye to determine gaze direction. If both eyes are looking forward (iris centered), the user is considered to be "Looking at screen".

5. **Emotion Analysis**: Once a face is detected, deep learning models analyze the facial features to determine what emotions are present. These models have been trained on thousands of facial expressions to recognize patterns.

6. **Emotion Classification**: The system classifies the detected emotions into one of seven categories: happy, sad, angry, surprise, fear, disgust, or neutral. It also calculates confidence scores for each emotion.

7. **Data Processing**: The application processes all the emotion data, determining which emotion is most dominant and calculating confidence levels for all emotions.

8. **Display**: The GUI updates in real-time, showing the dominant emotion, its confidence score, a detailed breakdown of all emotions with visual indicators, and the current attention status.

### Technical Details

The project uses several important technologies:

- **OpenCV**: Handles all the video capture and image processing. It's the industry standard for computer vision work. Also used for face and eye detection, and eye gaze analysis.

- **Deep Learning Models**: The full version uses DeepFace, which employs multiple neural network architectures (like VGG-Face and Facenet) to achieve high accuracy. The simple version uses FER, which is optimized for speed.

- **Face Detection**: Uses MTCNN or RetinaFace algorithms to locate faces in video frames. These are state-of-the-art methods that work well even with varying lighting conditions and angles.

- **Eye Gaze Detection**: Uses OpenCV's Haar Cascade classifiers for eye detection and analyzes iris/pupil position within the eye region to determine gaze direction.

- **GUI Framework**: Built with Tkinter, which comes with Python and works across different operating systems.

- **Image Processing**: Uses PIL/Pillow for converting video frames into formats that can be displayed in the GUI.

## Customization

You can customize the application to suit your needs by modifying the code. Here are some things you might want to adjust:

- **Confidence Threshold**: Change the minimum confidence level required to display an emotion (currently set to 30%)

- **Camera Settings**: Adjust the video capture resolution or frame rate

- **Detection Frequency**: Modify how often the system analyzes emotions (currently every 0.5 seconds)

- **Attention Threshold**: Adjust the gaze detection sensitivity (currently 15% offset from eye center)

- **GUI Layout**: Change the window size, component arrangement, or how information is displayed

- **Display Format**: Customize how emotion data is presented, including the visual indicators and text formatting

All of these settings can be found and modified in the `main.py` or `main_simple.py` files.

## Troubleshooting

Here are some common issues you might encounter and how to solve them:

**Camera won't open**
- Make sure no other application is using your webcam
- Check that your camera permissions are set correctly
- Try unplugging and reconnecting external webcams

**Missing tkinter module**
- On Linux, install it with: `sudo apt install python3-tk`
- This is required for the GUI to work

**Application runs slowly**
- Try using `main_simple.py` instead of `main.py` for faster performance
- Reduce the detection frequency in the code
- Make sure you're not running too many other applications

**No emotions detected**
- Ensure you have good lighting - the system needs to see your face clearly
- Face the camera directly and make sure nothing is blocking your face
- Try moving closer to or further from the camera

**Attention detection not working**
- Make sure your face is well-lit and clearly visible
- Ensure both eyes are visible to the camera
- Try adjusting the gaze threshold in the code if detection is too sensitive or not sensitive enough

**Model download fails**
- Check your internet connection - the models need to be downloaded the first time
- The download is about 500MB, so make sure you have enough space and bandwidth
- If it fails, try running the application again - it will retry the download

**GPU not being used**
- The application runs on CPU by default, which works fine for most cases
- GPU support requires additional CUDA setup, which is beyond the scope of this project

## Dependencies

### Full Version

The full version requires these packages:

- `opencv-python` (4.8.0 or newer): Handles video capture and image processing
- `deepface` (0.0.79 or newer): Provides advanced face recognition and emotion detection
- `tensorflow` (2.13.0 or newer): The deep learning framework that powers the emotion models
- `tf-keras` (2.20.0 or newer): Keras interface for TensorFlow
- `pillow` (10.0.0 or newer): Image processing and display
- `numpy` (1.24.0 or newer): Numerical computing operations

### Simple Version

The simple version has fewer dependencies:

- `opencv-python` (4.8.0 or newer): Computer vision operations
- `fer` (22.5.0 or newer): Facial Expression Recognition library
- `pillow` (10.0.0 or newer): Image processing
- `numpy` (1.24.0 or newer): Numerical operations

## Contributing

This project was developed by:
- Isli Basha
- Sidrit Halili
- Serxhio Lekgegaj
- Helena Petro
- Miken Shpati

If you'd like to contribute to this project, we'd love to hear from you! You can:
- Report any bugs you find
- Suggest new features or improvements
- Submit pull requests with your changes
- Help improve the documentation

This is an academic project, so contributions that help with learning or research are especially welcome.

## Academic Context

This project was developed as part of coursework at Polis University. It represents a practical application of several important computer science concepts:

- Taking theoretical knowledge about computer vision and AI and applying it to solve a real problem
- Learning how to integrate multiple complex libraries and frameworks
- Understanding software development best practices through hands-on experience
- Demonstrating the ability to build, document, and deploy a complete application

The project covers multiple aspects of software development:
- Research into emotion recognition algorithms and available models
- Implementation of a working application from the ground up
- Integration of various technologies into a cohesive system
- Comprehensive documentation for both academic and practical use
- Testing and ensuring the application works across different environments

## Technologies and Resources

This project makes use of several excellent open-source tools and libraries:

- **OpenCV**: The go-to library for computer vision work, used here for video capture and image processing
- **DeepFace**: A powerful framework for face recognition and emotion detection that makes it easy to work with complex models
- **TensorFlow/Keras**: Industry-standard deep learning frameworks that power the emotion recognition models
- **FER**: A lightweight library specifically designed for facial expression recognition
- **Tkinter**: Python's built-in GUI framework, perfect for creating cross-platform interfaces

The project also draws on academic knowledge from:
- Computer Vision and Pattern Recognition research
- Deep Learning and Neural Network architectures
- Human-Computer Interaction design principles
- Software Engineering methodologies

## License

This project was developed for academic purposes at Polis University and is available for educational use.

## Acknowledgments

I'd like to thank:
- Polis University for providing the academic framework and support for this project
- The developers of DeepFace, FER, OpenCV, and TensorFlow for creating such powerful and accessible tools
- The Python community for maintaining excellent documentation and support resources

## Contact

For academic inquiries or project-related questions, please contact islibasha1@gmail.com or open an issue on GitHub.

---

**Developed for Polis University | Academic Project 2026**

**Made with ❤️ for advancing computer vision and human-computer interaction research**
