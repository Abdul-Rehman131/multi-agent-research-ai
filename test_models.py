import os
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY environment variable not set. Please set it in your .env file or environment.")

# Initialize client
client = genai.Client(api_key=GEMINI_API_KEY)

# List available models
print("Available Google Gemini Models:")
print("-" * 50)
for m in client.models.list():
    print(f"✓ {m.name}")
print("-" * 50)
print("✅ API connection successful!")
