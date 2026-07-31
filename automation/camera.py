import cv2
import os
from datetime import datetime

from core.logger import JarvisLogger


class CameraAutomation:

    @staticmethod
    def open_camera():

        JarvisLogger.info("Opening Camera")

        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        if not cap.isOpened():
            return "Camera is not available."

        while True:

            ret, frame = cap.read()

            if not ret:
                JarvisLogger.error("Unable to read camera frame")
                break

            cv2.imshow("Jarvis Camera", frame)

            # Press Q to close camera
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        return "Camera closed."


    @staticmethod
    def take_photo():

        JarvisLogger.info("Taking Photo")

        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        if not cap.isOpened():
            return "Camera is not available."

        ret, frame = cap.read()

        if ret:

            folder = "photos"
            os.makedirs(folder, exist_ok=True)

            filename = datetime.now().strftime("%Y%m%d_%H%M%S.jpg")

            path = os.path.join(folder, filename)

            cv2.imwrite(path, frame)

            JarvisLogger.info(f"Photo saved: {path}")

            cap.release()

            return "Photo captured successfully."

        cap.release()

        return "Unable to capture photo."