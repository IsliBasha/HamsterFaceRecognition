"""
Helper script to set up emotion image directories
"""

from pathlib import Path

def setup_emotion_directories():
    """Create emotion image directories"""
    emotion_images_dir = Path("emotion_images")
    emotion_images_dir.mkdir(exist_ok=True)
    
    emotions = ['happy', 'sad', 'angry', 'surprise', 'fear', 'disgust', 'neutral']
    
    print("Creating emotion image directories...")
    for emotion in emotions:
        emotion_dir = emotion_images_dir / emotion
        emotion_dir.mkdir(exist_ok=True)
        print(f"  ✓ Created: {emotion_dir}")
    
    print("\nSetup complete!")
    print("\nNext steps:")
    print("1. Add .jpg or .png images to each emotion folder")
    print("2. Example: Place happy images in 'emotion_images/happy/'")
    print("3. Run the application with: python main.py")

if __name__ == "__main__":
    setup_emotion_directories()
