from src.data.NeuroskyDataStorage import NeuroskyDataStorage
from src.data.NeuroskyReader import NeuroskyReader
from src.configuration.profile import Profile


# Ensure connection of the data (receiving + storing) with the GUI
class Controller:
    def __init__(self, gui):
        self.gui = gui
        self.gui.set_controller(self)
        self.data_storage = NeuroskyDataStorage()
        self.connect_signal_slots()
        self.reader = NeuroskyReader(self)

    def connect_signal_slots(self):
        # GUI actions
        self.gui.pbStart.clicked.connect(self.start_recording)
        self.gui.pbStop.clicked.connect(self.pause_recording)
        self.gui.pbSave.clicked.connect(self.data_storage.save)
        self.gui.leSubjectName.textChanged[str].connect(self.update_subject_name)
        self.gui.rbCondition1.clicked.connect(lambda: self.update_condition('1'))
        self.gui.rbCondition2.clicked.connect(lambda: self.update_condition('2'))


    def start_recording(self):
        self.data_storage.clear()
        self.gui.clear_plot()
        self.gui.set_plot_axes()
        self.gui.recording_started()

        if not self.reader.isRunning():
            self.reader.start()
        else:
            self.reader.set_pause(False)

    def pause_recording(self):
        self.reader.set_pause(True)
        self.gui.recording_stopped()

    # When a new data sample is received, it is:
    # - appended to the data storage
    # - displayed in the GUI (plot + info label)
    def receive_data(self, time_elapsed, data):
        print(data)
        self.data_storage.append(time_elapsed, data)
        self.gui.update_plot(self.data_storage.get_all_data())
        self.gui.display_data(time_elapsed, data)

    def update_subject_name(self, sn_text):
        # first, keep only alphanumeric characters
        # to have a valid filename
        sn_text_an = "".join(x for x in sn_text if x.isalnum())
        Profile().write('subject_name', sn_text_an)

    def update_condition(self, condition):
        Profile().write('condition', condition)
