# AI Anime Generator Backend

This project is a FastAPI backend for generating anime-style images using the Waifu Diffusion model from Hugging Face.

## Features

- Exposes a `/generate` API endpoint to generate anime images from text prompts.
- Loads the model from Hugging Face at runtime (no need to upload model files).
- CORS enabled for easy frontend integration.

## Requirements

- Python 3.8+
- See `requirements.txt` for dependencies

## Running Locally

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows (Git Bash)
   # or venv\Scripts\activate.bat for Command Prompt
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the server:
   ```bash
   python main.py
   ```
4. Open [http://localhost:8000/docs](http://localhost:8000/docs) to test the API.

## Deployment

- Deploy the backend to Railway or any cloud platform that supports Python.
- The model will be downloaded from Hugging Face at runtime.

## API Usage

- `POST /generate` with a form field `prompt` (string).
- Returns a generated anime image as a PNG file.

## Example Frontend Integration

You can build a frontend (React, Next.js, etc.) and deploy it separately (e.g., on Vercel). The frontend can call this backend API to generate images.

---
