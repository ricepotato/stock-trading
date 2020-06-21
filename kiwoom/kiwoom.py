import logging
from PyQt5.QAxContainer import QAxWidget, QEventLoop
from config.errorCode import errors

log = logging.getLogger("app")


class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        log.info("Kiwoom class Start")

        self.get_ocx_instance()
        self.event_slots()
        self.signal_login_commConnect()
        self.login_event_loop = QEventLoop()

    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot)

    def login_slot(self, err_code):
        log.info(errors(err_code[1]))
        self.login_event_loop.exit()

    def signal_login_commConnect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop.exec_()
