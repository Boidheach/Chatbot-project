# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mwMain(object):
    def setupUi(self, mwMain):
        mwMain.setObjectName("mwMain")
        mwMain.resize(1350, 692)
        self.centralwidget = QtWidgets.QWidget(mwMain)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gbControl = QtWidgets.QGroupBox(self.centralwidget)
        self.gbControl.setObjectName("gbControl")
        self.pbStart = QtWidgets.QPushButton(self.gbControl)
        self.pbStart.setGeometry(QtCore.QRect(40, 140, 91, 51))
        self.pbStart.setObjectName("pbStart")
        self.pbStop = QtWidgets.QPushButton(self.gbControl)
        self.pbStop.setEnabled(False)
        self.pbStop.setGeometry(QtCore.QRect(40, 200, 91, 51))
        self.pbStop.setObjectName("pbStop")
        self.pbSave = QtWidgets.QPushButton(self.gbControl)
        self.pbSave.setEnabled(False)
        self.pbSave.setGeometry(QtCore.QRect(170, 140, 91, 51))
        self.pbSave.setObjectName("pbSave")
        self.pbLoad = QtWidgets.QPushButton(self.gbControl)
        self.pbLoad.setGeometry(QtCore.QRect(170, 200, 91, 51))
        self.pbLoad.setObjectName("pbLoad")
        self.chbAutosave = QtWidgets.QCheckBox(self.gbControl)
        self.chbAutosave.setGeometry(QtCore.QRect(80, 100, 191, 17))
        self.chbAutosave.setChecked(True)
        self.chbAutosave.setObjectName("chbAutosave")
        self.chbShowAllSignal = QtWidgets.QCheckBox(self.gbControl)
        self.chbShowAllSignal.setGeometry(QtCore.QRect(90, 280, 131, 17))
        self.chbShowAllSignal.setChecked(True)
        self.chbShowAllSignal.setObjectName("chbShowAllSignal")
        self.leSubjectName = QtWidgets.QLineEdit(self.gbControl)
        self.leSubjectName.setGeometry(QtCore.QRect(170, 30, 131, 20))
        self.leSubjectName.setObjectName("leSubjectName")
        self.lblSubjectName = QtWidgets.QLabel(self.gbControl)
        self.lblSubjectName.setGeometry(QtCore.QRect(30, 30, 121, 16))
        self.lblSubjectName.setObjectName("lblSubjectName")
        self.rbCondition1 = QtWidgets.QRadioButton(self.gbControl)
        self.rbCondition1.setGeometry(QtCore.QRect(190, 60, 31, 17))
        self.rbCondition1.setObjectName("rbCondition1")
        self.rbCondition2 = QtWidgets.QRadioButton(self.gbControl)
        self.rbCondition2.setGeometry(QtCore.QRect(240, 60, 41, 17))
        self.rbCondition2.setObjectName("rbCondition2")
        self.lblExperimentalSetup = QtWidgets.QLabel(self.gbControl)
        self.lblExperimentalSetup.setGeometry(QtCore.QRect(20, 60, 131, 16))
        self.lblExperimentalSetup.setObjectName("lblExperimentalSetup")
        self.gridLayout.addWidget(self.gbControl, 0, 3, 1, 1)
        self.gbInfo = QtWidgets.QGroupBox(self.centralwidget)
        self.gbInfo.setObjectName("gbInfo")
        self.lblInfo = QtWidgets.QLabel(self.gbInfo)
        self.lblInfo.setGeometry(QtCore.QRect(50, 10, 221, 291))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblInfo.setFont(font)
        self.lblInfo.setText("")
        self.lblInfo.setWordWrap(True)
        self.lblInfo.setObjectName("lblInfo")
        self.gridLayout.addWidget(self.gbInfo, 0, 2, 1, 1)
        self.neuroskyPlot = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.neuroskyPlot.sizePolicy().hasHeightForWidth())
        self.neuroskyPlot.setSizePolicy(sizePolicy)
        self.neuroskyPlot.setAutoFillBackground(True)
        self.neuroskyPlot.setObjectName("neuroskyPlot")
        self.gridLayout.addWidget(self.neuroskyPlot, 1, 1, 1, 3)
        self.gbSelectVars = QtWidgets.QGroupBox(self.centralwidget)
        self.gbSelectVars.setObjectName("gbSelectVars")
        self.formLayoutWidget = QtWidgets.QWidget(self.gbSelectVars)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 30, 101, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.chbMeditation = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.chbMeditation.setObjectName("chbMeditation")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chbMeditation)
        self.chbAttention = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.chbAttention.setObjectName("chbAttention")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.chbAttention)
        self.chbBlinkStrength = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.chbBlinkStrength.setObjectName("chbBlinkStrength")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.chbBlinkStrength)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.gbSelectVars)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(50, 110, 160, 171))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.chbLowAlpha = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.chbLowAlpha.setObjectName("chbLowAlpha")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.chbLowAlpha)
        self.chHighAlpha = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.chHighAlpha.setObjectName("chHighAlpha")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.chHighAlpha)
        self.chbHighBeta = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.chbHighBeta.setObjectName("chbHighBeta")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.chbHighBeta)
        self.chbLowBeta = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.chbLowBeta.setObjectName("chbLowBeta")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chbLowBeta)
        self.chHighGamma = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.chHighGamma.setObjectName("chHighGamma")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.chHighGamma)
        self.chbLowGamma = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.chbLowGamma.setObjectName("chbLowGamma")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.chbLowGamma)
        self.chbDelta = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.chbDelta.setObjectName("chbDelta")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.chbDelta)
        self.chbTheta = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.chbTheta.setObjectName("chbTheta")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.chbTheta)
        self.gridLayout.addWidget(self.gbSelectVars, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 331, 631))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.frame, 0, 0, 2, 1)
        mwMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mwMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 21))
        self.menubar.setObjectName("menubar")
        mwMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mwMain)
        self.statusbar.setObjectName("statusbar")
        mwMain.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(mwMain)
        self.toolBar.setObjectName("toolBar")
        mwMain.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(mwMain)
        QtCore.QMetaObject.connectSlotsByName(mwMain)

    def retranslateUi(self, mwMain):
        _translate = QtCore.QCoreApplication.translate
        mwMain.setWindowTitle(_translate("mwMain", "MainWindow"))
        self.gbControl.setTitle(_translate("mwMain", "Ovl??d??n??"))
        self.pbStart.setText(_translate("mwMain", "Start"))
        self.pbStop.setText(_translate("mwMain", "Stop"))
        self.pbSave.setText(_translate("mwMain", "Ulo??it"))
        self.pbLoad.setText(_translate("mwMain", "Nahr??t"))
        self.chbAutosave.setText(_translate("mwMain", "Automatick?? ukl??d??n??"))
        self.chbShowAllSignal.setText(_translate("mwMain", "Zobrazit cel?? sign??l"))
        self.lblSubjectName.setText(_translate("mwMain", "Jm??no m????en?? osoby:"))
        self.rbCondition1.setText(_translate("mwMain", "1"))
        self.rbCondition2.setText(_translate("mwMain", "2"))
        self.lblExperimentalSetup.setText(_translate("mwMain", "Nastaven?? experimentu:"))
        self.gbInfo.setTitle(_translate("mwMain", "Info"))
        self.gbSelectVars.setTitle(_translate("mwMain", "Sledovan?? metriky"))
        self.chbMeditation.setToolTip(_translate("mwMain", "??rove?? meditace 0-100"))
        self.chbMeditation.setText(_translate("mwMain", "meditation"))
        self.chbAttention.setToolTip(_translate("mwMain", "??rove?? pozornosti 0-100"))
        self.chbAttention.setText(_translate("mwMain", "attention"))
        self.chbBlinkStrength.setToolTip(_translate("mwMain", "Intenzita mrknut?? 0-100"))
        self.chbBlinkStrength.setText(_translate("mwMain", "blinkStrength"))
        self.chbLowAlpha.setToolTip(_translate("mwMain", "Amplitude ve frekven??n??m p??smu (7.5 - 9.25Hz)"))
        self.chbLowAlpha.setText(_translate("mwMain", "lowAlpha"))
        self.chHighAlpha.setToolTip(_translate("mwMain", "Amplitude ve frekven??n??m p??smu (10 - 11.75Hz)"))
        self.chHighAlpha.setText(_translate("mwMain", "highAlpha"))
        self.chbHighBeta.setToolTip(_translate("mwMain", "Amplitude ve frekven??n??m p??smu (18 - 29.75Hz)"))
        self.chbHighBeta.setText(_translate("mwMain", "highBeta"))
        self.chbLowBeta.setToolTip(_translate("mwMain", "Amplitude ve frekven??n??m p??smu (13 - 16.75Hz)"))
        self.chbLowBeta.setText(_translate("mwMain", "lowBeta"))
        self.chHighGamma.setToolTip(_translate("mwMain", "Amplitude ve frekven??n??m p??smu  (41 - 49.75Hz)"))
        self.chHighGamma.setText(_translate("mwMain", "highGamma"))
        self.chbLowGamma.setToolTip(_translate("mwMain", "Amplitude ve frekven??n??m p??smu  (31 - 39.75Hz)"))
        self.chbLowGamma.setText(_translate("mwMain", "lowGamma"))
        self.chbDelta.setToolTip(_translate("mwMain", "Amplitude ve frekven??n??m p??smu  (0.5 - 2.75Hz)"))
        self.chbDelta.setText(_translate("mwMain", "delta"))
        self.chbTheta.setToolTip(_translate("mwMain", "Amplitude ve frekven??n??m p??smu  (3.5 - 6.75Hz)"))
        self.chbTheta.setText(_translate("mwMain", "theta"))
        self.toolBar.setWindowTitle(_translate("mwMain", "toolBar"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mwMain = QtWidgets.QMainWindow()
    ui = Ui_mwMain()
    ui.setupUi(mwMain)
    mwMain.show()
    sys.exit(app.exec_())
