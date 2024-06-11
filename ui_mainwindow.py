from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QAction, QIcon)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMenu, QMenuBar,
                               QPushButton, QSizePolicy, QStatusBar, QVBoxLayout, QWidget, QApplication)
from game import Game


class Ui_MainWindow(object):
    def __init__(self):
        self.game = Game()

        self.reroll_count = 0

        self.can_score = False

        self.icon = QIcon()
        self.icon.addFile(u"img/png/d6_blank.png", QSize(), QIcon.Normal, QIcon.Off)

        self.icon_d1 = QIcon()
        self.icon_d2 = QIcon()
        self.icon_d3 = QIcon()
        self.icon_d4 = QIcon()
        self.icon_d5 = QIcon()
        self.icon_d6 = QIcon()

        self.icon_d1.addFile(u"img/png/d6_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_d2.addFile(u"img/png/d6_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_d3.addFile(u"img/png/d6_3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_d4.addFile(u"img/png/d6_4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_d5.addFile(u"img/png/d6_5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_d6.addFile(u"img/png/d6_6.png", QSize(), QIcon.Normal, QIcon.Off)

        self.dice_icons = {
            1: self.icon_d1,
            2: self.icon_d2,
            3: self.icon_d3,
            4: self.icon_d4,
            5: self.icon_d5,
            6: self.icon_d6
        }

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Yahtzee 1.0")
        MainWindow.setFixedSize(384, 456)

        self.actionNew_Game = QAction(MainWindow)
        self.actionNew_Game.setObjectName(u"actionNew_Game")
        self.actionNew_Game.triggered.connect(lambda: self.reset_game())

        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionQuit.triggered.connect(QApplication.instance().quit)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 361, 92))

        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.btn_dice1 = QPushButton(self.verticalLayoutWidget)
        self.btn_dice1.setObjectName(u"btn_dice1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dice1.sizePolicy().hasHeightForWidth())
        self.btn_dice1.setSizePolicy(sizePolicy)
        self.btn_dice1.setIcon(self.icon)
        self.btn_dice1.setIconSize(QSize(48, 48))
        self.btn_dice1.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_dice1)

        self.btn_dice2 = QPushButton(self.verticalLayoutWidget)
        self.btn_dice2.setObjectName(u"btn_dice2")
        sizePolicy.setHeightForWidth(self.btn_dice2.sizePolicy().hasHeightForWidth())
        self.btn_dice2.setSizePolicy(sizePolicy)
        self.btn_dice2.setIcon(self.icon)
        self.btn_dice2.setIconSize(QSize(48, 48))
        self.btn_dice2.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_dice2)

        self.btn_dice3 = QPushButton(self.verticalLayoutWidget)
        self.btn_dice3.setObjectName(u"btn_dice3")
        sizePolicy.setHeightForWidth(self.btn_dice3.sizePolicy().hasHeightForWidth())
        self.btn_dice3.setSizePolicy(sizePolicy)
        self.btn_dice3.setIcon(self.icon)
        self.btn_dice3.setIconSize(QSize(48, 48))
        self.btn_dice3.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_dice3)

        self.btn_dice4 = QPushButton(self.verticalLayoutWidget)
        self.btn_dice4.setObjectName(u"btn_dice4")
        sizePolicy.setHeightForWidth(self.btn_dice4.sizePolicy().hasHeightForWidth())
        self.btn_dice4.setSizePolicy(sizePolicy)
        self.btn_dice4.setIcon(self.icon)
        self.btn_dice4.setIconSize(QSize(48, 48))
        self.btn_dice4.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_dice4)

        self.btn_dice5 = QPushButton(self.verticalLayoutWidget)
        self.btn_dice5.setObjectName(u"btn_dice5")
        sizePolicy.setHeightForWidth(self.btn_dice5.sizePolicy().hasHeightForWidth())
        self.btn_dice5.setSizePolicy(sizePolicy)
        self.btn_dice5.setIcon(self.icon)
        self.btn_dice5.setIconSize(QSize(48, 48))
        self.btn_dice5.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_dice5)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.btn_roll = QPushButton(self.verticalLayoutWidget)
        self.btn_roll.setObjectName(u"btn_roll")
        self.btn_roll.clicked.connect(lambda: self.roll_hand())

        self.horizontalLayout_2.addWidget(self.btn_roll)

        self.btn_reroll = QPushButton(self.verticalLayoutWidget)
        self.btn_reroll.setObjectName(u"btn_reroll")
        self.btn_reroll.clicked.connect(lambda: self.reroll_hand())
        self.btn_reroll.setDisabled(True)

        self.horizontalLayout_2.addWidget(self.btn_reroll)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 110, 361, 262))

        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.btn_aces = QPushButton(self.gridLayoutWidget)
        self.btn_aces.setObjectName(u"btn_aces")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_aces.sizePolicy().hasHeightForWidth())
        self.btn_aces.setSizePolicy(sizePolicy1)
        self.btn_aces.setMaximumSize(QSize(48, 16777215))
        self.btn_aces.clicked.connect(lambda: self.score_hand('aces'))

        self.gridLayout_2.addWidget(self.btn_aces, 0, 2, 1, 1)

        self.btn_threes = QPushButton(self.gridLayoutWidget)
        self.btn_threes.setObjectName(u"btn_threes")
        sizePolicy1.setHeightForWidth(self.btn_threes.sizePolicy().hasHeightForWidth())
        self.btn_threes.setSizePolicy(sizePolicy1)
        self.btn_threes.setMaximumSize(QSize(48, 16777215))
        self.btn_threes.clicked.connect(lambda: self.score_hand('threes'))

        self.gridLayout_2.addWidget(self.btn_threes, 2, 2, 1, 1)

        self.lbl_fives = QLabel(self.gridLayoutWidget)
        self.lbl_fives.setObjectName(u"lbl_fives")

        self.gridLayout_2.addWidget(self.lbl_fives, 4, 0, 1, 1)

        self.lbl_aces = QLabel(self.gridLayoutWidget)
        self.lbl_aces.setObjectName(u"lbl_aces")

        self.gridLayout_2.addWidget(self.lbl_aces, 0, 0, 1, 1)

        self.lbl_threes = QLabel(self.gridLayoutWidget)
        self.lbl_threes.setObjectName(u"lbl_threes")

        self.gridLayout_2.addWidget(self.lbl_threes, 2, 0, 1, 1)

        self.btn_fours = QPushButton(self.gridLayoutWidget)
        self.btn_fours.setObjectName(u"btn_fours")
        sizePolicy1.setHeightForWidth(self.btn_fours.sizePolicy().hasHeightForWidth())
        self.btn_fours.setSizePolicy(sizePolicy1)
        self.btn_fours.setMaximumSize(QSize(48, 16777215))
        self.btn_fours.clicked.connect(lambda: self.score_hand('fours'))

        self.gridLayout_2.addWidget(self.btn_fours, 3, 2, 1, 1)

        self.score_aces = QLineEdit(self.gridLayoutWidget)
        self.score_aces.setObjectName(u"score_aces")
        sizePolicy1.setHeightForWidth(self.score_aces.sizePolicy().hasHeightForWidth())
        self.score_aces.setSizePolicy(sizePolicy1)
        self.score_aces.setMaximumSize(QSize(36, 16777215))
        self.score_aces.setAlignment(Qt.AlignCenter)
        self.score_aces.setReadOnly(True)

        self.gridLayout_2.addWidget(self.score_aces, 0, 1, 1, 1)

        self.btn_twos = QPushButton(self.gridLayoutWidget)
        self.btn_twos.setObjectName(u"btn_twos")
        sizePolicy1.setHeightForWidth(self.btn_twos.sizePolicy().hasHeightForWidth())
        self.btn_twos.setSizePolicy(sizePolicy1)
        self.btn_twos.setMaximumSize(QSize(48, 16777215))
        self.btn_twos.clicked.connect(lambda: self.score_hand('twos'))

        self.gridLayout_2.addWidget(self.btn_twos, 1, 2, 1, 1)

        self.score_fours = QLineEdit(self.gridLayoutWidget)
        self.score_fours.setObjectName(u"score_fours")
        sizePolicy1.setHeightForWidth(self.score_fours.sizePolicy().hasHeightForWidth())
        self.score_fours.setSizePolicy(sizePolicy1)
        self.score_fours.setMaximumSize(QSize(36, 16777215))
        self.score_fours.setAlignment(Qt.AlignCenter)
        self.score_fours.setReadOnly(True)

        self.gridLayout_2.addWidget(self.score_fours, 3, 1, 1, 1)

        self.lbl_twos = QLabel(self.gridLayoutWidget)
        self.lbl_twos.setObjectName(u"lbl_twos")

        self.gridLayout_2.addWidget(self.lbl_twos, 1, 0, 1, 1)

        self.score_threes = QLineEdit(self.gridLayoutWidget)
        self.score_threes.setObjectName(u"score_threes")
        sizePolicy1.setHeightForWidth(self.score_threes.sizePolicy().hasHeightForWidth())
        self.score_threes.setSizePolicy(sizePolicy1)
        self.score_threes.setMaximumSize(QSize(36, 16777215))
        self.score_threes.setAlignment(Qt.AlignCenter)
        self.score_threes.setReadOnly(True)

        self.gridLayout_2.addWidget(self.score_threes, 2, 1, 1, 1)

        self.score_twos = QLineEdit(self.gridLayoutWidget)
        self.score_twos.setObjectName(u"score_twos")
        sizePolicy1.setHeightForWidth(self.score_twos.sizePolicy().hasHeightForWidth())
        self.score_twos.setSizePolicy(sizePolicy1)
        self.score_twos.setMaximumSize(QSize(36, 16777215))
        self.score_twos.setAlignment(Qt.AlignCenter)
        self.score_twos.setReadOnly(True)

        self.gridLayout_2.addWidget(self.score_twos, 1, 1, 1, 1)

        self.lbl_fours = QLabel(self.gridLayoutWidget)
        self.lbl_fours.setObjectName(u"lbl_fours")

        self.gridLayout_2.addWidget(self.lbl_fours, 3, 0, 1, 1)

        self.btn_sixes = QPushButton(self.gridLayoutWidget)
        self.btn_sixes.setObjectName(u"btn_sixes")
        sizePolicy1.setHeightForWidth(self.btn_sixes.sizePolicy().hasHeightForWidth())
        self.btn_sixes.setSizePolicy(sizePolicy1)
        self.btn_sixes.setMaximumSize(QSize(48, 16777215))
        self.btn_sixes.clicked.connect(lambda: self.score_hand('sixes'))

        self.gridLayout_2.addWidget(self.btn_sixes, 5, 2, 1, 1)

        self.lbl_sixes = QLabel(self.gridLayoutWidget)
        self.lbl_sixes.setObjectName(u"lbl_sixes")

        self.gridLayout_2.addWidget(self.lbl_sixes, 5, 0, 1, 1)

        self.score_fives = QLineEdit(self.gridLayoutWidget)
        self.score_fives.setObjectName(u"score_fives")
        sizePolicy1.setHeightForWidth(self.score_fives.sizePolicy().hasHeightForWidth())
        self.score_fives.setSizePolicy(sizePolicy1)
        self.score_fives.setMaximumSize(QSize(36, 16777215))
        self.score_fives.setAlignment(Qt.AlignCenter)
        self.score_fives.setReadOnly(True)

        self.gridLayout_2.addWidget(self.score_fives, 4, 1, 1, 1)

        self.btn_fives = QPushButton(self.gridLayoutWidget)
        self.btn_fives.setObjectName(u"btn_fives")
        sizePolicy1.setHeightForWidth(self.btn_fives.sizePolicy().hasHeightForWidth())
        self.btn_fives.setSizePolicy(sizePolicy1)
        self.btn_fives.setMaximumSize(QSize(48, 16777215))
        self.btn_fives.clicked.connect(lambda: self.score_hand('fives'))

        self.gridLayout_2.addWidget(self.btn_fives, 4, 2, 1, 1)

        self.score_sixes = QLineEdit(self.gridLayoutWidget)
        self.score_sixes.setObjectName(u"score_sixes")
        sizePolicy1.setHeightForWidth(self.score_sixes.sizePolicy().hasHeightForWidth())
        self.score_sixes.setSizePolicy(sizePolicy1)
        self.score_sixes.setMaximumSize(QSize(36, 16777215))
        self.score_sixes.setAlignment(Qt.AlignCenter)
        self.score_sixes.setReadOnly(True)

        self.gridLayout_2.addWidget(self.score_sixes, 5, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_2.addWidget(self.label, 6, 0, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.score_3kind = QLineEdit(self.gridLayoutWidget)
        self.score_3kind.setObjectName(u"score_3kind")
        sizePolicy1.setHeightForWidth(self.score_3kind.sizePolicy().hasHeightForWidth())
        self.score_3kind.setSizePolicy(sizePolicy1)
        self.score_3kind.setMaximumSize(QSize(36, 16777215))
        self.score_3kind.setAlignment(Qt.AlignCenter)
        self.score_3kind.setReadOnly(True)

        self.gridLayout_3.addWidget(self.score_3kind, 0, 1, 1, 1)

        self.lbl_yahtzee = QLabel(self.gridLayoutWidget)
        self.lbl_yahtzee.setObjectName(u"lbl_yahtzee")

        self.gridLayout_3.addWidget(self.lbl_yahtzee, 5, 0, 1, 1)

        self.score_fullhouse = QLineEdit(self.gridLayoutWidget)
        self.score_fullhouse.setObjectName(u"score_fullhouse")
        sizePolicy1.setHeightForWidth(self.score_fullhouse.sizePolicy().hasHeightForWidth())
        self.score_fullhouse.setSizePolicy(sizePolicy1)
        self.score_fullhouse.setMaximumSize(QSize(36, 16777215))
        self.score_fullhouse.setAlignment(Qt.AlignCenter)
        self.score_fullhouse.setReadOnly(True)

        self.gridLayout_3.addWidget(self.score_fullhouse, 2, 1, 1, 1)

        self.lbl_fullhouse = QLabel(self.gridLayoutWidget)
        self.lbl_fullhouse.setObjectName(u"lbl_fullhouse")

        self.gridLayout_3.addWidget(self.lbl_fullhouse, 2, 0, 1, 1)

        self.score_yahtzee = QLineEdit(self.gridLayoutWidget)
        self.score_yahtzee.setObjectName(u"score_yahtzee")
        sizePolicy1.setHeightForWidth(self.score_yahtzee.sizePolicy().hasHeightForWidth())
        self.score_yahtzee.setSizePolicy(sizePolicy1)
        self.score_yahtzee.setMaximumSize(QSize(36, 16777215))
        self.score_yahtzee.setAlignment(Qt.AlignCenter)
        self.score_yahtzee.setReadOnly(True)

        self.gridLayout_3.addWidget(self.score_yahtzee, 5, 1, 1, 1)

        self.btn_3kind = QPushButton(self.gridLayoutWidget)
        self.btn_3kind.setObjectName(u"btn_3kind")
        sizePolicy1.setHeightForWidth(self.btn_3kind.sizePolicy().hasHeightForWidth())
        self.btn_3kind.setSizePolicy(sizePolicy1)
        self.btn_3kind.setMaximumSize(QSize(48, 16777215))
        self.btn_3kind.clicked.connect(lambda: self.score_hand('3_kind'))

        self.gridLayout_3.addWidget(self.btn_3kind, 0, 2, 1, 1)

        self.btn_fullhouse = QPushButton(self.gridLayoutWidget)
        self.btn_fullhouse.setObjectName(u"btn_fullhouse")
        sizePolicy1.setHeightForWidth(self.btn_fullhouse.sizePolicy().hasHeightForWidth())
        self.btn_fullhouse.setSizePolicy(sizePolicy1)
        self.btn_fullhouse.setMaximumSize(QSize(48, 16777215))
        self.btn_fullhouse.clicked.connect(lambda: self.score_hand('full_house'))

        self.gridLayout_3.addWidget(self.btn_fullhouse, 2, 2, 1, 1)

        self.lbl_3kind = QLabel(self.gridLayoutWidget)
        self.lbl_3kind.setObjectName(u"lbl_3kind")

        self.gridLayout_3.addWidget(self.lbl_3kind, 0, 0, 1, 1)

        self.btn_4kind = QPushButton(self.gridLayoutWidget)
        self.btn_4kind.setObjectName(u"btn_4kind")
        sizePolicy1.setHeightForWidth(self.btn_4kind.sizePolicy().hasHeightForWidth())
        self.btn_4kind.setSizePolicy(sizePolicy1)
        self.btn_4kind.setMaximumSize(QSize(48, 16777215))
        self.btn_4kind.clicked.connect(lambda: self.score_hand('4_kind'))

        self.gridLayout_3.addWidget(self.btn_4kind, 1, 2, 1, 1)

        self.score_4kind = QLineEdit(self.gridLayoutWidget)
        self.score_4kind.setObjectName(u"score_4kind")
        sizePolicy1.setHeightForWidth(self.score_4kind.sizePolicy().hasHeightForWidth())
        self.score_4kind.setSizePolicy(sizePolicy1)
        self.score_4kind.setMaximumSize(QSize(36, 16777215))
        self.score_4kind.setAlignment(Qt.AlignCenter)
        self.score_4kind.setReadOnly(True)

        self.gridLayout_3.addWidget(self.score_4kind, 1, 1, 1, 1)

        self.score_smstraight = QLineEdit(self.gridLayoutWidget)
        self.score_smstraight.setObjectName(u"score_smstraight")
        sizePolicy1.setHeightForWidth(self.score_smstraight.sizePolicy().hasHeightForWidth())
        self.score_smstraight.setSizePolicy(sizePolicy1)
        self.score_smstraight.setMaximumSize(QSize(36, 16777215))
        self.score_smstraight.setAlignment(Qt.AlignCenter)
        self.score_smstraight.setReadOnly(True)

        self.gridLayout_3.addWidget(self.score_smstraight, 3, 1, 1, 1)

        self.btn_yahtzee = QPushButton(self.gridLayoutWidget)
        self.btn_yahtzee.setObjectName(u"btn_yahtzee")
        sizePolicy1.setHeightForWidth(self.btn_yahtzee.sizePolicy().hasHeightForWidth())
        self.btn_yahtzee.setSizePolicy(sizePolicy1)
        self.btn_yahtzee.setMaximumSize(QSize(48, 16777215))
        self.btn_yahtzee.clicked.connect(lambda: self.score_hand('yahtzee'))

        self.gridLayout_3.addWidget(self.btn_yahtzee, 5, 2, 1, 1)

        self.lbl_chance = QLabel(self.gridLayoutWidget)
        self.lbl_chance.setObjectName(u"lbl_chance")

        self.gridLayout_3.addWidget(self.lbl_chance, 8, 0, 1, 1)

        self.btn_smstraight = QPushButton(self.gridLayoutWidget)
        self.btn_smstraight.setObjectName(u"btn_smstraight")
        sizePolicy1.setHeightForWidth(self.btn_smstraight.sizePolicy().hasHeightForWidth())
        self.btn_smstraight.setSizePolicy(sizePolicy1)
        self.btn_smstraight.setMaximumSize(QSize(48, 16777215))
        self.btn_smstraight.clicked.connect(lambda: self.score_hand('sm_straight'))

        self.gridLayout_3.addWidget(self.btn_smstraight, 3, 2, 1, 1)

        self.btn_lgstraight = QPushButton(self.gridLayoutWidget)
        self.btn_lgstraight.setObjectName(u"btn_lgstraight")
        sizePolicy1.setHeightForWidth(self.btn_lgstraight.sizePolicy().hasHeightForWidth())
        self.btn_lgstraight.setSizePolicy(sizePolicy1)
        self.btn_lgstraight.setMaximumSize(QSize(48, 16777215))
        self.btn_lgstraight.clicked.connect(lambda: self.score_hand('lg_straight'))

        self.gridLayout_3.addWidget(self.btn_lgstraight, 4, 2, 1, 1)

        self.lbl_lgstraight = QLabel(self.gridLayoutWidget)
        self.lbl_lgstraight.setObjectName(u"lbl_lgstraight")

        self.gridLayout_3.addWidget(self.lbl_lgstraight, 4, 0, 1, 1)

        self.score_lgstraight = QLineEdit(self.gridLayoutWidget)
        self.score_lgstraight.setObjectName(u"score_lgstraight")
        sizePolicy1.setHeightForWidth(self.score_lgstraight.sizePolicy().hasHeightForWidth())
        self.score_lgstraight.setSizePolicy(sizePolicy1)
        self.score_lgstraight.setMaximumSize(QSize(36, 16777215))
        self.score_lgstraight.setAlignment(Qt.AlignCenter)
        self.score_lgstraight.setReadOnly(True)

        self.gridLayout_3.addWidget(self.score_lgstraight, 4, 1, 1, 1)

        self.lbl_4kind = QLabel(self.gridLayoutWidget)
        self.lbl_4kind.setObjectName(u"lbl_4kind")

        self.gridLayout_3.addWidget(self.lbl_4kind, 1, 0, 1, 1)

        self.lbl_smstraight = QLabel(self.gridLayoutWidget)
        self.lbl_smstraight.setObjectName(u"lbl_smstraight")

        self.gridLayout_3.addWidget(self.lbl_smstraight, 3, 0, 1, 1)

        self.btn_chance = QPushButton(self.gridLayoutWidget)
        self.btn_chance.setObjectName(u"btn_chance")
        sizePolicy1.setHeightForWidth(self.btn_chance.sizePolicy().hasHeightForWidth())
        self.btn_chance.setSizePolicy(sizePolicy1)
        self.btn_chance.setMaximumSize(QSize(48, 16777215))
        self.btn_chance.clicked.connect(lambda: self.score_hand('chance'))

        self.gridLayout_3.addWidget(self.btn_chance, 8, 2, 1, 1)

        self.score_chance = QLineEdit(self.gridLayoutWidget)
        self.score_chance.setObjectName(u"score_chance")
        sizePolicy1.setHeightForWidth(self.score_chance.sizePolicy().hasHeightForWidth())
        self.score_chance.setSizePolicy(sizePolicy1)
        self.score_chance.setMaximumSize(QSize(36, 16777215))
        self.score_chance.setAlignment(Qt.AlignCenter)
        self.score_chance.setReadOnly(True)

        self.gridLayout_3.addWidget(self.score_chance, 8, 1, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(90, 380, 181, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_total = QLabel(self.horizontalLayoutWidget_2)
        self.lbl_total.setObjectName(u"lbl_total")
        self.lbl_total.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lbl_total)

        self.lbl_total_score = QLabel(self.horizontalLayoutWidget_2)
        self.lbl_total_score.setObjectName(u"lbl_total_score")
        self.lbl_total_score.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lbl_total_score)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 384, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionNew_Game)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Yahtzee 1.0", u"Yahtzee 1.0", None))
        self.actionNew_Game.setText(QCoreApplication.translate("MainWindow", u"New Game...", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit...", None))
        self.btn_dice1.setText("")
        self.btn_dice2.setText("")
        self.btn_dice3.setText("")
        self.btn_dice4.setText("")
        self.btn_dice5.setText("")
        self.btn_roll.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.btn_reroll.setText(QCoreApplication.translate("MainWindow", u"Reroll", None))
        self.btn_aces.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.btn_threes.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.lbl_fives.setText(QCoreApplication.translate("MainWindow", u"Fives", None))
        self.lbl_aces.setText(QCoreApplication.translate("MainWindow", u"Aces", None))
        self.lbl_threes.setText(QCoreApplication.translate("MainWindow", u"Threes", None))
        self.btn_fours.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.score_aces.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_twos.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.score_fours.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_twos.setText(QCoreApplication.translate("MainWindow", u"Twos", None))
        self.score_threes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.score_twos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_fours.setText(QCoreApplication.translate("MainWindow", u"Fours", None))
        self.btn_sixes.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.lbl_sixes.setText(QCoreApplication.translate("MainWindow", u"Sixes", None))
        self.score_fives.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_fives.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.score_sixes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText("")
        self.score_3kind.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_yahtzee.setText(QCoreApplication.translate("MainWindow", u"Yahtzee", None))
        self.score_fullhouse.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_fullhouse.setText(QCoreApplication.translate("MainWindow", u"Full House", None))
        self.score_yahtzee.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_3kind.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.btn_fullhouse.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.lbl_3kind.setText(QCoreApplication.translate("MainWindow", u"3 of a Kind", None))
        self.btn_4kind.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.score_4kind.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.score_smstraight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_yahtzee.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.lbl_chance.setText(QCoreApplication.translate("MainWindow", u"Chance", None))
        self.btn_smstraight.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.btn_lgstraight.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.lbl_lgstraight.setText(QCoreApplication.translate("MainWindow", u"Lg Straight", None))
        self.score_lgstraight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_4kind.setText(QCoreApplication.translate("MainWindow", u"4 of a Kind", None))
        self.lbl_smstraight.setText(QCoreApplication.translate("MainWindow", u"Sm Straight", None))
        self.btn_chance.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.score_chance.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_total.setText(QCoreApplication.translate("MainWindow", u"Total Score:", None))
        self.lbl_total_score.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

    def update_icons(self):
        curr_hand = self.game.get_hand()

        self.btn_dice1.setIcon(self.dice_icons[curr_hand[0]])
        self.btn_dice2.setIcon(self.dice_icons[curr_hand[1]])
        self.btn_dice3.setIcon(self.dice_icons[curr_hand[2]])
        self.btn_dice4.setIcon(self.dice_icons[curr_hand[3]])
        self.btn_dice5.setIcon(self.dice_icons[curr_hand[4]])

    def roll_hand(self):
        self.game.roll_hand()
        self.update_icons()

        self.reroll_count = 2
        self.btn_roll.setDisabled(True)
        self.btn_reroll.setDisabled(False)
        self.can_score = True

    def reroll_hand(self):
        checked = [
            self.btn_dice1.isChecked(),
            self.btn_dice2.isChecked(),
            self.btn_dice3.isChecked(),
            self.btn_dice4.isChecked(),
            self.btn_dice5.isChecked()
        ]

        self.reroll_count -= 1

        self.game.reroll_hand(checked)
        self.update_icons()

        if self.reroll_count == 0:
            self.btn_reroll.setDisabled(True)

        self.btn_dice1.setChecked(False)
        self.btn_dice2.setChecked(False)
        self.btn_dice3.setChecked(False)
        self.btn_dice4.setChecked(False)
        self.btn_dice5.setChecked(False)

    def score_hand(self, cat):
        print(f'Attempting to score: {cat}')

        if self.can_score:
            curr_scores = self.game.score_hand(cat)

            self.score_aces.setText(str(curr_scores['aces']))
            self.score_twos.setText(str(curr_scores['twos']))
            self.score_threes.setText(str(curr_scores['threes']))
            self.score_fours.setText(str(curr_scores['fours']))
            self.score_fives.setText(str(curr_scores['fives']))
            self.score_sixes.setText(str(curr_scores['sixes']))
            self.score_3kind.setText(str(curr_scores['3_kind']))
            self.score_4kind.setText(str(curr_scores['4_kind']))
            self.score_fullhouse.setText(str(curr_scores['full_house']))
            self.score_smstraight.setText(str(curr_scores['sm_straight']))
            self.score_lgstraight.setText(str(curr_scores['lg_straight']))
            self.score_yahtzee.setText(str(curr_scores['yahtzee']))
            self.score_chance.setText(str(curr_scores['chance']))
            self.can_score = False

            if cat == 'aces':
                self.btn_aces.setDisabled(True)
            elif cat == 'twos':
                self.btn_twos.setDisabled(True)
            elif cat == 'threes':
                self.btn_threes.setDisabled(True)
            elif cat == 'fours':
                self.btn_fours.setDisabled(True)
            elif cat == 'fives':
                self.btn_fives.setDisabled(True)
            elif cat == 'sixes':
                self.btn_sixes.setDisabled(True)
            elif cat == '3_kind':
                self.btn_3kind.setDisabled(True)
            elif cat == '4_kind':
                self.btn_4kind.setDisabled(True)
            elif cat == 'full_house':
                self.btn_fullhouse.setDisabled(True)
            elif cat == 'sm_straight':
                self.btn_smstraight.setDisabled(True)
            elif cat == 'lg_straight':
                self.btn_lgstraight.setDisabled(True)
            elif cat == 'yahtzee':
                self.btn_yahtzee.setDisabled(True)
            elif cat == 'chance':
                self.btn_chance.setDisabled(True)

        self.btn_dice1.setChecked(False)
        self.btn_dice2.setChecked(False)
        self.btn_dice3.setChecked(False)
        self.btn_dice4.setChecked(False)
        self.btn_dice5.setChecked(False)

        self.update_total()
        self.btn_roll.setDisabled(False)
        self.btn_reroll.setDisabled(True)

    def update_total(self):
        total = self.game.get_total()
        self.lbl_total_score.setText(str(total))

    def reset_game(self):
        self.game = Game()

        self.btn_dice1.setIcon(self.icon)
        self.btn_dice2.setIcon(self.icon)
        self.btn_dice3.setIcon(self.icon)
        self.btn_dice4.setIcon(self.icon)
        self.btn_dice5.setIcon(self.icon)

        self.btn_roll.setDisabled(False)
        self.btn_reroll.setDisabled(True)

        self.update_total()

        self.score_aces.setText('')
        self.score_twos.setText('')
        self.score_threes.setText('')
        self.score_fours.setText('')
        self.score_fives.setText('')
        self.score_sixes.setText('')
        self.score_3kind.setText('')
        self.score_4kind.setText('')
        self.score_fullhouse.setText('')
        self.score_smstraight.setText('')
        self.score_lgstraight.setText('')
        self.score_yahtzee.setText('')
        self.score_chance.setText('')

        self.btn_aces.setDisabled(False)
        self.btn_twos.setDisabled(False)
        self.btn_threes.setDisabled(False)
        self.btn_fours.setDisabled(False)
        self.btn_fives.setDisabled(False)
        self.btn_sixes.setDisabled(False)
        self.btn_3kind.setDisabled(False)
        self.btn_4kind.setDisabled(False)
        self.btn_fullhouse.setDisabled(False)
        self.btn_smstraight.setDisabled(False)
        self.btn_lgstraight.setDisabled(False)
        self.btn_yahtzee.setDisabled(False)
        self.btn_chance.setDisabled(False)




