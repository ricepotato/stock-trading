import sys
import logging
from PyQt5.QtWidgets import QApplication
from kiwoom.kiwoom import Kiwoom

log = logging.getLogger("app")
log.addHandler(logging.StreamHandler())
log.setLevel(logging.INFO)


class Main:
    def __init__(self):
        log.info("Main() Start")

        self.app = QApplication(sys.argv)
        self.kiwoom = Kiwoom()
        self.app.exec_()


if __name__ == "__main__":
    Main()
