"""
==========================================
JARVIS AI - Global Settings
==========================================
Modify values here to configure JARVIS.
"""

# ==========================================
# Assistant
# ==========================================

ASSISTANT_NAME = "Jarvis"

USER_NAME = "Krishna"

LANGUAGE = "en"

# ==========================================
# Wake Word
# ==========================================

WAKE_WORD = "jarvis"

WAKE_WORD_ALIASES = [

    "jarvis",
    "hey jarvis",
    "hello jarvis",
    "hi jarvis",

]

# ==========================================
# Whisper
# ==========================================

WHISPER_MODEL = "base"

WHISPER_DEVICE = "cpu"

WHISPER_COMPUTE_TYPE = "int8"

# ==========================================
# Speech Recognition
# ==========================================

MIC_DEVICE = None

ENERGY_THRESHOLD = 200

DYNAMIC_ENERGY = True

DYNAMIC_RATIO = 1.5

DYNAMIC_DAMPING = 0.15

PAUSE_THRESHOLD = 0.5

NON_SPEAKING_DURATION = 0.25

PHRASE_TIME_LIMIT = 5

AMBIENT_DURATION = 0.8

LISTEN_TIMEOUT = 5

MAX_COMMAND_WORDS = 15

# ==========================================
# Voice
# ==========================================

VOICE = "en-US-GuyNeural"

VOICE_RATE = "+0%"

VOICE_VOLUME = "+0%"

VOICE_PITCH = "+0Hz"

VOICE_OUTPUT = "sounds/jarvis_voice.mp3"

# ==========================================
# GUI
# ==========================================

WINDOW_TITLE = "JARVIS AI"

WINDOW_WIDTH = 420

WINDOW_HEIGHT = 520

FPS = 60

# ==========================================
# Sounds
# ==========================================

SOUND_FOLDER = "assets/sounds"

WAKE_SOUND = "wake.wav"

LISTEN_SOUND = "listen.wav"

SUCCESS_SOUND = "success.wav"

ERROR_SOUND = "error.wav"

# ==========================================
# Screenshot
# ==========================================

SCREENSHOT_FOLDER = "screenshots"

# ==========================================
# Camera
# ==========================================

PHOTO_FOLDER = "photos"

# ==========================================
# Memory
# ==========================================

MEMORY_FOLDER = "memory"

MEMORY_FILE = "memory.json"

# ==========================================
# AI
# ==========================================

OLLAMA_MODEL = "qwen2.5:1.5b"

OLLAMA_HOST = "http://localhost:11434"

AI_TIMEOUT = 120

# ==========================================
# Logging
# ==========================================

ENABLE_LOGGING = True

LOG_LEVEL = "INFO"

LOG_FILE = "logs/jarvis.log"

# ==========================================
# Debug
# ==========================================

DEBUG = False