import os
import time
from datetime import datetime

import cv2

from core.logger import JarvisLogger


class CameraAutomation:

    CAMERA_INDEX = 0

    # ======================================

    @staticmethod
    def open_camera():

        JarvisLogger.info(
            "Opening Camera..."
        )

        camera = None

        try:

            camera = cv2.VideoCapture(
                CameraAutomation.CAMERA_INDEX,
                cv2.CAP_DSHOW
            )

            if not camera.isOpened():

                JarvisLogger.error(
                    "Camera not found."
                )

                return "Camera is not available."

            JarvisLogger.success(
                "Camera Started."
            )

            while True:

                success, frame = camera.read()

                if not success:

                    JarvisLogger.error(
                        "Failed to read camera frame."
                    )

                    break

                cv2.imshow(
                    "JARVIS Camera",
                    frame
                )

                key = cv2.waitKey(1) & 0xFF

                if key == ord("q") or key == 27:

                    break

            return "Camera closed."

        except Exception as e:

            JarvisLogger.error(
                f"Camera Error : {e}"
            )

            return "Unable to open camera."

        finally:

            if camera is not None:

                camera.release()

            cv2.destroyAllWindows()

    # ======================================

    @staticmethod
    def take_photo():

        JarvisLogger.info(
            "Capturing Photo..."
        )

        camera = None

        try:

            camera = cv2.VideoCapture(
                CameraAutomation.CAMERA_INDEX,
                cv2.CAP_DSHOW
            )

            if not camera.isOpened():

                JarvisLogger.error(
                    "Camera not available."
                )

                return "Camera is not available."

            # Camera warm-up

            time.sleep(1)

            success, frame = camera.read()

            if not success:

                JarvisLogger.error(
                    "Unable to capture frame."
                )

                return "Unable to capture photo."

            folder = os.path.join(
                os.getcwd(),
                "photos"
            )

            os.makedirs(
                folder,
                exist_ok=True
            )

            filename = datetime.now().strftime(
                "%Y%m%d_%H%M%S.jpg"
            )

            filepath = os.path.join(
                folder,
                filename
            )

            cv2.imwrite(
                filepath,
                frame
            )

            JarvisLogger.success(
                f"Photo Saved : {filepath}"
            )

            return f"Photo captured successfully."

        except Exception as e:

            JarvisLogger.error(
                f"Photo Error : {e}"
            )

            return "Unable to capture photo."

        finally:

            if camera is not None:

                camera.release()

            cv2.destroyAllWindows()