# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'minesweeper_settings.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QSpinBox, QWidget)

class Ui_MinesweeperSettings(object):
    def setupUi(self, MinesweeperSettings):
        if not MinesweeperSettings.objectName():
            MinesweeperSettings.setObjectName(u"MinesweeperSettings")
        MinesweeperSettings.resize(392, 285)
        self.buttonBox = QDialogButtonBox(MinesweeperSettings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label_rows = QLabel(MinesweeperSettings)
        self.label_rows.setObjectName(u"label_rows")
        self.label_rows.setGeometry(QRect(20, 20, 111, 21))
        self.label_cols = QLabel(MinesweeperSettings)
        self.label_cols.setObjectName(u"label_cols")
        self.label_cols.setGeometry(QRect(20, 50, 111, 21))
        self.spinBox_rows = QSpinBox(MinesweeperSettings)
        self.spinBox_rows.setObjectName(u"spinBox_rows")
        self.spinBox_rows.setGeometry(QRect(140, 20, 42, 22))
        self.spinBox_cols = QSpinBox(MinesweeperSettings)
        self.spinBox_cols.setObjectName(u"spinBox_cols")
        self.spinBox_cols.setGeometry(QRect(140, 50, 42, 22))
        self.label_mines = QLabel(MinesweeperSettings)
        self.label_mines.setObjectName(u"label_mines")
        self.label_mines.setGeometry(QRect(20, 90, 111, 21))
        self.spinBox_mines = QSpinBox(MinesweeperSettings)
        self.spinBox_mines.setObjectName(u"spinBox_mines")
        self.spinBox_mines.setGeometry(QRect(140, 90, 42, 22))
        self.label_animationPeriod = QLabel(MinesweeperSettings)
        self.label_animationPeriod.setObjectName(u"label_animationPeriod")
        self.label_animationPeriod.setGeometry(QRect(20, 130, 111, 21))
        self.spinBox_animationPeriod = QSpinBox(MinesweeperSettings)
        self.spinBox_animationPeriod.setObjectName(u"spinBox_animationPeriod")
        self.spinBox_animationPeriod.setGeometry(QRect(140, 130, 42, 22))

        self.retranslateUi(MinesweeperSettings)
        self.buttonBox.accepted.connect(MinesweeperSettings.accept)
        self.buttonBox.rejected.connect(MinesweeperSettings.reject)

        QMetaObject.connectSlotsByName(MinesweeperSettings)
    # setupUi

    def retranslateUi(self, MinesweeperSettings):
        MinesweeperSettings.setWindowTitle(QCoreApplication.translate("MinesweeperSettings", u"Dialog", None))
        self.label_rows.setText(QCoreApplication.translate("MinesweeperSettings", u"Rows (height):", None))
        self.label_cols.setText(QCoreApplication.translate("MinesweeperSettings", u"Columns (width):", None))
        self.label_mines.setText(QCoreApplication.translate("MinesweeperSettings", u"Mines:", None))
        self.label_animationPeriod.setText(QCoreApplication.translate("MinesweeperSettings", u"Animation period", None))
    # retranslateUi

