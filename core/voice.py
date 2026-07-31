import asyncio
import os

import edge_tts
import pygame

from core.logger import JarvisLogger



class VoiceEngine:


    def __init__(
        self,
        voice="en-US-GuyNeural"
    ):

        self.voice = voice

        self.output_file = (
            "sounds/jarvis_voice.mp3"
        )


        os.makedirs(
            "sounds",
            exist_ok=True
        )



    async def _generate(self, text):

        communicate = edge_tts.Communicate(
            text,
            self.voice
        )


        await communicate.save(
            self.output_file
        )



    def speak(self, text):

        print(
            f"JARVIS : {text}"
        )


        try:


            asyncio.run(
                self._generate(text)
            )



            pygame.mixer.init()


            pygame.mixer.music.load(
                self.output_file
            )


            pygame.mixer.music.play()



            while pygame.mixer.music.get_busy():

                pygame.time.Clock().tick(10)



            pygame.mixer.quit()



        except RuntimeError:

            # Agar asyncio already running ho

            loop = asyncio.new_event_loop()

            asyncio.set_event_loop(loop)


            loop.run_until_complete(
                self._generate(text)
            )


            loop.close()



        except Exception as e:


            JarvisLogger.error(
                f"Voice Error : {e}"
            )


            print(
                "Voice output unavailable, continuing..."
            )