from PySide6.QtCore import QObject, Signal


class JarvisSignals(QObject):

    # ==========================================
    # Assistant States
    # ==========================================

    ready = Signal()

    listening = Signal()

    thinking = Signal()

    speaking = Signal()

    shutdown = Signal()

    reset = Signal()

    # ==========================================
    # Text Updates
    # ==========================================

    status = Signal(str)

    command = Signal(str)

    ai_response = Signal(str)

    notification = Signal(str)

    error = Signal(str)

    # ==========================================
    # Progress
    # ==========================================

    progress = Signal(int)

    # ==========================================
    # Debug
    # ==========================================

    debug = Signal(str)


# Global Signal Instance

signals = JarvisSignals()