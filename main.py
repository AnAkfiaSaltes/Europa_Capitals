from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QApplication, QDialog, QLabel
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import sys
import sqlite3

# capitals = [
    # {"id": 1, "pos": (640, 760)},
    # {"id": 1, "pos": (630, 790)},
    # {"id": 2, "pos": (760, 350)},
    # {"id": 3, "pos": (710, 490)},
    # {"id": 4, "pos": (660, 430)},
    # {"id": 5, "pos": (320, 540)},
    # {"id": 6, "pos": (450, 460)},
    # {"id": 7, "pos": (460, 400)},
    # {"id": 8, "pos": (450, 300)},
    # {"id": 9, "pos": (620, 400)},
    # {"id": 10, "pos": (610, 360)},
    # {"id": 11, "pos": (610, 310)},
    # {"id": 12, "pos": (660, 610)},
    # {"id": 13, "pos": (540, 640)},
    # {"id": 14, "pos": (500, 520)},
    # {"id": 15, "pos": (540, 550)},
    # {"id": 16, "pos": (300, 460)},
    # {"id": 17, "pos": (610, 280)},
    # {"id": 18, "pos": (610, 280)},
    # {"id": 19, "pos": (640, 660)},
    # {"id": 20, "pos": (610, 280)},
    # {"id": 21, "pos": (560, 670)},
    # {"id": 22, "pos": (490, 600)},
    # {"id": 23, "pos": (530, 610)},
    # {"id": 24, "pos": (580, 700)},
    # {"id": 25, "pos": (580, 630)},
    # {"id": 26, "pos": (220, 400)},
    # {"id": 27, "pos": (360, 490)},
    # {"id": 28, "pos": (370, 460)},
    # {"id": 29, "pos": (170, 120)},
    # {"id": 30, "pos": (510, 550)},
    # {"id": 31, "pos": (530, 310)},
    # {"id": 32, "pos": (560, 470)},
    # {"id": 33, "pos": (560, 580)},
    # {"id": 34, "pos": (390, 580)},
    # {"id": 35, "pos": (460, 680)},
    # {"id": 36, "pos": (190, 690)},
    # {"id": 37, "pos": (90, 690)},

# ]

capitals = [
    {"id": 1, "pos": (630, 790)},

    {"id": 2, "pos": (750, 380)},
    {"id": 3, "pos": (700, 520)},
    {"id": 4, "pos": (650, 460)},
    {"id": 5, "pos": (310, 570)},
    {"id": 6, "pos": (440, 490)},

    {"id": 7, "pos": (450, 430)},
    {"id": 8, "pos": (440, 330)},
    {"id": 9, "pos": (610, 430)},
    {"id": 10, "pos": (600, 390)},
    {"id": 11, "pos": (600, 340)},
    {"id": 12, "pos": (650, 640)},

    {"id": 13, "pos": (530, 670)},
    {"id": 14, "pos": (490, 550)},
    {"id": 15, "pos": (530, 580)},
    {"id": 16, "pos": (290, 490)},
    # {"id": 17, "pos": (10, 10)},
    #
    # {"id": 18, "pos": (600, 310)},
    {"id": 19, "pos": (630, 690)},
    {"id": 20, "pos": (600, 310)},
    {"id": 21, "pos": (550, 700)},
    {"id": 22, "pos": (480, 630)},

    {"id": 23, "pos": (520, 640)},
    {"id": 24, "pos": (570, 730)},
    {"id": 25, "pos": (570, 660)},
    {"id": 26, "pos": (210, 430)},
    {"id": 27, "pos": (350, 520)},

    {"id": 28, "pos": (360, 490)},
    {"id": 29, "pos": (160, 150)},
    {"id": 30, "pos": (490, 580)},
    {"id": 31, "pos": (520, 340)},
    {"id": 32, "pos": (550, 500)},

    {"id": 33, "pos": (550, 610)},
    {"id": 34, "pos": (380, 610)},
    {"id": 35, "pos": (450, 710)},
    {"id": 36, "pos": (180, 720)},
    {"id": 37, "pos": (80, 720)},

]


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setStyleSheet("border-radius: 10px;")
        # uic.loadUi('Europa3.ui', self)
        uic.loadUi('Europa8.ui', self)

        self.__initUI__()
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def __initUI__(self):
        for c in capitals:
            button = QPushButton("", self)
            button.id = c["id"]
            button.setGeometry(c["pos"][0], c["pos"][1], 40, 40)
            icon = QIcon('icons8-button-24.png')
            # button.setText('')
            button.setIcon(icon)
            button.setFlat(True)
            button.clicked.connect(self.handle_press)

    def handle_press(self):
        button = self.sender()
        inf = "SELECT * FROM CAPITALS WHERE id = ?"
        self.cursor.execute(inf, (button.id,))
        result = self.cursor.fetchall()
        if result:
            dialog = QDialog()
            layout = QVBoxLayout(dialog)
            for row in result:
                label = QLabel(f"{row[2]}")
                label.setWordWrap(True)
                layout.addWidget(label)
            dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
