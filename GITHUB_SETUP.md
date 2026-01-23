# How to Upload This Project to GitHub

## Step 1: Initialize Git Repository

If you haven't already initialized git in this directory:

```bash
cd /home/lugat/Documents/aiproject
git init
```

## Step 2: Add All Files

```bash
git add .
```

This will add all files except those in `.gitignore` (like `venv/`, `emotion_images/` contents, etc.)

## Step 3: Create Initial Commit

```bash
git commit -m "Initial commit: Emotion recognition app with face detection"
```

## Step 4: Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name your repository (e.g., "emotion-recognition-app")
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

## Step 5: Connect Local Repository to GitHub

GitHub will show you commands. Use these (replace `YOUR_USERNAME` and `YOUR_REPO_NAME`):

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

## Alternative: Using SSH (if you have SSH keys set up)

```bash
git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

## What Gets Uploaded

✅ **Will be uploaded:**
- All Python source files (`main.py`, `main_simple.py`, etc.)
- `requirements.txt` and `requirements_simple.txt`
- `README.md`
- `setup_images.py`
- `run.sh`
- `.gitignore`
- Folder structure for `emotion_images/` (but not the actual images)

❌ **Will NOT be uploaded (thanks to .gitignore):**
- `venv/` - Virtual environment (too large, users should create their own)
- `emotion_images/*` - User's personal images (privacy)
- `.deepface/` - Downloaded models (too large, users should download their own)
- `__pycache__/` - Python cache files
- IDE configuration files

## Future Updates

To push future changes:

```bash
git add .
git commit -m "Description of your changes"
git push
```

## Important Notes

1. **Virtual Environment**: Users will need to create their own `venv` and install dependencies
2. **Emotion Images**: Users need to add their own images to `emotion_images/` folders
3. **Models**: DeepFace will download models automatically on first run
4. **System Dependencies**: Mention in README that `python3-tk` is needed on Linux
