from core.voice import VoiceEngine
from core.speech import SpeechRecognizer
from core.logger import JarvisLogger
from core.brain import Brain
from core.command_router import CommandRouter
from core.wake_word import WakeWord


class JarvisAssistant:

    def __init__(self):

        self.voice = VoiceEngine()

        self.listener = SpeechRecognizer()

        self.brain = Brain()

        self.router = CommandRouter()

        self.wake_word = WakeWord()


    def start(self):

        JarvisLogger.success(
            "JARVIS Started Successfully"
        )


        self.voice.speak(
            "Hello Krishna. I am ready."
        )


        while True:


            command = self.listener.listen()


            if not command:
                continue



            # =========================
            # Wake Word Check
            # =========================

            if not self.wake_word.detect(command):

                continue



            # Remove wake word

            command = command.replace(
                "jarvis",
                ""
            ).strip()



            if not command:
                self.voice.speak(
                    "Yes Krishna."
                )
                continue



            # =========================
            # Brain Processing
            # =========================

            action = self.brain.process(command)


            JarvisLogger.info(
                f"Action : {action}"
            )



            # =========================
            # Exit
            # =========================

            if action == "EXIT":

                self.voice.speak(
                    "Goodbye Krishna. Have a nice day."
                )

                break



            # =========================
            # Execute Command
            # =========================

            response = self.router.execute(action)



            if response:

                self.voice.speak(
                    response
                )