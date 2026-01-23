
import cv2
import numpy as np
from deepface import DeepFace
import os
from pathlib import Path
import random
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import threading
import time

class EmotionRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emotion Recognition App")
        self.root.geometry("1200x700")
        
        # Initialize camera
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise ValueError("Unable to open camera")
        
        # Emotion to image mapping
        self.emotion_images_dir = Path("emotion_images")
        self.current_emotion = None
        self.last_emotion_time = 0
        self.emotion_change_delay = 1  # seconds before changing image
        
        # Create GUI
        self.setup_gui()
        
        # Start emotion detection thread
        self.running = True
        self.detection_thread = threading.Thread(target=self.detect_emotions, daemon=True)
        self.detection_thread.start()
        
        # Update camera feed
        self.update_camera()
        
    def setup_gui(self):
        """Setup the GUI components"""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Camera feed frame
        camera_frame = ttk.LabelFrame(main_frame, text="Camera Feed", padding="5")
        camera_frame.grid(row=0, column=0, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.camera_label = ttk.Label(camera_frame)
        self.camera_label.pack()
        
        # Emotion display frame
        emotion_frame = ttk.LabelFrame(main_frame, text="Detected Emotion", padding="5")
        emotion_frame.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.emotion_label = ttk.Label(emotion_frame, text="No emotion detected", font=("Arial", 16))
        self.emotion_label.pack(pady=10)
        
        # Image display frame
        image_frame = ttk.LabelFrame(main_frame, text="Emotion Image", padding="5")
        image_frame.grid(row=0, column=2, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.image_label = ttk.Label(image_frame, text="Waiting for emotion...")
        self.image_label.pack()
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        main_frame.rowconfigure(0, weight=1)
        
    def detect_emotions(self):
        """Continuously detect emotions from camera feed"""
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                continue
                
            try:
                # Use DeepFace to analyze emotions
                result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                
                if isinstance(result, list):
                    result = result[0]
                
                # Get dominant emotion
                emotions = result.get('emotion', {})
                if emotions:
                    dominant_emotion = max(emotions, key=emotions.get)
                    emotion_score = emotions[dominant_emotion]
                    
                    # Update emotion if confidence is high enough
                    if emotion_score > 30:  # Threshold for emotion confidence
                        self.current_emotion = dominant_emotion
                        self.update_emotion_display(dominant_emotion, emotion_score)
                        self.update_emotion_image(dominant_emotion)
                        
            except Exception as e:
                # If face detection fails, continue
                pass
            
            time.sleep(0.5)  # Check every 0.5 seconds
    
    def update_emotion_display(self, emotion, score):
        """Update the emotion label in GUI"""
        emotion_text = f"{emotion.capitalize()}\nConfidence: {score:.1f}%"
        self.emotion_label.config(text=emotion_text)
    
    def update_emotion_image(self, emotion):
        """Update the displayed image based on emotion"""
        current_time = time.time()
        
        # Only change image if enough time has passed
        if current_time - self.last_emotion_time < self.emotion_change_delay:
            return
        
        self.last_emotion_time = current_time
        
        # Get image for this emotion
        emotion_dir = self.emotion_images_dir / emotion
        if emotion_dir.exists():
            images = list(emotion_dir.glob("*.jpg")) + list(emotion_dir.glob("*.png"))
            if images:
                image_path = random.choice(images)
                self.display_image(image_path)
    
    def display_image(self, image_path):
        """Display an image in the GUI"""
        try:
            img = Image.open(image_path)
            # Resize to fit display
            img.thumbnail((400, 400), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=photo, text="")
            self.image_label.image = photo  # Keep a reference
        except Exception as e:
            print(f"Error displaying image: {e}")
    
    def update_camera(self):
        """Update the camera feed display"""
        ret, frame = self.cap.read()
        if ret:
            # Draw emotion on frame if detected
            if self.current_emotion:
                cv2.putText(frame, f"Emotion: {self.current_emotion}", 
                           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Convert to RGB for tkinter
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_pil = Image.fromarray(frame_rgb)
            frame_pil.thumbnail((400, 300), Image.Resampling.LANCZOS)
            frame_tk = ImageTk.PhotoImage(frame_pil)
            
            self.camera_label.config(image=frame_tk, text="")
            self.camera_label.image = frame_tk  # Keep a reference
        
        if self.running:
            self.root.after(30, self.update_camera)  # Update ~30 FPS
    
    def on_closing(self):
        """Handle window closing"""
        self.running = False
        self.cap.release()
        self.root.destroy()

def main():
    # Create emotion images directory structure
    emotion_images_dir = Path("emotion_images")
    emotion_images_dir.mkdir(exist_ok=True)
    
    # Create subdirectories for each emotion
    emotions = ['happy', 'sad', 'angry', 'surprise', 'fear', 'disgust', 'neutral']
    for emotion in emotions:
        (emotion_images_dir / emotion).mkdir(exist_ok=True)
    
    # Create and run the application
    root = tk.Tk()
    app = EmotionRecognitionApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
