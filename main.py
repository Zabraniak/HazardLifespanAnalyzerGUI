# Analyze
import pandas
import matplotlib.pyplot as plt

# GUI
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import (
    QGridLayout,
    QFileDialog,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QSizePolicy
)


def lifeTable(path):
    data = pandas.read_excel(path, skiprows=2)
    frame = pandas.DataFrame(data, columns=['Action', 'Time to failure'])

    preparation = {'Interval endpoint': [0, 2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000],
                   'n': ['X', 0, 0, 0, 0, 0, 0, 0, 0], 'd': ['X', 0, 0, 0, 0, 0, 0, 0, 0],
                   'w': ['X', 0, 0, 0, 0, 0, 0, 0, 0],
                   'Survival': [1, 0, 0, 0, 0, 0, 0, 0, 0],
                   'Interval midpoint': [1000, 3000, 5000, 7000, 9000, 11000, 13000, 15000, 'X'],
                   'Hazard': [0, 0, 0, 0, 0, 0, 0, 0, 0]}

    table = pandas.DataFrame(preparation)

    n = frame.shape[0]
    old_survival = 0
    n_list = []
    d_list = []
    w_list = []
    survival_list = []
    endpoint_list = [0, 2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000]
    interval_list = [1000, 3000, 5000, 7000, 9000, 11000, 13000, 15000]
    hazard_list = []
    table['Survival'] = table['Survival'].astype("float")
    table['Hazard'] = table['Hazard'].astype("float")
    for index_table, row_table in table.iterrows():
        if index_table == 0:
            old_survival = 1
            continue

        n_list.append(n)
        table.at[index_table, 'n'] = n
        d = 0
        old_n = n

        for index_frame, row_frame in frame.iterrows():
            if row_table['Interval endpoint'] > row_frame['Time to failure'] > (
                    row_table['Interval endpoint'] - 2000):
                n = n - 1

                if row_frame['Action'] == "F":
                    d = d + 1
        d_list.append(d)
        table.at[index_table, 'd'] = d

        w = old_n - n - d
        w_list.append(w)
        table.at[index_table, 'w'] = w
        new_survival = old_survival * (1 - d / (old_n - w / 2))
        survival_list.append(new_survival)
        table.at[index_table, 'Survival'] = new_survival
        old_survival = new_survival

    for i in range(len(n_list)):
        if i == len(n_list) - 1:
            continue
        hazard_list.append(survival_list[i + 1] * d_list[i + 1] / ((n_list[i + 1] - 0.5 * w_list[i + 1]) * 2000))

    index = 0
    for index_table, row_table in table.iterrows():
        if index_table == 0:
            continue
        if index_table == 8:
            continue
        table.at[index_table, 'Hazard'] = hazard_list[index]
        index = index + 1

    fig, axis = plt.subplots(2, figsize=(10, 10))

    survival_list.insert(0, 1)
    axis[0].plot(endpoint_list, survival_list, "o-")
    axis[0].set_xlabel("Days elapsed")
    axis[0].set_ylabel("Survival Distribution")
    axis[0].set_title("Survival")

    survival_list.insert(0, 0)
    interval_list.pop()
    axis[1].plot(interval_list, hazard_list, "r-")
    axis[1].set_xlabel("Days elapsed")
    axis[1].set_ylabel("Hazard Function")
    axis[1].set_title("Hazard")

    fig.canvas.manager.set_window_title('Life Table')

    plt.show()


class Analyzer(QWidget):

    def __init__(self):
        super().__init__()
        self.GUI()

    def lifeTableButton(self):
        button = QPushButton("Analyze the file", self)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(self.activateLifeTable)
        return button

    def quitButton(self):
        button = QPushButton("Quit", self)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(self.closeApp)
        return button

    def path(self):
        path, _ = QFileDialog.getOpenFileName(self, "Choose a file to analyze", filter="Data files (*.xlsx)")
        return path

    def closeApp(self):
        sys.exit()

    def activateLifeTable(self):
        path = self.path()
        if path == "":
            return
        lifeTable(path)

    def GUI(self):
        menu = QGridLayout()
        layout = QVBoxLayout()
        layout.addWidget(self.lifeTableButton())
        layout.addWidget(self.quitButton())
        layout.addStretch()
        menu.addLayout(layout, 0, 0, 0, 0)
        self.setLayout(menu)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainmenu = QMainWindow()
    Analyzer = Analyzer()
    mainmenu.setWindowTitle("Life Cycle Analyzer v.1.0")
    mainmenu.setCentralWidget(Analyzer)
    mainmenu.setWindowIcon(QtGui.QIcon('Icon.png'))
    mainmenu.resize(200, 100)
    mainmenu.show()
    sys.exit(app.exec_())
