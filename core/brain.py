from core.logger import JarvisLogger


class Brain:

    def process(self, command: str):

        command = command.lower().strip()

        JarvisLogger.info(f"Processing Command : {command}")

        if "youtube" in command:
            return "OPEN_YOUTUBE"

        elif "google" in command:
            return "OPEN_google"

        elif "time" in command:
            return "GET_TIME"

        elif "date" in command:
            return "GET_DATE"

        elif "hello" in command:
            return "GREET"

        elif "who are you" in command:
            return "INTRO"

        elif command in ["exit", "quit", "stop"]:
            return "EXIT"

        return "AI_CHAT"