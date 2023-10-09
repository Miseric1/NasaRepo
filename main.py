import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTabWidget, QWidget
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtGui import QAction
import random

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy, QPushButton
from PyQt6.QtGui import QGuiApplication, QFont
from PyQt6.QtCore import Qt




class LearnMoreWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Learn More")
        self.setGeometry(500, 200, 600, 425)
        self.setStyleSheet("background-color: white;")

        self.setStyleSheet("""background-color: #000000; /* Dark background color (black) */font-family: Arial, sans-serif; /* Font family */color: #FFFFFF; /* Text color (white) */""")

        titleLabel = QLabel("Additional Information", self)
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titleLabel.setGeometry(130, 15, 350, 30)
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        titleLabel.setFont(font)

        contentLabel = QLabel("What is an Eclipse?", self)
        contentLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        contentLabel.setGeometry(5, 50, 250, 60)
        font2 = QFont()
        font2.setPointSize(18)
        contentLabel.setFont(font2)

        whatIsAnEclipse = QLabel("An eclipse occurs when a celestial object such as a moon or a planet moves into the shadow of another. There are two main types of eclipses," 
                                 "solar eclipses and lunar eclipses.", self)
        whatIsAnEclipse.setAlignment(Qt.AlignmentFlag.AlignCenter)
        whatIsAnEclipse.setGeometry(50,107,500,50)
        whatIsAnEclipse.setWordWrap(True)
        font3 = QFont()
        font3.setPointSize(12)
        whatIsAnEclipse.setFont(font3)

        solarEclipse = QLabel("Solar Eclipse: Occurs when the Moon passes between the Earth and the Sun. During a solar eclipse, the Moon blocks the light of the sun from reaching Earth"
                              "while also casting its shadow on Earth", self)
        solarEclipse.setAlignment(Qt.AlignmentFlag.AlignCenter)
        solarEclipse.setGeometry(50,180,500,50)
        solarEclipse.setWordWrap(True)
        solarEclipse.setFont(font3)

        lunarEclipse = QLabel("Lunar Eclipse: Occurs when the Earth passes between the Sun and the Moon. During a lunar eclipse, the Earth blocks the sunlight that is"
                              "normally reflected by the Moon.", self)
        lunarEclipse.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lunarEclipse.setGeometry(50, 250, 500, 50)
        lunarEclipse.setWordWrap(True)
        lunarEclipse.setFont(font3)


        closeButton = QPushButton("Close", self)
        closeButton.setGeometry(250, 350, 100, 30)
        closeButton.clicked.connect(self.close)
        closeButton.setStyleSheet("background-color: white; color: black;")

    def center(self):
        windowGeometry = self.frameGeometry()
        centerPoint = QGuiApplication.primaryScreen().availableGeometry().center()
        windowGeometry.moveCenter(centerPoint)
        self.move(windowGeometry.topLeft())
    

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NASA Space Apps")
        self.setGeometry(100, 100, 800, 800)
        self.setStyleSheet("background-color: black;")

        titleLabel = QLabel("Eclipses", self)
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titleLabel.setGeometry(200, 15, 175, 75)

        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        titleLabel.setFont(font)
        titleLabel.setStyleSheet("border: 3px solid white; padding: 10px; color: white;")

        font2 = QFont()
        font2.setPointSize(17)
        font2.setBold(True)
        learnMoreButton = QPushButton("Learn More", self)
        learnMoreButton.setFont(font2) 
        learnMoreButton.setStyleSheet("background-color: white;")
        learnMoreButton.setGeometry(217, 150, 140, 45)
        learnMoreButton.clicked.connect(self.openLearnMoreWindow)

        self.resize(600, 400)
        self.centerWindow()

    def centerWindow(self):
        screen = QGuiApplication.primaryScreen()
        screenGeometry = screen.availableGeometry()
        windowWidth = self.geometry().width()
        windowHeight = self.geometry().height()
        x = (screenGeometry.width() - windowWidth) // 2
        y = (screenGeometry.height() - windowHeight) // 2
        self.move(x, y)

    def openLearnMoreWindow(self):
        self.learnMoreWindow = LearnMoreWindow()
        self.learnMoreWindow.show()
        self.learnMoreWindow.center()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec())