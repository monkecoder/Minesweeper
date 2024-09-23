# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mineswepeer_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QLCDNumber, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QTimeEdit, QWidget)

class Ui_MinesweeperWindow(object):
    def setupUi(self, MinesweeperWindow):
        if not MinesweeperWindow.objectName():
            MinesweeperWindow.setObjectName(u"MinesweeperWindow")
        MinesweeperWindow.resize(800, 600)
        self.action_startNewGame = QAction(MinesweeperWindow)
        self.action_startNewGame.setObjectName(u"action_startNewGame")
        self.action_settings = QAction(MinesweeperWindow)
        self.action_settings.setObjectName(u"action_settings")
        self.action_aboutProgram = QAction(MinesweeperWindow)
        self.action_aboutProgram.setObjectName(u"action_aboutProgram")
        self.centralwidget = QWidget(MinesweeperWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_cellsUncovered = QLabel(self.centralwidget)
        self.label_cellsUncovered.setObjectName(u"label_cellsUncovered")

        self.horizontalLayout.addWidget(self.label_cellsUncovered)

        self.lcdNumber_cellsUncovered = QLCDNumber(self.centralwidget)
        self.lcdNumber_cellsUncovered.setObjectName(u"lcdNumber_cellsUncovered")
        self.lcdNumber_cellsUncovered.setDigitCount(3)
        self.lcdNumber_cellsUncovered.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout.addWidget(self.lcdNumber_cellsUncovered)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lcdNumber_cellsNotMined = QLCDNumber(self.centralwidget)
        self.lcdNumber_cellsNotMined.setObjectName(u"lcdNumber_cellsNotMined")
        self.lcdNumber_cellsNotMined.setDigitCount(3)
        self.lcdNumber_cellsNotMined.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout.addWidget(self.lcdNumber_cellsNotMined)

        self.label_cellsFlagged = QLabel(self.centralwidget)
        self.label_cellsFlagged.setObjectName(u"label_cellsFlagged")

        self.horizontalLayout.addWidget(self.label_cellsFlagged)

        self.lcdNumber_cellsFlagged = QLCDNumber(self.centralwidget)
        self.lcdNumber_cellsFlagged.setObjectName(u"lcdNumber_cellsFlagged")
        self.lcdNumber_cellsFlagged.setDigitCount(3)
        self.lcdNumber_cellsFlagged.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout.addWidget(self.lcdNumber_cellsFlagged)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lcdNumber_cellsMined = QLCDNumber(self.centralwidget)
        self.lcdNumber_cellsMined.setObjectName(u"lcdNumber_cellsMined")
        self.lcdNumber_cellsMined.setDigitCount(3)
        self.lcdNumber_cellsMined.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout.addWidget(self.lcdNumber_cellsMined)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_timer = QLabel(self.centralwidget)
        self.label_timer.setObjectName(u"label_timer")

        self.horizontalLayout.addWidget(self.label_timer)

        self.timeEdit_timer = QTimeEdit(self.centralwidget)
        self.timeEdit_timer.setObjectName(u"timeEdit_timer")
        self.timeEdit_timer.setReadOnly(True)
        self.timeEdit_timer.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout.addWidget(self.timeEdit_timer)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 1)

        MinesweeperWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MinesweeperWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu_settings = QMenu(self.menubar)
        self.menu_settings.setObjectName(u"menu_settings")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        MinesweeperWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.timeEdit_timer, self.tableWidget)

        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_settings.addAction(self.action_startNewGame)
        self.menu_settings.addSeparator()
        self.menu_settings.addAction(self.action_settings)
        self.menu_help.addAction(self.action_aboutProgram)

        self.retranslateUi(MinesweeperWindow)

        QMetaObject.connectSlotsByName(MinesweeperWindow)
    # setupUi

    def retranslateUi(self, MinesweeperWindow):
        MinesweeperWindow.setWindowTitle(QCoreApplication.translate("MinesweeperWindow", u"MainWindow", None))
        self.action_startNewGame.setText(QCoreApplication.translate("MinesweeperWindow", u"Start new game", None))
        self.action_settings.setText(QCoreApplication.translate("MinesweeperWindow", u"Settings", None))
        self.action_aboutProgram.setText(QCoreApplication.translate("MinesweeperWindow", u"About program", None))
        self.label_cellsUncovered.setText(QCoreApplication.translate("MinesweeperWindow", u"Uncovered cells:", None))
        self.label.setText(QCoreApplication.translate("MinesweeperWindow", u"/", None))
        self.label_cellsFlagged.setText(QCoreApplication.translate("MinesweeperWindow", u"Flagged cells:", None))
        self.label_2.setText(QCoreApplication.translate("MinesweeperWindow", u"/", None))
        self.label_timer.setText(QCoreApplication.translate("MinesweeperWindow", u"Timer", None))
        self.timeEdit_timer.setDisplayFormat(QCoreApplication.translate("MinesweeperWindow", u"mm:ss", None))
        self.menu_settings.setTitle(QCoreApplication.translate("MinesweeperWindow", u"Game", None))
        self.menu_help.setTitle(QCoreApplication.translate("MinesweeperWindow", u"Help", None))
    # retranslateUi

