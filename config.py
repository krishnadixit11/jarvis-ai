from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# ===========================
# Assistant Configuration
# ===========================

ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "JARVIS")
USER_NAME = os.getenv("USER_NAME", "User")

VOICE = os.getenv("VOICE", "male")
LANGUAGE = os.getenv("LANGUAGE", "en")

WAKE_WORD = os.getenv("WAKE_WORD", "jarvis")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DEBUG = os.getenv("DEBUG", "True") == "True"

DATABASE = os.getenv("DATABASE", "database/sqlite.db")