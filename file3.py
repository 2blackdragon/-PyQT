import sys
import plan1
import plan
import plan2
import plan3
import plan4
import pyglet
import math
import time
from datetime import datetime, timedelta
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QInputDialog
from PyQt5.QtWidgets import QLabel, QPushButton, QCheckBox


class TimerWindow(QWidget, plan1.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.way = 'melodies/cosmic-9466.mp3'
        self.setFixedSize(300, 300)
        self.setWindowTitle('Таймер')

        self.choose_melody.clicked.connect(self.choose)
        self.start_btn.clicked.connect(self.start_timer)
        self.reset_btn.clicked.connect(self.reset)

        self.time.clicked.connect(self.open_time_window)
        self.alarm.clicked.connect(self.open_alarm_window)
        self.stopwatch.clicked.connect(self.open_stopwatch_window)

        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.display('00:00:00')

    def choose(self):
        self.way = QFileDialog.getOpenFileName(self, 'Выбрать мелодию', '',
                                               'Мелодия (*.mp3)')[0]
        melody = pyglet.media.load(self.way)
        melody.play()

    def start_timer(self):
        hours = int(self.hours_btn.currentText())
        minutes = int(self.minutes_btn.currentText())
        seconds = int(self.seconds_btn.currentText())
        self.timer = QTimer(self)
        self.begin = datetime.strptime(f"{hours}:{minutes}:{seconds}",
                                       '%H:%M:%S')
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)

    def show_time(self):
        if str(self.begin).split()[-1] == '00:00:00':
            self.timer.stop()
            self.lcdNumber.display(str(self.begin).split()[1])
            melody = pyglet.media.load(self.way)
            melody.play()
            return
        self.lcdNumber.display(str(self.begin).split()[1])
        self.begin = self.begin - timedelta(seconds=1)

    def reset(self):
        self.lcdNumber.display('00:00:00')
        self.timer.stop()

    def open_time_window(self):
        self.close()
        self.time_window = TimeWindow()
        self.time_window.show()

    def open_alarm_window(self):
        self.close()
        self.alarm_window = AlarmWindow()
        self.alarm_window.show()

    def open_stopwatch_window(self):
        self.close()
        self.stopwatch_window = StopwatchWindow()
        self.stopwatch_window.show()


class TimeWindow(QWidget, plan3.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(300, 300)
        self.setWindowTitle('Время')
        self.pushButton.clicked.connect(self.open_digital_clock)

        self.alarm_btn.clicked.connect(self.open_alarm_window)
        self.stopwatch_btn.clicked.connect(self.open_stopwatch_window)
        self.timer_btn_2.clicked.connect(self.open_timer_window)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_analog_clock_face(qp)
        qp.end()

    def draw_analog_clock_face(self, qp):
        qp.setPen(QColor(255, 162, 0))
        qp.drawText(147, 145, '.')
        for i in range(60):
            qp.drawLine(int(150 + 65 * math.cos(-i * 6 * math.pi/180 + math.pi/2)),
                        int(145 - 65 * math.sin(-6 * i * math.pi/180 + math.pi/2)),
                        int(150 + 60 * math.cos(-6 * i * math.pi/180 + math.pi/2)),
                        int(145 - 60 * math.sin(-6 * i * math.pi/180 + math.pi/2)))
            if i % 5 == 0:
                qp.drawLine(int(150 + 65 * math.cos(-i * 6 * math.pi / 180 + math.pi / 2)),
                            int(145 - 65 * math.sin(-6 * i * math.pi / 180 + math.pi / 2)),
                            int(150 + 55 * math.cos(-6 * i * math.pi / 180 + math.pi / 2)),
                            int(145 - 55 * math.sin(-6 * i * math.pi / 180 + math.pi / 2)))

        for i in range(12):
            num = i
            if i == 0:
                num = 12
            qp.drawText(int(145 + 80 * math.cos(-i * 30 * math.pi / 180 + math.pi / 2)),
                        int(150 - 80 * math.sin(-30 * i * math.pi / 180 + math.pi / 2)), str(num))

        time_now = time.localtime()
        time_sec = int(time.strftime("%S", time_now))
        time_hour = int(time.strftime("%I", time_now))
        time_min = int(time.strftime("%M", time_now))
        sec_angle = 6 * time_sec
        min_angle = time_min * 6 + time_sec * 0.1
        hour_angle = time_hour * 30 + time_min * 60 * (30 / 3600)

        # рисуем минутную стрелку
        qp.setPen(QPen(QColor(255, 162, 0), 2))
        qp.drawLine(147, 145,
                    int(150 - 50 * math.cos(min_angle * math.pi / 180 + math.pi / 2)),
                    int(145 - 50 * math.sin(min_angle * math.pi / 180 + math.pi / 2)))
        # рисуем часовую стрелку
        qp.setPen(QPen(QColor(255, 162, 0), 3))
        qp.drawLine(147, 145,
                    int(150 - 40 * math.cos(hour_angle * math.pi / 180 + math.pi / 2)),
                    int(145 - 40 * math.sin(hour_angle * math.pi / 180 + math.pi / 2)))
        # рисуем секундную стрелку
        qp.setPen(QPen(QColor(255, 162, 0), 1))
        qp.drawLine(147, 145,
                    int(150 - 60 * math.cos(sec_angle * math.pi / 180 + math.pi / 2)),
                    int(145 - 60 * math.sin(sec_angle * math.pi / 180 + math.pi / 2)))

    def open_alarm_window(self):
        self.close()
        self.alarm_window = AlarmWindow()
        self.alarm_window.show()

    def open_stopwatch_window(self):
        self.close()
        self.stopwatch_window = StopwatchWindow()
        self.stopwatch_window.show()

    def open_timer_window(self):
        self.close()
        self.timer_window = TimerWindow()
        self.timer_window.show()

    def open_digital_clock(self):
        self.close()
        self.digital_clock = DigitalClock()
        self.digital_clock.show()


class DigitalClock(QWidget, plan4.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(300, 300)
        self.setWindowTitle('Время')

        self.alarm_btn.clicked.connect(self.open_alarm_window)
        self.stopwatch_btn.clicked.connect(self.open_stopwatch_window)
        self.timer_btn_2.clicked.connect(self.open_timer_window)
        self.pushButton.clicked.connect(self.open_analog_clock)

        self.lcdNumber.setDigitCount(8)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)

    def show_time(self):
        time_now = time.localtime()
        time_sec = time.strftime("%S", time_now)
        time_hour = time.strftime("%H", time_now)
        time_min = time.strftime("%M", time_now)
        self.lcdNumber.display(f"{time_hour}:{time_min}:{time_sec}")

    def open_alarm_window(self):
        self.close()
        self.alarm_window = AlarmWindow()
        self.alarm_window.show()

    def open_stopwatch_window(self):
        self.close()
        self.stopwatch_window = StopwatchWindow()
        self.stopwatch_window.show()

    def open_timer_window(self):
        self.close()
        self.timer_window = TimerWindow()
        self.timer_window.show()

    def open_analog_clock(self):
        self.close()
        self.analog_clock = TimeWindow()
        self.analog_clock.show()


class AlarmWindow(QWidget, plan2.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(300, 300)
        self.setWindowTitle('Будильник')

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_time)
        self.timer.start(1000)

        self.alarms = []
        self.alarms_to_play = []
        self.way = 'melodies/cosmic-9466.mp3'

        self.add_alarm_btn.clicked.connect(self.add_alarm)

        self.time_btn.clicked.connect(self.open_time_window)
        self.stopwatch_btn.clicked.connect(self.open_stopwatch_window)
        self.timer_btn_2.clicked.connect(self.open_timer_window)

    def add_alarm(self):
        values = [str(i) for i in range(0, 24)]
        hour, ok_pressed = QInputDialog.getItem(self, "Введите час", "Час", values, 0, False)

        if ok_pressed:
            values = [str(i) for i in range(0, 60)]
            minute, ok2_pressed = QInputDialog.getItem(self, "Введите минуты", "Минуты",
                                                       values, 0, False)
            if ok2_pressed:
                if len(hour) == 1:
                    hour = '0' + hour
                if len(minute) == 1:
                    minute = '0' + minute
                if (hour, minute) not in self.alarms:
                    self.alarms.append((hour, minute))

                    i = self.gridLayout.rowCount()
                    label = QLabel(f"{self.alarms[-1][0]}:{self.alarms[-1][1]}", self)
                    self.gridLayout.addWidget(label, i, 0)
                    check_box = QCheckBox("Вкл", self)
                    check_box.stateChanged.connect(self.on_alarm)
                    self.gridLayout.addWidget(check_box, i, 1)
                    button = QPushButton("Удалить", self)
                    button.resize(70, 30)
                    button.clicked.connect(self.del_alarm)
                    self.gridLayout.addWidget(button, i, 2)

    def del_alarm(self):
        index = self.gridLayout.indexOf(self.sender())
        row = self.gridLayout.getItemPosition(index)[0]
        for column in range(self.gridLayout.columnCount()):
            layout = self.gridLayout.itemAtPosition(row, column)
            if layout is not None:
                text = layout.widget().text()
                if ':' in text:
                    if (text.split(':')[0], text.split(':')[1]) in self.alarms:
                        self.alarms.pop(self.alarms.index((text.split(':')[0],
                                                           text.split(':')[1])))
                    if (int(text.split(':')[0]), int(text.split(':')[1])) in self.alarms_to_play:
                        value = (int(text.split(':')[0]), int(text.split(':')[1]))
                        self.alarms_to_play.pop(self.alarms_to_play.index(value))
                layout.widget().deleteLater()
                self.gridLayout.removeItem(layout)

    def on_alarm(self):
        if self.sender().isChecked():
            index = self.gridLayout.indexOf(self.sender())
            row = self.gridLayout.getItemPosition(index)[0]
            for column in range(self.gridLayout.columnCount()):
                layout = self.gridLayout.itemAtPosition(row, column)
                if layout is not None:
                    text = layout.widget().text()
                    if ':' in text:
                        h = int(text.split(':')[0])
                        m = int(text.split(':')[1])
                        self.alarms_to_play.append((h, m))
        else:
            index = self.gridLayout.indexOf(self.sender())
            row = self.gridLayout.getItemPosition(index)[0]
            for column in range(self.gridLayout.columnCount()):
                layout = self.gridLayout.itemAtPosition(row, column)
                if layout is not None:
                    text = layout.widget().text()
                    if ':' in text:
                        h = int(text.split(':')[0])
                        m = int(text.split(':')[1])
                        self.alarms_to_play.pop(self.alarms_to_play.index((h, m)))

    def check_time(self):
        for i in self.alarms_to_play:
            count = 0
            h, m = i[0], i[1]
            hours = int(datetime.now().hour)
            minutes = int(datetime.now().minute)
            seconds = int(datetime.now().second)
            if count == len(self.alarms_to_play):
                self.timer.stop()
            if h == hours and m == minutes and 0 == seconds:
                count += 1
                melody = pyglet.media.load(self.way)
                melody.play()
                return

    def open_time_window(self):
        self.close()
        self.time_window = TimeWindow()
        self.time_window.show()

    def open_stopwatch_window(self):
        self.close()
        self.alarm_window = StopwatchWindow()
        self.alarm_window.show()

    def open_timer_window(self):
        self.close()
        self.timer_window = TimerWindow()
        self.timer_window.show()


class StopwatchWindow(QWidget, plan.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(300, 300)
        self.setWindowTitle('Секундомер')
        self.flag = False
        self.text = ''
        self.count = 1
        self.begin = datetime.strptime('00:00.00', '%M:%S.%f')

        self.start_btn.clicked.connect(self.start_stopwatch)
        self.stop_btn.clicked.connect(self.stop_stopwatch)
        self.circle_btn.clicked.connect(self.circle_stopwatch)
        self.reset_btn.clicked.connect(self.reset_stopwatch)

        self.textEdit.setReadOnly(True)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.display('00:00.00')

        self.time.clicked.connect(self.open_time_window)
        self.alarm.clicked.connect(self.open_alarm_window)
        self.timer.clicked.connect(self.open_timer_window)

    def show_time(self):
        if not self.flag:
            self.timer.stop()
            self.lcdNumber.display(str(self.begin).split()[1][3:11])
            self.textEdit.setText(self.text)
            return
        self.begin = self.begin + timedelta(milliseconds=1)
        self.lcdNumber.display(str(self.begin).split()[1][3:11])

    def start_stopwatch(self):
        self.flag = True
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1)

    def stop_stopwatch(self):
        self.flag = False

    def circle_stopwatch(self):
        if f"Круг{self.count}: {str(self.begin).split()[1][3:11]}" not in self.text:
            self.text += f"Круг{self.count}: {str(self.begin).split()[1][3:11]}\n"
        self.textEdit.setText(self.text)
        self.count += 1

    def reset_stopwatch(self):
        self.timer.stop()
        self.begin = datetime.strptime('00:00.00', '%M:%S.%f')
        self.lcdNumber.display('00:00.00')
        self.count = 1
        self.text = ''
        self.textEdit.setText(self.text)

    def open_time_window(self):
        self.close()
        self.time_window = TimeWindow()
        self.time_window.show()

    def open_alarm_window(self):
        self.close()
        self.alarm_window = AlarmWindow()
        self.alarm_window.show()

    def open_timer_window(self):
        self.close()
        self.timer_window = TimerWindow()
        self.timer_window.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TimerWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
