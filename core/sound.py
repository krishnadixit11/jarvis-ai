import os
import pygame

from core.logger import JarvisLogger


class SoundPlayer:

    def __init__(self):

        self.enabled = False

        self.wake = None
        self.listen = None
        self.success = None

        try:

            if not pygame.mixer.get_init():

                pygame.mixer.init(
                    frequency=44100,
                    size=-16,
                    channels=2,
                    buffer=512
                )

            self.base_path = os.path.join(
                os.getcwd(),
                "assets",
                "sounds"
            )

            self.wake = self.load_sound(
                "wake.wav"
            )

            self.listen = self.load_sound(
                "listen.wav"
            )

            self.success = self.load_sound(
                "success.wav"
            )

            self.enabled = True

            JarvisLogger.success(
                "Sound Engine Initialized."
            )

        except Exception as e:

            JarvisLogger.error(
                f"Sound Engine Error : {e}"
            )

    # =====================================================

    def load_sound(self, filename):

        path = os.path.join(
            self.base_path,
            filename
        )

        if not os.path.exists(path):

            JarvisLogger.warning(
                f"Missing sound : {filename}"
            )

            return None

        try:

            sound = pygame.mixer.Sound(path)

            sound.set_volume(0.8)

            return sound

        except Exception as e:

            JarvisLogger.error(
                f"Failed to load {filename} : {e}"
            )

            return None

    # =====================================================

    def play(self, sound):

        if not self.enabled:
            return

        if sound is None:
            return

        try:

            sound.stop()

            sound.play()

        except Exception as e:

            JarvisLogger.error(
                f"Sound Play Error : {e}"
            )

    # =====================================================

    def play_wake(self):

        self.play(self.wake)

    # =====================================================

    def play_listen(self):

        self.play(self.listen)

    # =====================================================

    def play_success(self):

        self.play(self.success)

    # =====================================================

    def stop_all(self):

        try:

            pygame.mixer.stop()

        except Exception:

            pass

    # =====================================================

    def set_volume(self, volume):

        volume = max(
            0.0,
            min(
                1.0,
                volume
            )
        )

        for sound in [

            self.wake,
            self.listen,
            self.success

        ]:

            if sound:

                sound.set_volume(volume)

    # =====================================================

    def shutdown(self):

        try:

            self.stop_all()

            pygame.mixer.quit()

        except Exception:

            pass