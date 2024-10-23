# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'minesweeper_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLCDNumber, QLabel,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QTimeEdit,
    QVBoxLayout, QWidget)

class Ui_MinesweeperWindow(object):
    def setupUi(self, MinesweeperWindow):
        if not MinesweeperWindow.objectName():
            MinesweeperWindow.setObjectName(u"MinesweeperWindow")
        MinesweeperWindow.resize(800, 600)
        self.action_restartGame = QAction(MinesweeperWindow)
        self.action_restartGame.setObjectName(u"action_restartGame")
        self.action_settings = QAction(MinesweeperWindow)
        self.action_settings.setObjectName(u"action_settings")
        self.action_aboutProgram = QAction(MinesweeperWindow)
        self.action_aboutProgram.setObjectName(u"action_aboutProgram")
        self.action_themeLight = QAction(MinesweeperWindow)
        self.action_themeLight.setObjectName(u"action_themeLight")
        self.action_themeLight.setCheckable(True)
        self.action_themeDark = QAction(MinesweeperWindow)
        self.action_themeDark.setObjectName(u"action_themeDark")
        self.action_themeDark.setCheckable(True)
        self.centralwidget = QWidget(MinesweeperWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_cellsUncovered = QLabel(self.centralwidget)
        self.label_cellsUncovered.setObjectName(u"label_cellsUncovered")

        self.horizontalLayout.addWidget(self.label_cellsUncovered)

        self.lcdNumber_cellsUncovered = QLCDNumber(self.centralwidget)
        self.lcdNumber_cellsUncovered.setObjectName(u"lcdNumber_cellsUncovered")
        self.lcdNumber_cellsUncovered.setFrameShadow(QFrame.Shadow.Plain)
        self.lcdNumber_cellsUncovered.setDigitCount(3)
        self.lcdNumber_cellsUncovered.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout.addWidget(self.lcdNumber_cellsUncovered)

        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")

        self.horizontalLayout.addWidget(self.label_1)

        self.lcdNumber_cellsNotMined = QLCDNumber(self.centralwidget)
        self.lcdNumber_cellsNotMined.setObjectName(u"lcdNumber_cellsNotMined")
        self.lcdNumber_cellsNotMined.setFrameShadow(QFrame.Shadow.Plain)
        self.lcdNumber_cellsNotMined.setDigitCount(3)
        self.lcdNumber_cellsNotMined.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout.addWidget(self.lcdNumber_cellsNotMined)

        self.label_cellsFlagged = QLabel(self.centralwidget)
        self.label_cellsFlagged.setObjectName(u"label_cellsFlagged")

        self.horizontalLayout.addWidget(self.label_cellsFlagged)

        self.lcdNumber_cellsFlagged = QLCDNumber(self.centralwidget)
        self.lcdNumber_cellsFlagged.setObjectName(u"lcdNumber_cellsFlagged")
        self.lcdNumber_cellsFlagged.setFrameShadow(QFrame.Shadow.Plain)
        self.lcdNumber_cellsFlagged.setDigitCount(3)
        self.lcdNumber_cellsFlagged.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout.addWidget(self.lcdNumber_cellsFlagged)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lcdNumber_cellsMined = QLCDNumber(self.centralwidget)
        self.lcdNumber_cellsMined.setObjectName(u"lcdNumber_cellsMined")
        self.lcdNumber_cellsMined.setFrameShadow(QFrame.Shadow.Plain)
        self.lcdNumber_cellsMined.setDigitCount(3)
        self.lcdNumber_cellsMined.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout.addWidget(self.lcdNumber_cellsMined)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_timer = QLabel(self.centralwidget)
        self.label_timer.setObjectName(u"label_timer")

        self.horizontalLayout.addWidget(self.label_timer)

        self.frame_timer = QFrame(self.centralwidget)
        self.frame_timer.setObjectName(u"frame_timer")
        self.frame_timer.setFrameShape(QFrame.Shape.Box)
        self.frame_timer.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_timer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.timeEdit_timer = QTimeEdit(self.frame_timer)
        self.timeEdit_timer.setObjectName(u"timeEdit_timer")
        self.timeEdit_timer.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.timeEdit_timer.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.timeEdit_timer.setFrame(False)
        self.timeEdit_timer.setReadOnly(True)
        self.timeEdit_timer.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.verticalLayout_2.addWidget(self.timeEdit_timer)


        self.horizontalLayout.addWidget(self.frame_timer)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MinesweeperWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MinesweeperWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu_settings = QMenu(self.menubar)
        self.menu_settings.setObjectName(u"menu_settings")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_vIew = QMenu(self.menubar)
        self.menu_vIew.setObjectName(u"menu_vIew")
        self.menu_theme = QMenu(self.menu_vIew)
        self.menu_theme.setObjectName(u"menu_theme")
        MinesweeperWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_vIew.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_settings.addAction(self.action_restartGame)
        self.menu_settings.addSeparator()
        self.menu_settings.addAction(self.action_settings)
        self.menu_help.addAction(self.action_aboutProgram)
        self.menu_vIew.addAction(self.menu_theme.menuAction())
        self.menu_theme.addAction(self.action_themeLight)
        self.menu_theme.addAction(self.action_themeDark)

        self.retranslateUi(MinesweeperWindow)

        QMetaObject.connectSlotsByName(MinesweeperWindow)
    # setupUi

    def retranslateUi(self, MinesweeperWindow):
        MinesweeperWindow.setWindowTitle(QCoreApplication.translate("MinesweeperWindow", u"MainWindow", None))
        self.action_restartGame.setText(QCoreApplication.translate("MinesweeperWindow", u"Restart game", None))
        self.action_settings.setText(QCoreApplication.translate("MinesweeperWindow", u"Settings", None))
        self.action_aboutProgram.setText(QCoreApplication.translate("MinesweeperWindow", u"About program", None))
        self.action_themeLight.setText(QCoreApplication.translate("MinesweeperWindow", u"Light", None))
        self.action_themeDark.setText(QCoreApplication.translate("MinesweeperWindow", u"Dark", None))
        self.label_cellsUncovered.setText(QCoreApplication.translate("MinesweeperWindow", u"Uncovered cells:", None))
        self.label_1.setText(QCoreApplication.translate("MinesweeperWindow", u"/", None))
        self.label_cellsFlagged.setText(QCoreApplication.translate("MinesweeperWindow", u"Flagged cells:", None))
        self.label_2.setText(QCoreApplication.translate("MinesweeperWindow", u"/", None))
        self.label_timer.setText(QCoreApplication.translate("MinesweeperWindow", u"Timer:", None))
        self.timeEdit_timer.setDisplayFormat(QCoreApplication.translate("MinesweeperWindow", u"mm:ss", None))
        self.menu_settings.setTitle(QCoreApplication.translate("MinesweeperWindow", u"Game", None))
        self.menu_help.setTitle(QCoreApplication.translate("MinesweeperWindow", u"Help", None))
        self.menu_vIew.setTitle(QCoreApplication.translate("MinesweeperWindow", u"VIew", None))
        self.menu_theme.setTitle(QCoreApplication.translate("MinesweeperWindow", u"Theme", None))
    # retranslateUi

