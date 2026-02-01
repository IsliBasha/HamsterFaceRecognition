"""
Simpler Emotion Recognition App using FER library
Alternative version with lighter dependencies
Academic Project - Polis University
"""

import cv2
import numpy as np
from fer import FER
import tkinter as tk
from tkinter import ttk
import time
from PIL import Image, ImageTk

class SimpleEmotionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emotion Recognition App (Simple) - Polis University")
        self.root.geometry("900x600")
        
        # Initialize camera
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise ValueError("Unable to open camera")
        
        # Initialize emotion detector
        self.detector = FER(mtcnn=True)
        
        # Current emotion state
        self.current_emotion = None
        self.current_confidence = 0.0
        
        # Create GUI
        self.setup_gui()
        
        # Start emotion detection
        self.running = True
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
        emotion_frame = ttk.LabelFrame(main_frame, text="Detected Emotion", padding="20")
        emotion_frame.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Emotion label
        self.emotion_label = ttk.Label(
            emotion_frame, 
            text="No emotion detected", 
            font=("Arial", 24, "bold")
        )
        self.emotion_label.pack(pady=20)
        
        # Confidence label
        self.confidence_label = ttk.Label(
            emotion_frame, 
            text="Waiting for detection...", 
            font=("Arial", 14)
        )
        self.confidence_label.pack(pady=10)
        
        # Emotion details frame
        details_frame = ttk.LabelFrame(emotion_frame, text="Emotion Details", padding="10")
        details_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.details_text = tk.Text(
            details_frame, 
            height=10, 
            width=30, 
            font=("Arial", 10),
            wrap=tk.WORD
        )
        self.details_text.pack(fill=tk.BOTH, expand=True)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=2)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)
        
    def detect_emotion(self, frame):
        """Detect emotion in a frame"""
        try:
            emotions = self.detector.detect_emotions(frame)
            if emotions:
                # Get the first detected face's emotions
                emotion_dict = emotions[0]['emotions']
                dominant_emotion = max(emotion_dict, key=emotion_dict.get)
                emotion_score = emotion_dict[dominant_emotion] * 100
                
                # Update if confidence is high enough
                if emotion_score > 30:
                    self.current_emotion = dominant_emotion
                    self.current_confidence = emotion_score
                    self.update_emotion_display(emotion_dict)
                    
        except Exception as e:
            pass
    
    def update_emotion_display(self, emotions):
        """Update the emotion display in GUI"""
        if not emotions:
            return
            
        # Get dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        emotion_score = emotions[dominant_emotion] * 100
        
        # Update main emotion label
        emotion_text = f"{dominant_emotion.capitalize()}"
        self.emotion_label.config(text=emotion_text)
        
        # Update confidence label
        confidence_text = f"Confidence: {emotion_score:.1f}%"
        self.confidence_label.config(text=confidence_text)
        
        # Update details text
        self.details_text.delete(1.0, tk.END)
        details = "Emotion Breakdown:\n\n"
        for emotion, score in sorted(emotions.items(), key=lambda x: x[1], reverse=True):
            score_percent = score * 100
            bar_length = int(score_percent / 5)  # Scale to 20 chars max
            bar = "█" * bar_length
            details += f"{emotion.capitalize():12} {score_percent:6.1f}% {bar}\n"
        
        self.details_text.insert(1.0, details)
    
    def update_camera(self):
        """Update the camera feed display"""
        ret, frame = self.cap.read()
        if ret:
            # Detect emotions
            self.detect_emotion(frame)
            
            # Draw emotion on frame if detected
            if self.current_emotion:
                emotion_text = f"Emotion: {self.current_emotion.capitalize()}"
                confidence_text = f"Confidence: {self.current_confidence:.1f}%"
                
                # Draw background rectangle for text
                cv2.rectangle(frame, (10, 10), (400, 80), (0, 0, 0), -1)
                
                # Draw emotion text
                cv2.putText(frame, emotion_text, 
                           (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(frame, confidence_text, 
                           (15, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            # Convert to RGB for tkinter
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_pil = Image.fromarray(frame_rgb)
            frame_pil.thumbnail((600, 450), Image.Resampling.LANCZOS)
            frame_tk = ImageTk.PhotoImage(frame_pil)
            
            self.camera_label.config(image=frame_tk, text="")
            self.camera_label.image = frame_tk  # Keep a reference
        
        if self.running:
            self.root.after(100, self.update_camera)  # Update every 100ms
    
    def on_closing(self):
        """Handle window closing"""
        self.running = False
        self.cap.release()
        self.root.destroy()

def main():
    # Create and run the application
    root = tk.Tk()
    app = SimpleEmotionApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
