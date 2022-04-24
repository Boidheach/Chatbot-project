import pyqtgraph as pg
from src.gui.main import Ui_mwMain
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow
from src.configuration.profile import Profile


WINDOW_TITLE = "TAČR 2022: Neurosky Tool"
PLOT_TITLE = "Časový průběh vybraných metrik z čelenky Neurosky"
PLOT_X_LABEL = "Čas [s]"
PLOT_Y_LABEL = "Hodnota vybraných metrik"
LINES_COLORS = ["red", "blue", "green", "yellow", "purple", "orange", "white", "black"]


# Main window that displays the graph and
# allows the control of NeuroSky recording
class MainWindow(QMainWindow, Ui_mwMain):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(WINDOW_TITLE)
        self.controller = None
        self.connection_warning = False  # if the NeuroSky connection failed

        self.metrics_to_display = set(Profile().get_profile()['metrics_to_display'])

        # check corresponding checkboxes in
        for chb in self.gbSelectVars.findChildren(QtWidgets.QCheckBox):
            chb.clicked.connect(self.update_metrics_to_display)
            # Connect each radio button to a method to run when it's clicked
            if chb.text() in self.metrics_to_display:
                chb.setChecked(True)

        # control plotting of lines in the graph
        self.curves = dict()
        self.pens = dict()

        # GUI signal and slots
        self.pbLoad.clicked.connect(self.load_from_file)

        # load config to GUI fields
        self.leSubjectName.setText(Profile().get_profile()['subject_name'])
        condition = int(Profile().get_profile()['condition'])
        if condition == 1:
            self.rbCondition1.setChecked(True)
        elif condition == 2:
            self.rbCondition2.setChecked(True)

        self.config_plot()


    def set_controller(self, controller):
        self.controller = controller

    # Load existing NeuroSky recording from a JSON file
    def load_from_file(self):
        json_f_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a NeuroSky recording.',
                                                               Profile().get_profile()['output_dir'],
                                                               "JSON file (*.json)")
        self.controller.data_storage.load(json_f_name)

        self.lblInfo.setText("")

        # fill in the plot with loaded data
        self.clear_plot()
        self.set_plot_axes()
        self.update_plot(self.controller.data_storage.get_all_data())

    # On checkbox click, update graph with corresponding lines
    def update_metrics_to_display(self):
        selected_var = self.sender().text()
        if self.sender().isChecked():
            self.metrics_to_display.add(selected_var)
        else:
            self.metrics_to_display.remove(selected_var)
        # refresh the plot according to user's selection
        self.clear_plot()
        self.set_plot_axes()
        self.update_plot(self.controller.data_storage.get_all_data())

    # Received NeuroSky status -> update the GUI accordingly
    def set_status(self, status_text):
        if status_text == 'notscanning' and not self.connection_warning:
            self.connection_warning = True
            # self.pbStart.setEnabled(False)
            # self.pbStop.setEnabled(False)
            # self.pbSave.setEnabled(False)

            self.lblInfo.setText('<strong><font color=red>Spojení s čelenkou Neurosky bylo ztraceno.'
                                 ' Zkuste prosím restartovat čelenku'
                                 ' a případně i tuto aplikaci. V případě přetrvávajících problémů může být'
                                 ' nutné vyměnit baterie v čelence.</font></strong>')

        else:
            self.connection_warning = False
        self.statusbar.showMessage('Neurosky status: ' + status_text)

    # Prepare an empty plot ready to display the data
    def config_plot(self):
        # setup plot
        pg.setConfigOptions(antialias=True)
        styles = {'color': 'rgb(160, 160, 160)', 'font-size': '11px'}
        self.neuroskyPlot.setTitle(PLOT_TITLE)
        self.neuroskyPlot.setLabel('bottom', PLOT_X_LABEL, **styles)
        self.neuroskyPlot.setLabel('left', PLOT_Y_LABEL, **styles)

        self.neuroskyPlot.addLegend()
        self.neuroskyPlot.setBackground('w')
        self.neuroskyPlot.showGrid(x=True, y=True)

    # Prepare the data lines of the graph
    # according to the users' selection in
    # self.metrics_to_display
    def set_plot_axes(self):
        self.curves = dict()
        self.pens = dict()
        i = 0

        for metrics in self.metrics_to_display:
            self.pens[metrics] = pg.mkPen(color=LINES_COLORS[i], width=2, style=QtCore.Qt.SolidLine)
            self.curves[metrics] = self.neuroskyPlot.plot(name=metrics, pen=self.pens[metrics])
            i += 1

    # Clear the data from the graph
    def clear_plot(self):
        self.neuroskyPlot.clear()
        for key in self.curves:
            self.curves[key] = None
        for key in self.pens:
            self.pens[key] = None

    # Update the plot with new data
    # provided in all_data parameter
    def update_plot(self, all_data):
        samples_to_plot = int(Profile().get_profile()['samples_to_plot'])

        for key in self.curves:
            if self.curves[key] is None:
                self.set_plot_axes()
            if self.chbShowAllSignal.isChecked():
                self.curves[key].setData(all_data['t'], all_data[key])
            else:
                self.curves[key].setData(all_data['t'][-samples_to_plot:], all_data[key][-samples_to_plot:])

    # Display the information about
    # the data in the Info tab label
    def display_data(self, time_elapsed, data):
        # first, clear all remaining text
        text_info = "<table>"
        text_info += "<tr><td>time: </td><td>" + str(round(time_elapsed)) + " s</td></tr>\n"
        for key in sorted(data):
            text_info = text_info + "<tr><td>" + key + ": </td><td>" + str(data[key]) + "</td></tr>\n"
        text_info += "</table>"
        self.lblInfo.setText(text_info)

    # Update button enable status if recording started
    def recording_started(self):
        self.pbStart.setEnabled(False)
        self.pbStop.setEnabled(True)
        self.pbSave.setEnabled(True)

    # Update button enable status if recording stopped
    def recording_stopped(self):
        self.pbStart.setEnabled(True)
        self.pbStop.setEnabled(False)
        self.clear_plot()

        if self.chbAutosave.isChecked():
            self.pbSave.click()
        # self.pbSave.setEnabled(False)

    # Stop the recording in case of the window close
    def closeEvent(self, event):
        self.pbStop.click()

