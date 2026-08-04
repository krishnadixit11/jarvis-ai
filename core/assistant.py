from core.voice import VoiceEngine
from core.speech import SpeechRecognizer
from core.logger import JarvisLogger
from core.brain import Brain
from core.command_router import CommandRouter
from core.wake_word import WakeWord
from core.sound import SoundPlayer

from gui.signals import signals


class JarvisAssistant:

    def __init__(self):

        JarvisLogger.info(
            "Initializing JARVIS..."
        )

        self.voice = VoiceEngine()

        self.listener = SpeechRecognizer()

        self.brain = Brain()

        self.router = CommandRouter()

        self.wake_word = WakeWord()

        self.sound = SoundPlayer()

        self.running = True

        JarvisLogger.success(
            "JARVIS Initialized Successfully."
        )

    # =====================================
    # Main Loop
    # =====================================

    def start(self):

        JarvisLogger.success(
            "JARVIS Started Successfully"
        )

        signals.ready.emit()

        try:

            self.voice.speak(
                "Hello Krishna. I am ready."
            )

        except Exception as e:

            JarvisLogger.error(
                f"Startup Voice Error : {e}"
            )

        while self.running:

            try:

                # -----------------------------
                # Ready To Listen
                # -----------------------------

                signals.listening.emit()

                command = self.listener.listen()

                if not command:
                    continue

                # -----------------------------
                # Wake Word Detection
                # -----------------------------

                if not self.wake_word.detect(command):
                    continue

                try:
                    self.sound.play_wake()
                except Exception:
                    pass

                # Remove Wake Word

                command = command.replace(
                    "jarvis",
                    "",
                    1
                ).strip()

                # -----------------------------
                # Only Wake Word Spoken
                # -----------------------------

                if command == "":

                    try:
                        self.sound.play_listen()
                    except Exception:
                        pass

                    signals.speaking.emit()

                    self.voice.speak(
                        "Yes Krishna. I'm listening."
                    )

                    signals.listening.emit()

                    command = self.listener.listen()

                    if not command:
                        continue

                # -----------------------------
                # Thinking
                # -----------------------------

                signals.thinking.emit()

                JarvisLogger.info(
                    f"User Command : {command}"
                )

                action = self.brain.process(command)

                JarvisLogger.info(
                    f"Brain Output : {action}"
                )

                if action is None:

                    signals.ready.emit()

                    self.voice.speak(
                        "Sorry Krishna, I didn't understand."
                    )

                    continue

                # -----------------------------
                # Exit
                # -----------------------------

                if action == "EXIT":

                    signals.speaking.emit()

                    try:
                        self.sound.play_success()
                    except Exception:
                        pass

                    self.voice.speak(
                        "Goodbye Krishna. Have a nice day."
                    )

                    JarvisLogger.success(
                        "JARVIS Closed Successfully."
                    )

                    self.running = False

                    break

                # -----------------------------
                # Execute Command
                # -----------------------------

                response = None

                try:

                    response = self.router.execute(action)

                except Exception as e:

                    JarvisLogger.error(
                        f"Router Error : {e}"
                    )

                    response = (
                        "Sorry Krishna. "
                        "Something went wrong while executing your command."
                    )

                # -----------------------------
                # Speak Response
                # -----------------------------

                if response:

                    signals.speaking.emit()

                    try:
                        self.sound.play_success()
                    except Exception:
                        pass

                    try:

                        self.voice.speak(response)

                    except Exception as e:

                        JarvisLogger.error(
                            f"Voice Error : {e}"
                        )

                signals.ready.emit()

            except KeyboardInterrupt:

                JarvisLogger.info(
                    "Keyboard Interrupt Received."
                )

                self.running = False

                break

            except Exception as e:

                JarvisLogger.error(
                    f"Assistant Loop Error : {e}"
                )

                try:

                    self.voice.speak(
                        "Sorry Krishna. Something went wrong."
                    )

                except Exception:
                    pass

                signals.ready.emit()

                # -----------------------------
                # Shutdown
                # -----------------------------

                signals.ready.emit()

                JarvisLogger.success(
                    "Assistant Stopped."
                )