#!/bin/bash
# Git setup script for emotion recognition app

echo "Setting up Git repository..."

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Error: Git is not installed."
    echo "Please install it first with: sudo apt install git"
    exit 1
fi

# Initialize git if not already initialized
if [ ! -d .git ]; then
    echo "Initializing Git repository..."
    git init
    echo "✓ Git repository initialized"
else
    echo "✓ Git repository already exists"
fi

# Check current status
echo ""
echo "Current Git status:"
git status

echo ""
echo "Next steps:"
echo "1. Review the files to be committed (above)"
echo "2. If everything looks good, run:"
echo "   git add ."
echo "   git commit -m 'Initial commit: Emotion recognition app'"
echo ""
echo "3. Create a repository on GitHub, then run:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git"
echo "   git branch -M main"
echo "   git push -u origin main"
