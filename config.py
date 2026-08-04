import os
from pathlib import Path

from dotenv import load_dotenv

# =====================================================
# Load Environment Variables
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)

# =====================================================
# Helper Functions
# =====================================================

def get_env(name, default=None):

    value = os.getenv(name)

    if value is None or value == "":
        return default

    return value


def get_bool(name, default=False):

    value = str(get_env(name, default)).lower()

    return value in (
        "true",
        "1",
        "yes",
        "on"
    )


def get_int(name, default=0):

    try:
        return int(get_env(name, default))
    except Exception:
        return default


# =====================================================
# Assistant
# =====================================================

ASSISTANT_NAME = get_env(
    "ASSISTANT_NAME",
    "JARVIS"
)

USER_NAME = get_env(
    "USER_NAME",
    "Krishna"
)

# =====================================================
# AI
# =====================================================

AI_PROVIDER = get_env(
    "AI_PROVIDER",
    "OLLAMA"
)

OLLAMA_MODEL = get_env(
    "OLLAMA_MODEL",
    "qwen2.5:1.5b"
)

OLLAMA_HOST = get_env(
    "OLLAMA_HOST",
    "http://localhost:11434"
)

OPENAI_API_KEY = get_env(
    "OPENAI_API_KEY",
    ""
)

# =====================================================
# Voice
# =====================================================

VOICE = get_env(
    "VOICE",
    "en-US-GuyNeural"
)

LANGUAGE = get_env(
    "LANGUAGE",
    "en-US"
)

WAKE_WORD = get_env(
    "WAKE_WORD",
    "jarvis"
)

# =====================================================
# Whisper
# =====================================================

WHISPER_MODEL = get_env(
    "WHISPER_MODEL",
    "base"
)

# =====================================================
# Database
# =====================================================

DATABASE = get_env(
    "DATABASE",
    "database/sqlite.db"
)

# =====================================================
# Camera
# =====================================================

CAMERA_INDEX = get_int(
    "CAMERA_INDEX",
    0
)

# =====================================================
# Logging
# =====================================================

DEBUG = get_bool(
    "DEBUG",
    True
)

LOG_LEVEL = get_env(
    "LOG_LEVEL",
    "INFO"
)

# =====================================================
# Folders
# =====================================================

PHOTO_FOLDER = get_env(
    "PHOTO_FOLDER",
    "photos"
)

SCREENSHOT_FOLDER = get_env(
    "SCREENSHOT_FOLDER",
    "screenshots"
)

SOUND_FOLDER = get_env(
    "SOUND_FOLDER",
    "assets/sounds"
)

# Auto Create

os.makedirs(
    PHOTO_FOLDER,
    exist_ok=True
)

os.makedirs(
    SCREENSHOT_FOLDER,
    exist_ok=True
)

os.makedirs(
    SOUND_FOLDER,
    exist_ok=True
)

os.makedirs(
    "logs",
    exist_ok=True
)

os.makedirs(
    "database",
    exist_ok=True
)

# =====================================================
# Network
# =====================================================

REQUEST_TIMEOUT = get_int(
    "REQUEST_TIMEOUT",
    30
)

# =====================================================
# Memory
# =====================================================

MEMORY_LIMIT = get_int(
    "MEMORY_LIMIT",
    1000
)