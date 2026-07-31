import os
import tempfile

import whisper
import speech_recognition as sr

from core.logger import JarvisLogger


class SpeechRecognizer:

    def __init__(self):

        JarvisLogger.info(
            "Loading Whisper Base Model..."
        )

        self.model = whisper.load_model("base")

        JarvisLogger.success(
            "Whisper Loaded Successfully."
        )


        self.recognizer = sr.Recognizer()


        self.recognizer.pause_threshold = 0.8
        self.recognizer.non_speaking_duration = 0.5
        self.recognizer.dynamic_energy_threshold = True



    def listen(self):

        try:

            with sr.Microphone() as source:

                JarvisLogger.info(
                    "Listening..."
                )


                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )


                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=8
                )


        except sr.WaitTimeoutError:

            return ""


        except Exception as e:

            JarvisLogger.error(
                f"Microphone Error: {e}"
            )

            return ""



        temp_path = None


        try:

            JarvisLogger.info(
                "Recognizing with Whisper..."
            )


            with tempfile.NamedTemporaryFile(
                suffix=".wav",
                delete=False
            ) as temp_audio:


                temp_path = temp_audio.name


                temp_audio.write(
                    audio.get_wav_data()
                )



            result = self.model.transcribe(
                temp_path,
                fp16=False
            )



            text = result["text"].strip()



            JarvisLogger.success(
                f"You : {text}"
            )


            return text.lower()



        except Exception as e:

            JarvisLogger.error(
                f"Whisper Error: {e}"
            )


            return ""



        finally:

            if temp_path and os.path.exists(temp_path):

                try:

                    os.remove(temp_path)

                except:

                    pass