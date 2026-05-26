import os
import dotenv

# Load environment variables
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv.load_dotenv(os.path.join(parent_dir, ".env"))

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
