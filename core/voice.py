import asyncio
import edge_tts
import os
import pygame


class VoiceEngine:

    def __init__(self, voice="en-US-GuyNeural"):
        self.voice = voice
        self.output_file = "sounds/jarvis_voice.mp3"

    async def _generate(self, text):
        communicate = edge_tts.Communicate(text, self.voice)
        await communicate.save(self.output_file)

    def speak(self, text):
        print(f"JARVIS : {text}")

        os.makedirs("sounds", exist_ok=True)

        asyncio.run(self._generate(text))

        pygame.mixer.init()
        pygame.mixer.music.load(self.output_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

        pygame.mixer.quit()