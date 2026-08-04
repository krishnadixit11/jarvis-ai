import os
import re
import time
import tempfile

import speech_recognition as sr
from faster_whisper import WhisperModel

from core.logger import JarvisLogger


class SpeechRecognizer:

    def __init__(self):

        JarvisLogger.info(
            "Loading Faster Whisper Model..."
        )

        try:

            self.model = WhisperModel(
                "base",
                device="cpu",
                compute_type="int8"
            )

            JarvisLogger.success(
                "Faster Whisper Loaded Successfully."
            )

        except Exception as e:

            JarvisLogger.error(
                f"Whisper Loading Error : {e}"
            )

            raise


        # =====================================
        # Speech Recognition Setup
        # =====================================

        self.recognizer = sr.Recognizer()

        self.recognizer.dynamic_energy_threshold = True

        self.recognizer.dynamic_energy_adjustment_damping = 0.15

        self.recognizer.dynamic_energy_ratio = 1.5


        self.recognizer.energy_threshold = 200

        self.recognizer.pause_threshold = 0.5

        self.recognizer.non_speaking_duration = 0.25


        self.timeout = None

        self.phrase_time_limit = 8


        # =====================================
        # Microphone Setup
        # =====================================

        try:

            self.microphone = sr.Microphone()


            JarvisLogger.info(
                "Calibrating Microphone..."
            )


            with self.microphone as source:

                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=1
                )


            JarvisLogger.success(
                "Microphone Ready."
            )


        except Exception as e:


            JarvisLogger.error(
                f"Microphone Initialization Error : {e}"
            )

            raise



        # =====================================
        # Anti Duplicate System
        # =====================================

        self.last_text = ""

        self.last_time = 0



        JarvisLogger.success(
            "Speech Engine Initialized."
        )


    # =====================================
    # Text Cleaning
    # =====================================

    def clean_text(self, text):

        if not text:

            return ""


        text = text.lower().strip()



        text = re.sub(
            r"\s+",
            " ",
            text
        )


        text = re.sub(
            r"[^\w\s]",
            "",
            text
        )



        # Empty Check

        if len(text) < 2:

            return ""



        # Too Long Sentence Protection

        if len(text.split()) > 30:

            return ""



        blacklist = [

            "thank you",

            "thanks",

            "thanks for watching",

            "you",

            "bye",

            "music",

            "subtitle",

            "foreign"

        ]



        if text in blacklist:

            return ""



        # Duplicate Protection

        current_time = time.time()


        if (

            text == self.last_text

            and

            current_time - self.last_time < 3

        ):

            return ""



        self.last_text = text

        self.last_time = current_time



        return text


        # =====================================
    # Listen Function
    # =====================================

    def listen(self):

        try:

            with self.microphone as source:

                JarvisLogger.info("Listening...")

                audio = self.recognizer.listen(
                    source,
                    timeout=self.timeout,
                    phrase_time_limit=self.phrase_time_limit
                )

        except sr.WaitTimeoutError:

            return ""

        except Exception as e:

            JarvisLogger.error(
                f"Microphone Error : {e}"
            )

            return ""

        temp_path = None

        try:

            with tempfile.NamedTemporaryFile(
                suffix=".wav",
                delete=False
            ) as temp_audio:

                temp_path = temp_audio.name

                temp_audio.write(
                    audio.get_wav_data()
                )

            start = time.time()

            segments, info = self.model.transcribe(

                temp_path,

                language="en",

                beam_size=5,

                best_of=5,

                vad_filter=True,

                vad_parameters=dict(

                    min_silence_duration_ms=400,

                    speech_pad_ms=200

                )

            )

            text = ""

            for segment in segments:

                if segment.text:

                    text += segment.text + " "

            text = self.clean_text(text)

            end = time.time()

            JarvisLogger.info(

                f"Recognition Time : {round(end-start,2)} sec"

            )

            if not text:

                return ""

            JarvisLogger.success(
                f"You : {text}"
            )

            return text

        except Exception as e:

            JarvisLogger.error(
                f"Whisper Error : {e}"
            )

            return ""

        finally:

            if temp_path:

                try:

                    if os.path.exists(temp_path):

                        os.remove(temp_path)

                except Exception as e:

                    JarvisLogger.warning(
                        f"Temp File Delete Error : {e}"
                    )