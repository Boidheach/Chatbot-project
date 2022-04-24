import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from src.gui.MainWindow import MainWindow
from src.processing.Controller import Controller
from src.chatbot.Chatbot import Chatbot

# Main application to run
class Application:

    def __init__(self):
        app = QApplication(sys.argv)
        win = MainWindow()
        controller = Controller(win)
        chatbot = Chatbot(win.textBrowser, controller.reader.pn)

        win.show()
        sys.exit(app.exec())


if __name__ == "__main__":
    app = Application()
