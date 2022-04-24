from src.pyneuro.PyNeuro import PyNeuro
from time import sleep
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from src.configuration.profile import Profile
from datetime import datetime


# Reads the data from NeuroSky headset and
# sends them to the controller to save and display
class NeuroskyReader(QtCore.QThread):

    # Signals for sending the data (single sample, multiple
    # observed variables
    set_neurosky_metrics = pyqtSignal(float, dict)
    set_status = pyqtSignal(object)

    def __init__(self, controller):
        super(NeuroskyReader, self).__init__()
        self.controller = controller
        self.pn = PyNeuro()

        self.neurosky_msg = dict()
        self.updated = False
        self.pause = False
        self.timestamp_start = None

        # connect NeuroSky reader signal and slots
        self.set_neurosky_metrics.connect(self.controller.receive_data)
        self.set_status.connect(self.controller.gui.set_status)

        self.pn.connect()
        self.terminated = False

    def run(self):
        self.pn.start()

        # Callback activates when new data are received
        self.pn.set_attention_callback(self.update_all)
        self.pn.set_meditation_callback(self.update_all)
        self.pn.set_blinkStrength_callback(self.update_all)

        # Timestamp to measure the starting time of recording
        self.timestamp_start = datetime.now()

        while not self.terminated:
            if self.updated and not self.pause and self.pn.status == 'connected':
                self.updated = False
                timestamp_curr = datetime.now()
                timestamp_diff = timestamp_curr - self.timestamp_start  # Actual time from start
                # Send the data
                self.set_neurosky_metrics.emit(timestamp_diff.total_seconds(), self.neurosky_msg)
            # Send the status (transmitted in all cases)
            self.set_status.emit(self.pn.status)
            sleep(0.01)
        self.pn.close()

    # If paused (= new data ignored temporarily),
    # update the starting timestamp
    def set_pause(self, pause):
        self.pause = pause

        if not self.pause:
            self.timestamp_start = datetime.now()

    # No matter what data has been received, update
    # all collected variables in the data package to be sent
    def update_all(self, new_value):
        all_metrics = Profile().get_profile()['collected_metrics']

        for metrics in all_metrics:
            self.neurosky_msg[metrics] = getattr(self.pn, metrics)

        self.updated = True
