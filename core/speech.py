import speech_recognition as sr
from core.logger import JarvisLogger


class SpeechRecognizer:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.pause_threshold = 1
        self.recognizer.energy_threshold = 300

    def listen(self):
        with sr.Microphone() as source:

            JarvisLogger.info("Listening...")

            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = self.recognizer.listen(source)

        try:
            JarvisLogger.info("Recognizing...")

            text = self.recognizer.recognize_google(audio)

            JarvisLogger.success(f"You : {text}")

            return text.lower()

        except sr.UnknownValueError:

            JarvisLogger.warning("Couldn't understand.")

            return ""

        except Exception as e:

            JarvisLogger.error(str(e))

            return ""