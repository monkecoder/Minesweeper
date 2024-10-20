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
    QFrame, QLabel, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MinesweeperAbout(object):
    def setupUi(self, MinesweeperAbout):
        if not MinesweeperAbout.objectName():
            MinesweeperAbout.setObjectName(u"MinesweeperAbout")
        MinesweeperAbout.resize(318, 435)
        MinesweeperAbout.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        MinesweeperAbout.setAcceptDrops(True)
        self.verticalLayout = QVBoxLayout(MinesweeperAbout)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(MinesweeperAbout)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.Shape.StyledPanel)
        self.label.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(MinesweeperAbout)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(MinesweeperAbout)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Courier"])
        font1.setPointSize(4)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(MinesweeperAbout)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(MinesweeperAbout)
        self.buttonBox.accepted.connect(MinesweeperAbout.accept)
        self.buttonBox.rejected.connect(MinesweeperAbout.reject)

        QMetaObject.connectSlotsByName(MinesweeperAbout)
    # setupUi

    def retranslateUi(self, MinesweeperAbout):
        MinesweeperAbout.setWindowTitle(QCoreApplication.translate("MinesweeperAbout", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("MinesweeperAbout", u"Minesweeper game based on PySide6", None))
        self.label_2.setText(QCoreApplication.translate("MinesweeperAbout", u"<a href='https://github.com/monkecoder/Minesweeper.git'>Minesweeper on GitHub</a>", None))
        self.label_3.setText(QCoreApplication.translate("MinesweeperAbout", u"....................................................................................................\n"
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

