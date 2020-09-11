# Selected Problems in Biosignal Processing

# Project on human ECG and PPG measurement

# Elisabeth Otte, Alexander Resch, Ali Sadr

# Last changed: 21.07.2015

#------------------------------------------------------------------------------

# Importing packages



from PyQt4 import QtCore, QtGui

import sys

from pyqtgraph import PlotWidget

from scipy.io import loadmat, savemat

import numpy as np

import scipy.signal as signal

import copy as copy

import datetime as dt



# Creating variables



filepath = " "



Combobox_list = []

ECG_peaks = []

ECG_peaks_nan = []

Patient = []

Patient_ECG = []

Patient_PPG = []

PPG_peaks = []

PPG_peaks_nan = []

time = []



Loop_Time = 0

Max_ECG = 0

Max_PPG = 0

Min_ECG = 0

Min_PPG = 0

ptt = 0

test = 0

time_ecg = 0

time_ppg = 0 



i_ECG = 1

i_PPG = 1



ECG_startpoint = 6000

PPG_startpoint = 6000



Bandpass_flag = False

Bandstop_flag = False

Cutoff_flag = False

ECG_Filtered_flag = False

ECG_RAW_flag = False

Highpass_flag = False

Lowpass_flag = False

PPG_Filtered_flag = False

PPG_RAW_flag = False



StartStop = True





# GUI created mainly using QTDesigner, translated into Python



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'biosignal_project_v1.ui'

# Created by: PyQt4 UI code generator 4.11.4



try:

    _fromUtf8 = QtCore.QString.fromUtf8

except AttributeError:

    def _fromUtf8(s):

        return s



try:

    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):

        return QtGui.QApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):

        return QtGui.QApplication.translate(context, text, disambig)



# Graphical creation of GUI

class Ui_BioSignal(object):

    def setupUi(self, BioSignal):

        BioSignal.setObjectName(_fromUtf8("BioSignal"))

        BioSignal.resize(840, 525)

        self.centralwidget = QtGui.QWidget(BioSignal)

        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

# Play Button

        self.pushButton = QtGui.QPushButton(self.centralwidget)

        self.pushButton.setGeometry(QtCore.QRect(660, 390, 71, 21))

        self.pushButton.setObjectName(_fromUtf8("pushButton"))

# Stop Button

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)

        self.pushButton_2.setGeometry(QtCore.QRect(660, 420, 71, 21))

        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

# Save Button

        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)

        self.pushButton_3.setGeometry(QtCore.QRect(740, 390, 71, 21))

        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

# Plot Raw ECG Function Checkbox

        self.checkBox_6 = QtGui.QCheckBox(self.centralwidget)

        self.checkBox_6.setGeometry(QtCore.QRect(510, 360, 21, 16))

        self.checkBox_6.setText(_fromUtf8(""))

        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))

# Plot Filtered ECG Function Checkbox

        self.checkBox_7 = QtGui.QCheckBox(self.centralwidget)

        self.checkBox_7.setGeometry(QtCore.QRect(510, 390, 21, 16))

        self.checkBox_7.setText(_fromUtf8(""))

        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))

# Plot Raw PPG Function Checkbox

        self.checkBox_5 = QtGui.QCheckBox(self.centralwidget)

        self.checkBox_5.setGeometry(QtCore.QRect(550, 360, 21, 16))

        self.checkBox_5.setText(_fromUtf8(""))

        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))

# Create a Highpass Filter Checkbox

        self.checkBox_9 = QtGui.QCheckBox(self.centralwidget)

        self.checkBox_9.setGeometry(QtCore.QRect(50, 360, 91, 16))

        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))

# Create a Lowpass Filter Checkbox

        self.checkBox_10 = QtGui.QCheckBox(self.centralwidget)

        self.checkBox_10.setGeometry(QtCore.QRect(50, 390, 91, 16))

        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))

# Create a Bandpass Filter Checkbox

        self.checkBox_11 = QtGui.QCheckBox(self.centralwidget)

        self.checkBox_11.setGeometry(QtCore.QRect(50, 420, 91, 16))

        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))

# Create a Bandstop Filter Checkbox

        self.checkBox_12 = QtGui.QCheckBox(self.centralwidget)

        self.checkBox_12.setGeometry(QtCore.QRect(50, 450, 91, 16))

        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))

# Open File Button

        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)

        self.pushButton_4.setGeometry(QtCore.QRect(660, 330, 151, 21))

        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

# Plot Filtered PPG Function Checkbox

        self.checkBox_8 = QtGui.QCheckBox(self.centralwidget)

        self.checkBox_8.setGeometry(QtCore.QRect(550, 390, 21, 16))

        self.checkBox_8.setText(_fromUtf8(""))

        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))

# Close Button

        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)

        self.pushButton_5.setGeometry(QtCore.QRect(660, 450, 151, 31))

        self.pushButton_5.setAutoFillBackground(False)

        self.pushButton_5.setDefault(False)

        self.pushButton_5.setFlat(False)

        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

# Filters Label

        self.label = QtGui.QLabel(self.centralwidget)

        self.label.setGeometry(QtCore.QRect(70, 330, 47, 13))

        self.label.setAutoFillBackground(False)

        self.label.setObjectName(_fromUtf8("label"))

# Cutoff Frequencies Label

        self.label_2 = QtGui.QLabel(self.centralwidget)

        self.label_2.setGeometry(QtCore.QRect(280, 330, 101, 16))

        self.label_2.setObjectName(_fromUtf8("label_2"))

# Lower Cutoff Frequency Label

        self.label_3 = QtGui.QLabel(self.centralwidget)

        self.label_3.setGeometry(QtCore.QRect(220, 360, 47, 13))

        self.label_3.setObjectName(_fromUtf8("label_3"))

# Higher Cutoff Frequency Label

        self.label_4 = QtGui.QLabel(self.centralwidget)

        self.label_4.setGeometry(QtCore.QRect(220, 390, 47, 13))

        self.label_4.setObjectName(_fromUtf8("label_4"))

# Text fields to fill in Higher and Lower Cutoff Frequencies

        self.lineEdit = QtGui.QLineEdit(self.centralwidget)

        self.lineEdit.setGeometry(QtCore.QRect(270, 360, 113, 20))

        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)

        self.lineEdit_2.setGeometry(QtCore.QRect(270, 390, 113, 20))

        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

# Plot Raw Data Label

        self.label_5 = QtGui.QLabel(self.centralwidget)

        self.label_5.setGeometry(QtCore.QRect(460, 360, 47, 13))

        self.label_5.setObjectName(_fromUtf8("label_5"))

# Plot Filtered Data Label

        self.label_6 = QtGui.QLabel(self.centralwidget)

        self.label_6.setGeometry(QtCore.QRect(460, 390, 47, 13))

        self.label_6.setObjectName(_fromUtf8("label_6"))

# ECG Label

        self.label_7 = QtGui.QLabel(self.centralwidget)

        self.label_7.setGeometry(QtCore.QRect(510, 330, 21, 16))

        self.label_7.setObjectName(_fromUtf8("label_7"))

# PPG Label

        self.label_8 = QtGui.QLabel(self.centralwidget)

        self.label_8.setGeometry(QtCore.QRect(550, 330, 21, 16))

        self.label_8.setObjectName(_fromUtf8("label_8"))

# Reset Button

        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)

        self.pushButton_6.setGeometry(QtCore.QRect(740, 420, 71, 21))

        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

# ECG Plot Label

        self.label_9 = QtGui.QLabel(self.centralwidget)

        self.label_9.setGeometry(QtCore.QRect(180, 300, 47, 13))

        self.label_9.setObjectName(_fromUtf8("label_9"))

# PPG Plot Label

        self.label_10 = QtGui.QLabel(self.centralwidget)

        self.label_10.setGeometry(QtCore.QRect(600, 300, 47, 13))

        self.label_10.setObjectName(_fromUtf8("label_10"))

# ECG PLot

        self.ECG = PlotWidget(self.centralwidget)

        self.ECG.setGeometry(QtCore.QRect(20, 10, 391, 281))

        self.ECG.setObjectName(_fromUtf8("ECG"))

# PPG PLot

        self.PPG = PlotWidget(self.centralwidget)

        self.PPG.setGeometry(QtCore.QRect(430, 10, 391, 281))

        self.PPG.setObjectName(_fromUtf8("PPG"))

# Select Patients Measurement Data Combobox

        self.comboBox = QtGui.QComboBox(self.centralwidget)

        self.comboBox.setGeometry(QtCore.QRect(740, 360, 69, 22))

        self.comboBox.setObjectName(_fromUtf8("comboBox"))

# Signal Number Label

        self.label_11 = QtGui.QLabel(self.centralwidget)

        self.label_11.setGeometry(QtCore.QRect(660, 360, 71, 20))

        self.label_11.setObjectName(_fromUtf8("label_11"))

# PTT Detection Display

        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)

        self.lcdNumber.setGeometry(QtCore.QRect(350, 40, 64, 23))

        self.lcdNumber.setFrameShape(QtGui.QFrame.NoFrame)

        self.lcdNumber.setFrameShadow(QtGui.QFrame.Plain)

        self.lcdNumber.setMidLineWidth(0)

        self.lcdNumber.setSmallDecimalPoint(False)

        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))

# PTT / ms Label

        self.label_12 = QtGui.QLabel(self.centralwidget)

        self.label_12.setGeometry(QtCore.QRect(361, 10, 51, 25))

        self.label_12.setObjectName(_fromUtf8("label_12"))

        self.label_12.setStyleSheet('color: white')

# Full Window Geometries

        BioSignal.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(BioSignal)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 21))

        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.menuECG_PPG_Analysis = QtGui.QMenu(self.menubar)

        self.menuECG_PPG_Analysis.setObjectName(_fromUtf8("menuECG_PPG_Analysis"))

        BioSignal.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(BioSignal)

        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        BioSignal.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuECG_PPG_Analysis.menuAction())



# Add functionality to Buttons and Checkboxes

        self.retranslateUi(BioSignal)

# Close Button

        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), BioSignal.close)

        QtCore.QMetaObject.connectSlotsByName(BioSignal)

# Open File Button -> calls Python Function fileSelect

        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.fileSelect)

# Play Button -> calls Python Function plotData

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.plotData)

# Stop Button -> calls Python Function stopPlot

        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.stopPlot)

# Reset Button -> calls Python Function resetAll

        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.resetAll)

# Plot unfiltered ECG Signal Checkbox -> calls Python Function ECG_Raw_func

        QtCore.QObject.connect(self.checkBox_6,QtCore.SIGNAL("stateChanged(int)"),self.ECG_RAW_func)

# Plot filtered ECG Signal Checkbox -> calls Python Function ECG_Filtered_func

        QtCore.QObject.connect(self.checkBox_7,QtCore.SIGNAL("stateChanged(int)"),self.ECG_Filtered_func)

# Plot unfiltered PPG Signal Checkbox -> calls Python Function PPG_Raw_func

        QtCore.QObject.connect(self.checkBox_5,QtCore.SIGNAL("stateChanged(int)"),self.PPG_RAW_func)

# Plot filtered PPG Signal Checkbox -> calls Python Function PPG_Filtered_func

        QtCore.QObject.connect(self.checkBox_8,QtCore.SIGNAL("stateChanged(int)"),self.PPG_Filtered_func)

# Create Highpass Filter Checkbox -> calls Python Function Highpass_func

        QtCore.QObject.connect(self.checkBox_9,QtCore.SIGNAL("stateChanged(int)"),self.Highpass_func)

# Create Lowpass Filter Checkbox -> calls Python Function Lowpass_func

        QtCore.QObject.connect(self.checkBox_10,QtCore.SIGNAL("stateChanged(int)"),self.Lowpass_func)

# Create Bandpass Filter Checkbox -> calls Python Function Bandpass_func

        QtCore.QObject.connect(self.checkBox_11,QtCore.SIGNAL("stateChanged(int)"),self.Bandpass_func)

# Create Bandstop Filter Checkbox -> calls Python Function Bandstop_func

        QtCore.QObject.connect(self.checkBox_12,QtCore.SIGNAL("stateChanged(int)"),self.Bandstop_func)

# Save Button -> calls Python Function Save

        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Save)



# Name Buttons, Checkboxes and Textfields        

    def retranslateUi(self, BioSignal):

        BioSignal.setWindowTitle(_translate("BioSignal", "BioSignal", None))

        self.pushButton.setText(_translate("BioSignal", "Play", None))

        self.pushButton_2.setText(_translate("BioSignal", "Stop", None))

        self.pushButton_3.setText(_translate("BioSignal", "Save", None))

        self.checkBox_9.setText(_translate("BioSignal", "High-pass", None))

        self.checkBox_10.setText(_translate("BioSignal", "Low-pass", None))

        self.checkBox_11.setText(_translate("BioSignal", "Band-pass", None))

        self.checkBox_12.setText(_translate("BioSignal", "Band-stop", None))

        self.pushButton_4.setText(_translate("BioSignal", "Open file", None))

        self.pushButton_5.setText(_translate("BioSignal", "Close", None))

        self.label.setText(_translate("BioSignal", "Filters", None))

        self.label_2.setText(_translate("BioSignal", "Cut off frequencies", None))

        self.label_3.setText(_translate("BioSignal", "Lower", None))

        self.label_4.setText(_translate("BioSignal", "Higher", None))

        self.label_5.setText(_translate("BioSignal", "Raw", None))

        self.label_6.setText(_translate("BioSignal", "Filtered", None))

        self.label_7.setText(_translate("BioSignal", "ECG", None))

        self.label_8.setText(_translate("BioSignal", "PPG", None))

        self.pushButton_6.setText(_translate("BioSignal", "Reset", None))

        self.label_9.setText(_translate("BioSignal", "ECG plot", None))

        self.label_10.setText(_translate("BioSignal", "PPG plot", None))

        self.label_11.setText(_translate("BioSignal", "Signal number:", None))

        self.label_12.setText(_translate("BioSignal", "PTT / ms", None))

        self.menuECG_PPG_Analysis.setTitle(_translate("BioSignal", "ECG PPG Analysis", None))



# Definition of Python functions



# Open  the file of a patient and loading the data    

    def fileSelect(self):

# Importing global variables

        global filepath, Patient, Combobox_list

# Open a new window to select files - only .mat files will be shown

        self.comboBox.clear()        

        dialog = QtGui.QFileDialog(None,"Open File", None,"Mat-files (*.mat)")

        dialog.exec_()

        for file in dialog.selectedFiles():

            filepath = file    

 # Import selected File and save data in coresponding variables            

        Patient = loadmat(filepath)

        Data_blocks = Patient.keys()

        Data_blocks.sort()

        Combobox_list = [0]*(len(Data_blocks)/2)        

        for i in range(0,len(Data_blocks)/2):

            if len(Data_blocks[i]) == 12:

                Combobox_list[int(Data_blocks[i][10:12])-1]=Patient[Data_blocks[i]]

            else:

                Combobox_list[int(Data_blocks[i][10:11])-1]=Patient[Data_blocks[i]]

            self.comboBox.addItem(str(i+1))

            

# Filtering Data, Detecting Peaks, Plotting ECG and PPG and Calculation of PTT            

    def plotData(self):

# Importing global variables

        global Combobox_list, i_ECG, i_PPG, StartStop, Patient_ECG, Patient_PPG, ECG_peaks, PPG_peaks

        global ECG_RAW_flag, ECG_Filtered_flag, PPG_RAW_flag, PPG_Filtered_flag

        global Highpass_flag, Lowpass_flag, Bandpass_flag, Bandstop_flag, Cutoff_flag

        global ECG_startpoint, PPG_startpoint, ptt, time_ppg, time_ecg, PPG_peaks_nan, ECG_peaks_nan
        
        global Max_ECG, Min_ECG, Max_PPG, Min_PPG, Loop_Time

# Error Message if no file is selected        

        if len(Combobox_list) == 0:

            QtGui.QMessageBox.critical(None, 'Error',

            "Please select patient's file", QtGui.QMessageBox.Ok)

# Loading data and time from patients variables

        else:            

            Patient_ECG = Combobox_list[self.comboBox.currentIndex()][0]

            Patient_PPG = Combobox_list[self.comboBox.currentIndex()][1]  

            Patient_ECG = Patient_ECG[ECG_startpoint:len(Patient_ECG)]

            Patient_PPG = Patient_PPG[PPG_startpoint:len(Patient_PPG)]               

            x_ECG = Patient['ticktimes_block'+str(self.comboBox.currentIndex()+1)][0][ECG_startpoint:len(Patient_ECG)]

            x_PPG = Patient['ticktimes_block'+str(self.comboBox.currentIndex()+1)][0][PPG_startpoint:len(Patient_PPG)]

            StartStop = True

# Checking the filter type and loading the cutoff frequencies. Error Message, if not enough data is given.

            if self.checkBox_9.isChecked():                  

                if (self.lineEdit.text() == ''):

                    QtGui.QMessageBox.critical(None, 'Error',

                    "Please enter the lower cut-off frequency", QtGui.QMessageBox.Ok)

                    StartStop = False

                else:

                    Low_cutoff = float(self.lineEdit.text())

                    Cutoff_flag = True

            elif self.checkBox_10.isChecked():

                if (self.lineEdit_2.text() == ''):

                    QtGui.QMessageBox.critical(None, 'Error',

                    "Please enter the higher cut-off frequency", QtGui.QMessageBox.Ok)

                    StartStop = False

                else:

                    High_cutoff = float(self.lineEdit_2.text())

                    Cutoff_flag = True

            elif self.checkBox_11.isChecked():

                if (self.lineEdit.text() == ''):

                    QtGui.QMessageBox.critical(None, 'Error',

                    "Please enter the lower cut-off frequency", QtGui.QMessageBox.Ok)

                    StartStop = False

                elif (self.lineEdit_2.text() == ''):

                    QtGui.QMessageBox.critical(None, 'Error',

                    "Please enter the higher cut-off frequency", QtGui.QMessageBox.Ok)

                    StartStop = False

                else:

                    Low_cutoff = float(self.lineEdit.text())

                    High_cutoff = float(self.lineEdit_2.text())

                    Cutoff_flag = True

            elif self.checkBox_12.isChecked():

                if (self.lineEdit.text() == ''):

                    QtGui.QMessageBox.critical(None, 'Error',

                    "Please enter the lower cut-off frequency", QtGui.QMessageBox.Ok)

                    StartStop = False

                elif (self.lineEdit_2.text() == ''):

                    QtGui.QMessageBox.critical(None, 'Error',

                    "Please enter the higher cut-off frequency", QtGui.QMessageBox.Ok)

                    StartStop = False

                else:

                    Low_cutoff = float(self.lineEdit.text())

                    High_cutoff = float(self.lineEdit_2.text())

                    Cutoff_flag = True

            else:

                Low_cutoff = 0.5

                High_cutoff = 48

# Check if filtered or unifltered signal should be plottet. Error message, if not enough information                

            if not(self.checkBox_6.isChecked()) and not(self.checkBox_7.isChecked()):

                QtGui.QMessageBox.critical(None, 'Error',

                    "Please select raw or filtered ECG to plot", QtGui.QMessageBox.Ok)

                StartStop = False

            elif not(self.checkBox_5.isChecked()) and not(self.checkBox_8.isChecked()):

                QtGui.QMessageBox.critical(None, 'Error',

                    "Please select raw or filtered PPG to plot", QtGui.QMessageBox.Ok)

                StartStop = False

# Creation of the Highpass Filter and filtering of the chosen signals

            elif self.checkBox_9.isChecked():

                if ECG_Filtered_flag == 1 and Cutoff_flag:

                    fir2 = signal.firwin(801, Low_cutoff*np.pi*2, pass_zero=False,nyq=(2*np.pi*500.0))

                    ECG_conv = np.convolve(fir2, Patient_ECG, 'same')

                    ECG_conv = ECG_conv[::-1]

                    ECG_conv = np.convolve(fir2, ECG_conv, 'same')

                    Patient_ECG = ECG_conv[::-1]

                if PPG_Filtered_flag == 1 and Cutoff_flag:

                    fir2 = signal.firwin(801, Low_cutoff*np.pi*2, pass_zero=False,nyq=(2*np.pi*500.0))

                    PPG_conv = np.convolve(fir2, Patient_PPG, 'same')

                    PPG_conv = PPG_conv[::-1]

                    PPG_conv = np.convolve(fir2, PPG_conv, 'same')

                    Patient_PPG = PPG_conv[::-1]

# Creation of the Lowpass Filter and filtering of the chosen signals

            elif self.checkBox_10.isChecked():

                if ECG_Filtered_flag == 1 and Cutoff_flag:

                    fir2 = signal.firwin(800, High_cutoff*np.pi*2, nyq=(2*np.pi*500.0))
                    ECG_conv = np.convolve(fir2, Patient_ECG, 'same')
                    ECG_conv = ECG_conv[::-1]
                    ECG_conv = np.convolve(fir2, ECG_conv, 'same')
                    Patient_ECG = ECG_conv[::-1]

                if PPG_Filtered_flag == 1 and Cutoff_flag:

                    fir2 = signal.firwin(800, High_cutoff*np.pi*2, nyq=(2*np.pi*500.0))

                    PPG_conv = np.convolve(fir2, Patient_PPG, 'same')

                    PPG_conv = PPG_conv[::-1]

                    PPG_conv = np.convolve(fir2, PPG_conv, 'same')

                    Patient_PPG = PPG_conv[::-1]

# Creation of the Bandpass Filter and filtering of the chosen signals                    

            elif self.checkBox_11.isChecked():

                if ECG_Filtered_flag == 1 and Cutoff_flag:

                    fir2 = signal.firwin(800, [Low_cutoff*np.pi*2, High_cutoff*np.pi*2], pass_zero=False,nyq=(2*np.pi*500.0))

                    ECG_conv = np.convolve(fir2, Patient_ECG, 'same')

                    ECG_conv = ECG_conv[::-1]

                    ECG_conv = np.convolve(fir2, ECG_conv, 'same')

                    Patient_ECG = ECG_conv[::-1]

                if PPG_Filtered_flag == 1 and Cutoff_flag:

                    fir2 = signal.firwin(800, [Low_cutoff*np.pi*2, High_cutoff*np.pi*2], pass_zero=False,nyq=(2*np.pi*500.0))

                    PPG_conv = np.convolve(fir2, Patient_PPG, 'same')

                    PPG_conv = PPG_conv[::-1]

                    PPG_conv = np.convolve(fir2, PPG_conv, 'same')

                    Patient_PPG = PPG_conv[::-1]

# Creation of the Bandstop Filter and filtering of the chosen signals                    

            elif self.checkBox_12.isChecked():

                if ECG_Filtered_flag == 1 and Cutoff_flag:

                    fir2 = signal.firwin(801, [Low_cutoff*np.pi*2, High_cutoff*np.pi*2], nyq=(2*np.pi*500.0))

                    ECG_conv = np.convolve(fir2, Patient_ECG, 'same')

                    ECG_conv = ECG_conv[::-1]

                    ECG_conv = np.convolve(fir2, ECG_conv, 'same')

                    Patient_ECG = ECG_conv[::-1]

                if PPG_Filtered_flag == 1 and Cutoff_flag:

                    fir2 = signal.firwin(801, [Low_cutoff*np.pi*2, High_cutoff*np.pi*2], nyq=(2*np.pi*500.0))

                    PPG_conv = np.convolve(fir2, Patient_PPG, 'same')

                    PPG_conv = PPG_conv[::-1]

                    PPG_conv = np.convolve(fir2, PPG_conv, 'same')

                    Patient_PPG = PPG_conv[::-1]

# Error message if no type of filter is selected

            elif self.checkBox_7.isChecked() and self.checkBox_8.isChecked():                   

                QtGui.QMessageBox.critical(None, 'Error',

                "Please select a filter", QtGui.QMessageBox.Ok)

                StartStop = False

     

# Detecting peaks (Variable with zeroes for save function, variable with nan for plotting purposes)

# Peaks in ECG Signal

            ECG_peaks = np.zeros(len(Patient_ECG))    

            for i in range(1,len(Patient_ECG)-1):
                
                if i==1:
                    Div_res_ecg = divmod(0,1000)
                else:
                    Div_res_ecg = divmod(i,1000)
                    
                if Div_res_ecg[1]==0:
                    Max_ECG = Patient_ECG[Div_res_ecg[0]*1000:Div_res_ecg[0]*1000+1000].max()                    

                if Patient_ECG[i-1]<Patient_ECG[i] and Patient_ECG[i+1]<Patient_ECG[i]:

                    if Patient_ECG[i]> 0.7*Max_ECG:    

                        ECG_peaks[i] = Patient_ECG[i]

            ECG_peaks_nan = copy.copy(ECG_peaks)

            ECG_peaks_nan[ECG_peaks_nan == 0] = np.nan

# Error Message, if filter setting doesn't allow the detection of datapeaks

            if  ECG_peaks.max() == 0:

                QtGui.QMessageBox.critical(None, 'Error',

                "No peaks detected, please adjust filter.", QtGui.QMessageBox.Ok)

                StartStop = False

# Peaks in PPG Signal            

            PPG_peaks = np.zeros(len(Patient_PPG))    

            for i in range(1,len(Patient_PPG)-1):
                
                if i==1:
                    Div_res_ppg = divmod(0,1000)
                else:
                    Div_res_ppg = divmod(i,1000)
                    
                if Div_res_ppg[1]==0:
                    Max_PPG = Patient_PPG[Div_res_ppg[0]*1000:Div_res_ppg[0]*1000+1000].max()

                if Patient_PPG[i-1]<Patient_PPG[i] and Patient_PPG[i+1]<Patient_PPG[i]:

                    if Patient_PPG[i]> 0.7*Max_PPG:    

                        PPG_peaks[i] = Patient_PPG[i]

            PPG_peaks_nan = copy.copy(PPG_peaks)

            PPG_peaks_nan[PPG_peaks_nan == 0] = np.nan

# Error Message, if filter setting doesn't allow the detection of datapeaks

            if PPG_peaks.max() == 0:

                QtGui.QMessageBox.critical(None, 'Error',

                "No peaks detected, please adjust filter.", QtGui.QMessageBox.Ok)

                StartStop = False

           
            # Calculating the max and min of the y axis to prevent moving of this axis

            Max_ECG = Patient_ECG.max()

            Min_ECG = Patient_ECG.min()           

            Max_PPG = Patient_PPG.max()

            Min_PPG = Patient_PPG.min()   
                       

# Disabling settings to prevent user from changing them while signal is plotting and causing the program to crash

            if StartStop == True:                

                self.comboBox.setDisabled(1)

                self.pushButton_4.setDisabled(1)

                self.checkBox_5.setDisabled(1)

                self.checkBox_6.setDisabled(1)

                self.checkBox_7.setDisabled(1)

                self.checkBox_8.setDisabled(1)

                self.checkBox_9.setDisabled(1)

                self.checkBox_10.setDisabled(1)

                self.checkBox_11.setDisabled(1)

                self.checkBox_12.setDisabled(1)

                self.lineEdit.setDisabled(1)

                self.lineEdit_2.setDisabled(1)

            

# Real Time Plot of Signals using a timer

            while (StartStop):
                
# Start timer
                
                Start_Time = dt.datetime.now()
    
# Stopping the plot if the remaining datapoints are not enough            
                if not((len(x_ECG[i_ECG:2000+ i_ECG])==len(Patient_ECG[i_ECG:2000+ i_ECG])
                and len(x_ECG[i_ECG:2000+ i_ECG])==len(ECG_peaks_nan[i_ECG:2000+ i_ECG]))
                and (len(x_PPG[i_PPG:2000+ i_PPG])==len(Patient_PPG[i_PPG:2000+ i_PPG])
                and len(x_PPG[i_PPG:2000+ i_PPG])==len(PPG_peaks_nan[i_PPG:2000+ i_PPG]))):
                    self.stopPlot()
                    break

# Plotting of the ECG Signal

                if (i_ECG<len(Patient_ECG)):                    

                    x = x_ECG[i_ECG:2000+ i_ECG]

                    y = Patient_ECG[i_ECG:2000+ i_ECG]

                    z = ECG_peaks_nan[i_ECG:2000+ i_ECG]

                    self.ECG.setYRange(Max_ECG, Min_ECG)

                    self.ECG.plot(x, y, clear=True)

# Plotting of ECG Peaks if signal is filtered

                    if ECG_Filtered_flag == 1:                        

                        self.ECG.plot(x,z, symbol='o', pen=None)

                    QtGui.QApplication.processEvents()


# Getting the time for PTT calculation

                    time_ecg = np.nonzero(ECG_peaks[i_ECG:2000+ i_ECG])

# Plotting the PPG Signal

                if(i_PPG<len(Patient_PPG)):

                    x = x_PPG[i_PPG:2000+ i_PPG]

                    y = Patient_PPG[i_PPG:2000+ i_PPG]

                    z = PPG_peaks_nan[i_PPG:2000+ i_PPG]

                    self.PPG.setYRange(Max_PPG, Min_PPG)

                    self.PPG.plot(x, y, clear=True)
                    
# Plotting of PPG Peaks if signal is filtered

                    if PPG_Filtered_flag == 1:                        

                        self.PPG.plot(x,z, symbol='o', pen=None)

                    QtGui.QApplication.processEvents()

# Getting the time for PTT calculation, PTT calculation and showing the result on the display

                    time_ppg = np.nonzero(PPG_peaks[i_PPG:2000+ i_PPG])

                if PPG_Filtered_flag and ECG_Filtered_flag and not(len(time_ppg[0])==0) and not(len(time_ecg[0])==0):

                    ptt = x_PPG[time_ppg[0][0]] - x_ECG[time_ecg[0][0]]

                    if (ptt < 0 and len(time_ppg[0])>1):

                        ptt = x_PPG[time_ppg[0][1]] - x_ECG[time_ecg[0][0]]

                    self.lcdNumber.display(str(1000*ptt))
                    
# Show 0 if not enough peaks could be detected

                else:

                    self.lcdNumber.display(0)
                    
# Setting the passed time as starttime for going through the loop the next time
                
                Loop_Time = (dt.datetime.now() - Start_Time).microseconds/1000
                
                if (i_ECG<len(Patient_ECG)):
                    i_ECG = i_ECG+Loop_Time
                
                if(i_PPG<len(Patient_PPG)):
                    i_PPG = i_PPG+Loop_Time


# Stopping the Real Time Plot                                    

    def stopPlot(self):

        global StartStop

        

        StartStop = False

        self.comboBox.setDisabled(0)

        self.pushButton_4.setDisabled(0)

               

               

# Reset Button

    def resetAll(self):

        global filepath, Patient, Combobox_list, i_ECG, i_PPG, StartStop

        global ECG_RAW_flag, ECG_Filtered_flag, PPG_RAW_flag, PPG_Filtered_flag

        global Highpass_flag, Lowpass_flag, Bandpass_flag, Bandstop_flag

        

        i_ECG = 0

        i_PPG = 0

        StartStop = False        

        self.comboBox.setDisabled(0)

        self.pushButton_4.setDisabled(0)        

        self.lineEdit.setDisabled(0)

        self.lineEdit_2.setDisabled(0)

        self.checkBox_5.setCheckState(0)

        self.checkBox_6.setCheckState(0)

        self.checkBox_7.setCheckState(0)

        self.checkBox_8.setCheckState(0)

        self.checkBox_9.setCheckState(0)

        self.checkBox_10.setCheckState(0)

        self.checkBox_11.setCheckState(0)

        self.checkBox_12.setCheckState(0)

        Highpass_flag = False

        Lowpass_flag = False

        Bandpass_flag = False

        Bandstop_flag = False

        ECG_RAW_flag = False

        ECG_Filtered_flag = False

        PPG_RAW_flag = False

        PPG_Filtered_flag = False

        self.checkBox_5.setDisabled(0)

        self.checkBox_6.setDisabled(0)

        self.checkBox_7.setDisabled(0)

        self.checkBox_8.setDisabled(0)

        self.checkBox_9.setDisabled(0)

        self.checkBox_10.setDisabled(0)

        self.checkBox_11.setDisabled(0)

        self.checkBox_12.setDisabled(0)



# Save Button        

    def Save(self):

        global filepath, Patient_PPG, Patient_ECG, ECG_peaks, Patient, PPG_peaks, ECG_startpoint, time, ECG_Filtered_flag, PPG_Filtered_flag



# Filtered data saved in dictionary

        time = Patient['ticktimes_block'+str(self.comboBox.currentIndex()+1)][0]

        timecut = time[ECG_startpoint:len(time)]



# Save as .mat File

        if PPG_Filtered_flag and ECG_Filtered_flag:

            savemat('filteredData.mat', {'filtered_data': [[Patient_ECG],[Patient_PPG]], 'detected_peaks': [[ECG_peaks],[PPG_peaks]], 'ticktimes': timecut})

        elif PPG_Filtered_flag and not ECG_Filtered_flag:

            savemat('filteredData.mat', {'filtered_data': Patient_PPG, 'detected_peaks': PPG_peaks, 'ticktimes': timecut})

        elif not PPG_Filtered_flag and ECG_Filtered_flag:

            savemat('filteredData.mat', {'filtered_data': Patient_ECG, 'detected_peaks': ECG_peaks, 'ticktimes': timecut})

        else:

            QtGui.QMessageBox.critical(None, 'Error',

            "There is no filtered data to be saved.", QtGui.QMessageBox.Ok)







# Plotting the unfiltered ECG Signal        

    def ECG_RAW_func(self):
        
# Importing global variables

        global ECG_RAW_flag

# Setting flags and disabeling certain functions        

        ECG_RAW_flag = not ECG_RAW_flag

        if ECG_RAW_flag:

            self.checkBox_7.setDisabled(1)

        else:

            self.checkBox_7.setDisabled(0)



# Plotting the filtered ECG Signal            

    def ECG_Filtered_func(self):
        
# Importing global variables

        global ECG_Filtered_flag

# Setting flags and disabeling certain functions         

        ECG_Filtered_flag = not ECG_Filtered_flag

        if ECG_Filtered_flag:

            self.checkBox_6.setDisabled(1)

        else:

            self.checkBox_6.setDisabled(0)



# Plotting the unfiltered PPG Signal            

    def PPG_RAW_func(self):
        
# Importing global variables

        global PPG_RAW_flag

# Setting flags and disabeling certain functions         

        PPG_RAW_flag = not PPG_RAW_flag

        if PPG_RAW_flag:

            self.checkBox_8.setDisabled(1)

        else:

            self.checkBox_8.setDisabled(0)



# Plotting the filtered PPG Signal            

    def PPG_Filtered_func(self):
        
# Importing global variables

        global PPG_Filtered_flag

# Setting flags and disabeling certain functions 

        PPG_Filtered_flag = not PPG_Filtered_flag

        if PPG_Filtered_flag:

            self.checkBox_5.setDisabled(1)

        else:

            self.checkBox_5.setDisabled(0)



# Creating a Highpass Filter            

    def Highpass_func(self):
        
# Importing global variables

        global Highpass_flag

# Setting flags and disabeling certain functions         

        Highpass_flag = not Highpass_flag

        if Highpass_flag:

            self.checkBox_10.setDisabled(1)

            self.checkBox_11.setDisabled(1)

            self.checkBox_12.setDisabled(1)

            self.lineEdit_2.setDisabled(1)

        else:

            self.checkBox_10.setDisabled(0)

            self.checkBox_11.setDisabled(0)

            self.checkBox_12.setDisabled(0)

            self.lineEdit_2.setDisabled(0)



# Creating a Lowpass Filter            

    def Lowpass_func(self):
        
# Importing global variables

        global Lowpass_flag

# Setting flags and disabeling certain functions         

        Lowpass_flag = not Lowpass_flag

        if Lowpass_flag:

            self.checkBox_9.setDisabled(1)            

            self.checkBox_11.setDisabled(1)

            self.checkBox_12.setDisabled(1)

            self.lineEdit.setDisabled(1)

        else:

            self.checkBox_9.setDisabled(0)            

            self.checkBox_11.setDisabled(0)

            self.checkBox_12.setDisabled(0)

            self.lineEdit.setDisabled(0)



# Creting a Bandpass Filter            

    def Bandpass_func(self):
        
# Importing global variables

        global Bandpass_flag

# Setting flags and disabeling certain functions         

        Bandpass_flag = not Bandpass_flag

        if Bandpass_flag:

            self.checkBox_9.setDisabled(1)            

            self.checkBox_10.setDisabled(1)

            self.checkBox_12.setDisabled(1)

        else:

            self.checkBox_9.setDisabled(0)            

            self.checkBox_10.setDisabled(0)

            self.checkBox_12.setDisabled(0)



# Creating a Bandstop Filter            

    def Bandstop_func(self):
        
# Importing global variables

        global Bandstop_flag
        
# Setting flags and disabeling certain functions         

        Bandstop_flag = not Bandstop_flag

        if Bandstop_flag:

            self.checkBox_9.setDisabled(1)            

            self.checkBox_10.setDisabled(1)

            self.checkBox_11.setDisabled(1)

        else:

            self.checkBox_9.setDisabled(0)            

            self.checkBox_10.setDisabled(0)

            self.checkBox_11.setDisabled(0)



# Running the main applicatoin of the GUI

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)

    BioSignal = QtGui.QMainWindow()

    ui = Ui_BioSignal()

    ui.setupUi(BioSignal)

    BioSignal.show()

    sys.exit(app.exec_())


 
