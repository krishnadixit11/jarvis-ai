from core.voice import VoiceEngine
from core.speech import SpeechRecognizer
from core.logger import JarvisLogger
from core.brain import Brain
from core.command_router import CommandRouter

from ai.chat import ChatAI


class JarvisAssistant:

    def __init__(self):
        self.voice = VoiceEngine()
        self.listener = SpeechRecognizer()
        self.brain = Brain()
        self.router = CommandRouter()
        self.ai = ChatAI()

    def start(self):

        JarvisLogger.success("JARVIS Started Successfully")

        self.voice.speak("Hello Krishna. I am ready.")

        while True:

            command = self.listener.listen()

            if not command:
                continue

            action = self.brain.process(command)

            JarvisLogger.info(f"Action : {action}")

            if action == "EXIT":
                self.voice.speak("Goodbye Krishna. Have a nice day.")
                break

            # -----------------------------
            # AI Chat
            # -----------------------------
            if action == "AI_CHAT":

                response = self.ai.ask(command)

                if response:
                    self.voice.speak(response)

                continue

            # -----------------------------
            # Automation
            # -----------------------------
            response = self.router.execute(action)

            if response:
                self.voice.speak(response)