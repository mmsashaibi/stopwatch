from PySide2 import QtCore, QtGui, QtWidgets
import configparser

def readinicfg(section):
    config = configparser.ConfigParser()
    config.read('stopwatch.ini')
    yval = config.getint(section, 'y')
    moval = config.getint(section, 'mo')
    dval = config.getint(section, 'd')
    hval = config.getint(section, 'h')
    mival = config.getint(section, 'mi')
    sval = config.getint(section, 's')
    txtval = config.get(section, 'txt')
    return [yval, moval, dval, hval, mival, sval, 0, txtval]

def cmp_dates(dt):
    last_datetime = QtCore.QDateTime(QtCore.QDate(dt[0], dt[1], dt[2]), QtCore.QTime(dt[3], dt[4], dt[5],dt[6]))
    cur_datetime = QtCore.QDateTime.currentDateTime()
    days = last_datetime.daysTo(cur_datetime)
    days_passed = int(days % 365.25) % 30
    months_passed = int((days % 365.25) / 30)
    years_passed = int(days / 365.25)
    secs = last_datetime.secsTo(cur_datetime) % 86400
    #print(secs)
    hours_passed = int(secs / 60 / 60)
    minutes_passed = int((secs - (hours_passed * 60 * 60)) / 60)
    secs_passed = secs % 60

    display_time = (dt[7] + "\t" + str(years_passed).zfill(2) + "/" + str(months_passed).zfill(2) + "/" + str(days_passed).zfill(2)
                    + ":::" + str(hours_passed).zfill(2) + ":" + str(minutes_passed).zfill(2) + ":" + str(secs_passed).zfill(2))
    return display_time

class Ui_Form(object):
    def show_time(self):
        #lcddisplay = display_datetime.toString('yyyy:M:d:hh:mm:ss')
        #self.label1.setText(cmp_dates([2020,11,21,1,0,0,0,"Event"]))
        self.label1.setText(cmp_dates(readinicfg('label1')))
        self.label2.setText(cmp_dates(readinicfg('label2')))
        self.label3.setText(cmp_dates(readinicfg('label3')))
        self.label4.setText(cmp_dates(readinicfg('label4')))
        self.label5.setText(cmp_dates(readinicfg('label5')))
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1100, 600)
        Form.setFixedWidth(1100)
        Form.setFixedHeight(600)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(26, 22, 1000, 100))
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label1.setStyleSheet('background-color:yellow ; color:red') #set text color
        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(30, 130, 1000, 100))
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(Form)
        self.label3.setGeometry(QtCore.QRect(30, 230, 1000, 100))
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(Form)
        self.label4.setGeometry(QtCore.QRect(30, 330, 1000, 100))
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(Form)
        self.label5.setGeometry(QtCore.QRect(30, 430, 1000, 100))
        self.label5.setFont(font)
        self.label5.setObjectName("label5")
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        #self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



import sys
if (__name__=='__main__'):
    app = QtWidgets.QApplication(sys.argv)
    dlg = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(dlg)
    dlg.show()
    #ui.show_time()
    sys.exit(app.exec_())
