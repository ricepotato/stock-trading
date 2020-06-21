import logging
from PyQt5.QAxContainer import QAxWidget

log = logging.getLogger("app")


class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        log.info("Kiwoom class Start")

        self.get_ocx_instance()

    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")
