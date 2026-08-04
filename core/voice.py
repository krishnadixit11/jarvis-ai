import asyncio
import os
import threading

import edge_tts
import pygame

from core.logger import JarvisLogger


class VoiceEngine:

    def __init__(self, voice="en-US-GuyNeural"):

        self.voice = voice

        self.lock = threading.Lock()

        os.makedirs("sounds", exist_ok=True)

        self.output_file = os.path.join(
            "sounds",
            "jarvis_voice.mp3"
        )

        try:

            if not pygame.mixer.get_init():

                pygame.mixer.init(
                    frequency=44100,
                    size=-16,
                    channels=2,
                    buffer=512
                )

            pygame.mixer.music.set_volume(1.0)

            JarvisLogger.success(
                "Voice Engine Initialized."
            )

        except Exception as e:

            JarvisLogger.error(
                f"Pygame Init Error : {e}"
            )

    # =====================================

    async def _generate(self, text):

        communicate = edge_tts.Communicate(

            text=text,

            voice=self.voice,

            rate="+0%",

            pitch="+0Hz"

        )

        await communicate.save(
            self.output_file
        )

    # =====================================

    def _run_async(self, text):

        try:

            asyncio.run(
                self._generate(text)
            )

        except RuntimeError:

            loop = asyncio.new_event_loop()

            asyncio.set_event_loop(loop)

            loop.run_until_complete(
                self._generate(text)
            )

            loop.close()

    # =====================================

    def speak(self, text):

        if not text:

            return

        text = str(text).strip()

        if len(text) == 0:

            return

        print(f"\nJARVIS : {text}\n")

        with self.lock:

            try:

                JarvisLogger.info(
                    f"Speaking : {text}"
                )

                if pygame.mixer.music.get_busy():

                    pygame.mixer.music.stop()

                if os.path.exists(self.output_file):

                    try:
                        os.remove(self.output_file)
                    except Exception:
                        pass

                self._run_async(text)

                pygame.mixer.music.load(
                    self.output_file
                )

                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():

                    pygame.time.wait(50)

            except Exception as e:

                JarvisLogger.error(
                    f"Voice Error : {e}"
                )

                print(
                    "Voice output unavailable."
                )

            finally:

                try:

                    pygame.mixer.music.unload()

                except Exception:

                    pass

    # =====================================

    def stop(self):

        try:

            pygame.mixer.music.stop()

        except Exception:

            pass

    # =====================================

    def set_voice(self, voice):

        self.voice = voice

        JarvisLogger.info(
            f"Voice Changed : {voice}"
        )

    # =====================================

    def set_volume(self, volume):

        try:

            volume = max(
                0.0,
                min(1.0, volume)
            )

            pygame.mixer.music.set_volume(volume)

        except Exception:

            pass

    # =====================================

    def is_speaking(self):

        try:

            return pygame.mixer.music.get_busy()

        except Exception:

            return False