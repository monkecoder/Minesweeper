# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'minesweeper_about.ui'
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
    QLabel, QSizePolicy, QWidget)

class Ui_MinesweeperAbout(object):
    def setupUi(self, MinesweeperAbout):
        if not MinesweeperAbout.objectName():
            MinesweeperAbout.setObjectName(u"MinesweeperAbout")
        MinesweeperAbout.resize(362, 427)
        self.buttonBox = QDialogButtonBox(MinesweeperAbout)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 390, 301, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(MinesweeperAbout)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 341, 16))
        self.label_2 = QLabel(MinesweeperAbout)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 50, 301, 331))
        font = QFont()
        font.setFamilies([u"Courier"])
        font.setPointSize(4)
        font.setBold(True)
        self.label_2.setFont(font)

        self.retranslateUi(MinesweeperAbout)
        self.buttonBox.accepted.connect(MinesweeperAbout.accept)
        self.buttonBox.rejected.connect(MinesweeperAbout.reject)

        QMetaObject.connectSlotsByName(MinesweeperAbout)
    # setupUi

    def retranslateUi(self, MinesweeperAbout):
        MinesweeperAbout.setWindowTitle(QCoreApplication.translate("MinesweeperAbout", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("MinesweeperAbout", u"https://github.com/monkecoder/Minesweeper.git", None))
        self.label_2.setText(QCoreApplication.translate("MinesweeperAbout", u"....................................................................................................\n"
"....................................................................................................\n"
"..............................................................................x&&&&&&x..............\n"
"...........................................................................;&&&&&&&&&&X.............\n"
".........................................................................+&&&&&&&+;x&&&x............\n"
".......................................................................x&&&&&&&;x&&X;&&&............\n"
"...............................;&&&&&&&&&$..........................x&&&&&&&&x;&&&&&xx&&............\n"
".............................x&&&&&&&&&&&&&&&&&&&&&&&&&X...........x&&&&Xx$$;x&&&xx$x;&&............\n"
"...........................+&&&&&&&&x.;;&&&&&&&&&&&&&&&&&&&&&&&x.+&&&x::;$$:x&&&+:xX+;&&............\n"
"..........................+&&&$x&&&:;x+;:X&$$$$$x;::;x;$&&&&&&&&&&&&x:.:x$:x&&&;"
                        ":;xx;x&&............\n"
".........................x&&&x+$&X:+xxxx;:;x$$$&&&$Xx;::;;;:::X&&&x:...;$;x$&&;:;;+x;x&&............\n"
".......................+&&&&x;$&X:+xXx;;+;;:;xxXXX$&&&$$xx+;;;;;;:::..:xx;x$&x:;;;+x;$&&............\n"
"................&&&&&&&&&&$;;x&$:+x$x;;;;;;;:::;xx+++xx$$Xxx;;;;;;;::::xxxx$$:;;;;;+;&&x............\n"
"................&&&&&&&&X+;;;&&:;x&$;;;;::;;:::.:;;;;;;;;;;;;;;;;;;;;;::++;xX:;;;;;;;&&.............\n"
"..............x&&&+xx+:::;;;x&x;x&&x;;;;;::::::::::;;;;;;;;;;;;;;;;;;;:::::xX+:;;;;:;&&.............\n"
"..............&&&xx$x;:::;;;X&;;X&$;;;;;;:::::::::::;;;;;;;;;;;;;;;;;::;:::;xx;::;;:;&&.............\n"
"..............&&:$&X;::::;;;$&:;&&x;;;;;;;;:::::::::::;;;;;;;;;;;;::;;;:;::;+xx;;;::X&$.............\n"
".............+&&&&X:::::.;;;X$:;&&;;;;;;;;;;::::::;::;;;;;;;;;;;;;;::;::::::;;++;;:.&&;.............\n"
"............+&&$$x:::::;:;;;x$;;&&;;;;;;;;;;;;::::;;;;;;;;;;:;:;:;;;:::::::::;;;;:::&&..............\n"
"...........;&&x::::::::;::;;+X+:&&$:;;;;;;;;;;;::;++;::"
                        ";;;::::::::::::::::::::::::::&&..............\n"
"..........+&&x:::::::::;;:;;;xx:x&&x:;;;;;;;;;;;;;xx;::::::::::::::::::::::::;;;::::&&;.............\n"
"..........$&x:::::::::::;;:;;;x;:X&&&:;;+;;;;;;;+xX+:::::::::::::::::::::::::;x+::::X&$.............\n"
".........+&&::::::::::::;+;;+;;;::X&&&$;;;+;;;xX&$x::::::::::::::::;::;:::::;x&$x:::;&&;............\n"
".........$&x:::::::::::::;+;;++;;::x&&&&&&&&&&&&&x::::::::::::::::x&&&&&::::;$$xx::::X&X............\n"
"........+&&:::::::::::::::;++;;+;;:::x&&&&&&&&&x:.......::::::::::x&&&&&::::;x$$x::::;&&............\n"
"........$&x:::::::::::::::::;+;;;;::::::;xXx+::...........::::::::+&&&&&::::;;;;;;;;::&&+...........\n"
".......;&&::::::::::::::::::::;;;;:::::::::...............:::::::::;$&&x::;++++;;xx+;:x&&+..........\n"
".......X&x::::::::::::::::::::::::::::::::...............::::::::::::::::;+++;;+X$x::::x&&+.........\n"
".......&&;:::::::::::::::::::::::::::::::::....:......:::::::::::::::::.:;;;;;x$&x::::::x&&+........\n"
".......&&:::::::::::::::::::::"
                        "::::::::::::::::..:::::::::::::::::::::;;:;;::;x&&x:::;;;::x&&........\n"
".......&&:.:::::::::::::::::::::::::::::::::::::::::::::::::::::::::;x;;;;;+x&&$::.:;;;:::&&+.......\n"
".......$&x.::::::::::::::::::::::::::::::::::::::::::::::::::::::::;xx;;;+++$&&;::.;:++::.$&x.......\n"
".......+&&:.:::::::::::::::::::::::::::::::::::::::::::::::;:::::::+Xx;+++;x&&x;:..;:++:::&&+.......\n"
"........$&x.::::::::::::::::::::;;:::;;;;;;;:::::::::;;;;:;;;::::::x$x++++;$&$;;:..:;;+::x&&........\n"
"........;&&:.:::::::::::::::;;:::;;;;:;;;;;;;;;;;;;;;;;;;;;;;::::;:X$++++x;&&;;;:.::;;;::&&x........\n"
".........$&x:.::::::::::::;;::;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;X$;;;+x;&$:;;::::::::x&$.........\n"
".........+&&x:.:::::::;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;x$;::;x;&x;;;:::::::x&&;.........\n"
"..........;&&x:.::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;xx:.:x;X$;:::::::x&&&x..........\n"
"...........;&&+:.::::::;;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;+x;:::+;x+;:::::x&&$;...........\n"
"....."
                        ".......;&&$+..::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::::;;;;$&&&&;.............\n"
".............x&&&x:.::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::::::..:;+&&&&X;..............\n"
"...............x&&&+..::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::::::.::&&;..................\n"
"................;X&&X&$x::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::::::::::x&&...................\n"
"..................&&&&&&&x;.::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::::::;;;;:x&&&+...................\n"
"..................&&&xx$&&$x;:.::::::;;;;;;;;;;;;;;;;;;;;;;;;;::::::::;xxx$&&&&+....................\n"
"..................&&&$+;+xXXxx;:.::::::::;;;:::::::;;;;;:::::::::..:x&&&&&&&$+......................\n"
"..................$&&&&x+;;;++;;:;;::.:x&&&&&$Xxx+;:::::::::..::x&&&&&&$Xx;.........................\n"
"..................;$&&&&&$xx+;;x&&&&&$x&&$$$Xxxxxx+;;:...::x&&&&&&&&$;..............................\n"
"....................+&&&&&&&&&&&&&&&&&&&&;:;;;;;;;;;;:x&&&&&&&&&$+..................."
                        "...............\n"
"......................;X&&&&&&&&+....x&&&&Xxx+;;;;:;;:&&&&&$;.......................................\n"
"......................................&&&&&&&$$Xxx+;:+&&............................................\n"
"......................................x&&&&&&&&&&&&&&&&x............................................\n"
"........................................+$&&&&&&&&&&&&x.............................................\n"
"....................................................................................................\n"
"....................................................................................................", None))
    # retranslateUi

