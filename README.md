# Emotion Recognition and Image Display Application

A Python application that uses face recognition to detect emotions in real-time and displays corresponding images based on the detected emotion.

## Features

- Real-time emotion detection from webcam feed
- Supports 7 emotions: happy, sad, angry, surprise, fear, disgust, neutral
- Displays random images from emotion-specific folders
- GUI interface with camera feed, emotion display, and image viewer
- High confidence threshold to ensure accurate emotion detection

## Requirements

- Python 3.8 or higher
- Webcam
- Internet connection (for first-time model download)

## Installation

1. **Install system dependencies (Linux only):**
   ```bash
   sudo apt install python3-tk python3-venv python3-pip
   ```
   Note: `python3-tk` is required for the GUI interface.

2. Clone or download this repository

3. Choose one of two versions:

   **Option A: Full version (more accurate, requires more resources)**
   ```bash
   pip install -r requirements.txt
   ```
   Uses DeepFace library. Note: The first time you run the application, DeepFace will download pre-trained models automatically (this may take a few minutes).

   **Option B: Simple version (lighter, faster)**
   ```bash
   pip install -r requirements_simple.txt
   ```
   Uses FER (Facial Expression Recognition) library, which is lighter and faster but slightly less accurate.

## Setup

1. Create emotion image folders:
   The application will automatically create the following folder structure:
   ```
   emotion_images/
   ├── happy/
   ├── sad/
   ├── angry/
   ├── surprise/
   ├── fear/
   ├── disgust/
   └── neutral/
   ```

2. Add images to each emotion folder:
   - Place `.jpg` or `.png` images in the corresponding emotion folders
   - The application will randomly select and display images from these folders
   - Example: Place happy images in `emotion_images/happy/`

## Usage

Run the application:

**For full version:**
```bash
python main.py
```

**For simple version:**
```bash
python main_simple.py
```

Or first set up the image directories:
```bash
python setup_images.py
```

The application will:
1. Open your webcam
2. Detect your face and analyze emotions in real-time
3. Display the detected emotion with confidence score
4. Show a random image from the corresponding emotion folder

## How It Works

1. **Face Detection**: Uses OpenCV to capture video from your webcam
2. **Emotion Recognition**: Uses DeepFace library with pre-trained deep learning models to analyze facial expressions
3. **Image Display**: When an emotion is detected with sufficient confidence (>30%), it displays a random image from that emotion's folder

## Troubleshooting

- **Camera not opening**: Make sure no other application is using your webcam
- **Slow performance**: The emotion detection runs every 0.5 seconds to balance performance and responsiveness
- **No emotion detected**: Ensure good lighting and face the camera directly
- **Model download issues**: Make sure you have an internet connection for the first run

## Customization

You can customize the application by:
- Adjusting the emotion confidence threshold (currently 30%) in `main.py`
- Changing the emotion change delay (currently 2 seconds) in `main.py`
- Modifying the camera feed size or image display size
- Adding more emotions or changing the emotion categories

## License

This project is open source and available for personal and educational use.
