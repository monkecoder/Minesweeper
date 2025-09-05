# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'minesweeper_settings.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
    QFrame, QGridLayout, QLabel, QSizePolicy,
    QSpacerItem, QSpinBox, QWidget)

class Ui_MinesweeperSettings(object):
    def setupUi(self, MinesweeperSettings):
        if not MinesweeperSettings.objectName():
            MinesweeperSettings.setObjectName(u"MinesweeperSettings")
        MinesweeperSettings.resize(282, 225)
        self.gridLayout = QGridLayout(MinesweeperSettings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_rows = QLabel(MinesweeperSettings)
        self.label_rows.setObjectName(u"label_rows")

        self.gridLayout.addWidget(self.label_rows, 0, 0, 1, 1)

        self.spinBox_rows = QSpinBox(MinesweeperSettings)
        self.spinBox_rows.setObjectName(u"spinBox_rows")

        self.gridLayout.addWidget(self.spinBox_rows, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(120, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.label_cols = QLabel(MinesweeperSettings)
        self.label_cols.setObjectName(u"label_cols")

        self.gridLayout.addWidget(self.label_cols, 1, 0, 1, 1)

        self.spinBox_cols = QSpinBox(MinesweeperSettings)
        self.spinBox_cols.setObjectName(u"spinBox_cols")

        self.gridLayout.addWidget(self.spinBox_cols, 1, 2, 1, 1)

        self.label_mines = QLabel(MinesweeperSettings)
        self.label_mines.setObjectName(u"label_mines")

        self.gridLayout.addWidget(self.label_mines, 2, 0, 1, 1)

        self.spinBox_mines = QSpinBox(MinesweeperSettings)
        self.spinBox_mines.setObjectName(u"spinBox_mines")

        self.gridLayout.addWidget(self.spinBox_mines, 2, 2, 1, 1)

        self.line = QFrame(MinesweeperSettings)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 3)

        self.label_animationPeriod = QLabel(MinesweeperSettings)
        self.label_animationPeriod.setObjectName(u"label_animationPeriod")

        self.gridLayout.addWidget(self.label_animationPeriod, 4, 0, 2, 2)

        self.spinBox_animationPeriod = QSpinBox(MinesweeperSettings)
        self.spinBox_animationPeriod.setObjectName(u"spinBox_animationPeriod")

        self.gridLayout.addWidget(self.spinBox_animationPeriod, 5, 2, 1, 1)

        self.line_2 = QFrame(MinesweeperSettings)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 6, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(MinesweeperSettings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 8, 0, 1, 4)


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
        self.label_animationPeriod.setText(QCoreApplication.translate("MinesweeperSettings", u"Animation period:", None))
    # retranslateUi

