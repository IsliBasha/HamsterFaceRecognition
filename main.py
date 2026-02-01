"""
Emotion Recognition Application
Uses face recognition to detect emotions in real-time
Academic Project - Polis University
"""

import cv2
import numpy as np
from deepface import DeepFace
import tkinter as tk
from tkinter import ttk
import threading
import time
from PIL import Image, ImageTk

class EmotionRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emotion Recognition App - Polis University")
        self.root.geometry("900x600")
        
        # Initialize camera
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise ValueError("Unable to open camera")
        
        # Current emotion state
        self.current_emotion = None
        self.current_confidence = 0.0
        
        # Attention detection state
        self.attention_status = "Not looking at screen"  # "Looking at screen", "Not looking at screen"
        
        # Initialize OpenCV face and eye detectors
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        
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
        
        # Attention status frame
        attention_frame = ttk.LabelFrame(emotion_frame, text="Attention Status", padding="10")
        attention_frame.pack(fill=tk.X, pady=10)
        
        self.attention_label = ttk.Label(
            attention_frame,
            text="Not looking at screen",
            font=("Arial", 16, "bold"),
            foreground="orange"
        )
        self.attention_label.pack(pady=5)
        
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
                
                # Get emotion data
                emotions = result.get('emotion', {})
                if emotions:
                    dominant_emotion = max(emotions, key=emotions.get)
                    emotion_score = emotions[dominant_emotion]
                    
                    # Update emotion if confidence is high enough
                    if emotion_score > 30:  # Threshold for emotion confidence
                        self.current_emotion = dominant_emotion
                        self.current_confidence = emotion_score
                        self.update_emotion_display(emotions)
                        
            except Exception as e:
                # If face detection fails, continue
                pass
            
            time.sleep(0.5)  # Check every 0.5 seconds
    
    def update_emotion_display(self, emotions):
        """Update the emotion display in GUI"""
        if not emotions:
            return
            
        # Get dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        emotion_score = emotions[dominant_emotion]
        
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
            bar_length = int(score / 5)  # Scale to 20 chars max
            bar = "█" * bar_length
            details += f"{emotion.capitalize():12} {score:6.1f}% {bar}\n"
        
        self.details_text.insert(1.0, details)
    
    def detect_face_opencv(self, frame):
        """Detect face using OpenCV"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        return faces
    
    def detect_eyes_in_face(self, gray_frame, face_rect):
        """Detect eyes within a face region"""
        x, y, w, h = face_rect
        # Focus on upper half of face where eyes are typically located
        roi_gray = gray_frame[y:y+int(h*0.6), x:x+w]
        eyes = self.eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        # Adjust eye coordinates to full frame coordinates
        adjusted_eyes = [(ex + x, ey + y, ew, eh) for (ex, ey, ew, eh) in eyes]
        return adjusted_eyes
    
    def analyze_eye_gaze(self, gray_frame, eye_rect):
        """Analyze if eye is looking forward by detecting iris/pupil position"""
        ex, ey, ew, eh = eye_rect
        
        # Extract eye region
        eye_roi = gray_frame[ey:ey+eh, ex:ex+ew]
        if eye_roi.size == 0 or ew < 10 or eh < 10:
            return None
        
        # Apply Gaussian blur to reduce noise
        eye_roi_blur = cv2.GaussianBlur(eye_roi, (5, 5), 0)
        
        # Use adaptive threshold to find dark regions (pupil/iris)
        thresh = cv2.adaptiveThreshold(eye_roi_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                      cv2.THRESH_BINARY_INV, 11, 2)
        
        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contours) > 0:
            # Filter contours by area (pupil should be reasonably sized)
            min_area = (ew * eh) * 0.05  # At least 5% of eye area
            max_area = (ew * eh) * 0.4   # At most 40% of eye area
            valid_contours = [c for c in contours if min_area < cv2.contourArea(c) < max_area]
            
            if len(valid_contours) > 0:
                # Find the largest valid contour (likely the pupil)
                largest_contour = max(valid_contours, key=cv2.contourArea)
                
                # Get the center of the contour
                M = cv2.moments(largest_contour)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    
                    # Calculate offset from eye center
                    eye_center_x = ew // 2
                    eye_center_y = eh // 2
                    offset_x = cx - eye_center_x
                    offset_y = cy - eye_center_y
                    
                    # Normalize offset (as percentage of eye size)
                    offset_x_percent = (offset_x / ew) * 100 if ew > 0 else 0
                    offset_y_percent = (offset_y / eh) * 100 if eh > 0 else 0
                    
                    return (offset_x_percent, offset_y_percent)
        
        # Alternative method: find darkest point in eye region
        # This works when threshold fails
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(eye_roi_blur)
        cx, cy = min_loc  # Darkest point (likely pupil)
        
        # Calculate offset from eye center
        eye_center_x = ew // 2
        eye_center_y = eh // 2
        offset_x = cx - eye_center_x
        offset_y = cy - eye_center_y
        
        # Normalize offset
        offset_x_percent = (offset_x / ew) * 100 if ew > 0 else 0
        offset_y_percent = (offset_y / eh) * 100 if eh > 0 else 0
        
        return (offset_x_percent, offset_y_percent)
    
    def detect_attention(self, frame):
        """Detect if user is looking at screen based on eye gaze direction"""
        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Detect face
            faces = self.detect_face_opencv(frame)
            
            if len(faces) == 0:
                # No face detected - default to not looking
                self.attention_status = "Not looking at screen"
                return None
            
            # Get the largest face
            face = max(faces, key=lambda rect: rect[2] * rect[3])
            x, y, w, h = face
            
            # Detect eyes within the face
            eyes = self.detect_eyes_in_face(gray, face)
            
            if len(eyes) < 2:
                # Need at least 2 eyes for gaze detection
                self.attention_status = "Not looking at screen"
                return (face, eyes)
            
            # Analyze gaze direction for each eye
            gaze_offsets = []
            for eye in eyes[:2]:  # Use first 2 eyes detected
                gaze = self.analyze_eye_gaze(gray, eye)
                if gaze is not None:
                    gaze_offsets.append(gaze)
            
            if len(gaze_offsets) < 2:
                # Couldn't analyze both eyes
                self.attention_status = "Not looking at screen"
                return (face, eyes)
            
            # Calculate average gaze offset
            avg_offset_x = sum(g[0] for g in gaze_offsets) / len(gaze_offsets)
            avg_offset_y = sum(g[1] for g in gaze_offsets) / len(gaze_offsets)
            
            # Threshold for "looking at screen" - iris should be centered in eyes
            # If looking forward, iris should be near the center of each eye
            gaze_threshold = 15  # percent offset from eye center
            
            if abs(avg_offset_x) < gaze_threshold and abs(avg_offset_y) < gaze_threshold:
                self.attention_status = "Looking at screen"
            else:
                self.attention_status = "Not looking at screen"
            
            return (face, eyes)
                
        except Exception as e:
            # If any error occurs, default to not looking
            self.attention_status = "Not looking at screen"
            return None
    
    def update_attention_display(self):
        """Update the attention status display in GUI"""
        if self.attention_status == "Looking at screen":
            color = "green"
        else:  # Not looking at screen
            color = "orange"
        
        self.attention_label.config(
            text=self.attention_status,
            foreground=color
        )
    
    def update_camera(self):
        """Update the camera feed display"""
        ret, frame = self.cap.read()
        if ret:
            # Detect attention
            detection_result = self.detect_attention(frame)
            self.update_attention_display()
            
            # Draw face and eyes if detected
            if detection_result is not None:
                if isinstance(detection_result, tuple) and len(detection_result) == 2:
                    face_rect, eyes = detection_result
                    if face_rect is not None:
                        x, y, w, h = face_rect
                        # Draw face rectangle
                        face_color = (0, 255, 0) if self.attention_status == "Looking at screen" else (0, 165, 255)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), face_color, 2)
                        
                        # Draw eyes
                        for eye in eyes:
                            ex, ey, ew, eh = eye
                            cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
            
            # Draw attention status on frame
            if self.attention_status == "Looking at screen":
                attention_color = (0, 255, 0)  # Green
            else:  # Not looking at screen
                attention_color = (0, 165, 255)  # Orange
            
            # Draw attention status background
            cv2.rectangle(frame, (10, frame.shape[0] - 80), (400, frame.shape[0] - 10), (0, 0, 0), -1)
            cv2.putText(frame, f"Attention: {self.attention_status}", 
                       (15, frame.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, attention_color, 2)
            
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
            self.root.after(30, self.update_camera)  # Update ~30 FPS
    
    def on_closing(self):
        """Handle window closing"""
        self.running = False
        self.cap.release()
        self.root.destroy()

def main():
    # Create and run the application
    root = tk.Tk()
    app = EmotionRecognitionApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
