# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kict_rain_forecast_dialog_base.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qgis.PyQt.QtCore import QCoreApplication, QMetaObject, QRect
from qgis.PyQt.QtWidgets import (
    QCheckBox,
    QComboBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(630, 520)
        self.radioButton = QRadioButton(Dialog)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setGeometry(QRect(40, 260, 101, 16))
        self.radioButton.setChecked(True)
        self.radioButton_2 = QRadioButton(Dialog)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setGeometry(QRect(180, 260, 101, 16))
        self.label = QLabel(Dialog)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(20, 230, 141, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(20, 10, 131, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(20, 350, 131, 16))
        self.lineEdit_5 = QLineEdit(Dialog)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(30, 380, 411, 20))
        self.pushButton_5 = QPushButton(Dialog)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setGeometry(QRect(450, 380, 31, 23))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(450, 480, 75, 23))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QRect(540, 480, 75, 23))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setGeometry(QRect(30, 50, 451, 22))
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setGeometry(QRect(30, 100, 451, 22))
        self.comboBox_3 = QComboBox(Dialog)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.setGeometry(QRect(30, 150, 451, 22))
        self.comboBox_4 = QComboBox(Dialog)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.setGeometry(QRect(30, 200, 451, 22))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(30, 30, 151, 16))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(30, 80, 151, 16))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QRect(30, 130, 151, 16))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(30, 180, 151, 16))
        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setGeometry(QRect(30, 440, 221, 16))

        # 모델 상태 표시 라벨
        self.label_model_status = QLabel(Dialog)
        self.label_model_status.setObjectName("label_model_status")
        self.label_model_status.setGeometry(QRect(40, 290, 400, 16))

        # 모델 다운로드 버튼
        self.pushButton_download = QPushButton(Dialog)
        self.pushButton_download.setObjectName("pushButton_download")
        self.pushButton_download.setGeometry(QRect(450, 290, 120, 23))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", "KICT-RAIN-AI", None)
        )
        self.radioButton.setText(
            QCoreApplication.translate("Dialog", "Multi Target", None)
        )
        self.radioButton_2.setText(
            QCoreApplication.translate("Dialog", "Single Target", None)
        )
        self.label.setText(QCoreApplication.translate("Dialog", "Model Select", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", "Input Data", None))
        self.label_3.setText(
            QCoreApplication.translate("Dialog", "Output Folder", None)
        )
        self.lineEdit_5.setText(
            QCoreApplication.translate("Dialog", "C:\\User\\Downloads", None)
        )
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", "...", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", "&Predict", None))
        # if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("Dialog", "P", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", "&Cancel", None))
        self.comboBox.setItemText(
            0,
            QCoreApplication.translate(
                "Dialog", "RDR_CMP_HSP_PUB_202208082130-525x625-1km.asc", None
            ),
        )

        self.comboBox.setCurrentText(
            QCoreApplication.translate(
                "Dialog", "RDR_CMP_HSP_PUB_202208082130-525x625-1km.asc", None
            )
        )
        self.comboBox_2.setItemText(
            0,
            QCoreApplication.translate(
                "Dialog", "RDR_CMP_HSP_PUB_202208082140-525x625-1km.asc", None
            ),
        )

        self.comboBox_3.setItemText(
            0,
            QCoreApplication.translate(
                "Dialog", "RDR_CMP_HSP_PUB_202208082150-525x625-1km.asc", None
            ),
        )

        self.comboBox_4.setItemText(
            0,
            QCoreApplication.translate(
                "Dialog", "RDR_CMP_HSP_PUB_202208082200-525x625-1km.asc", None
            ),
        )

        self.label_4.setText(
            QCoreApplication.translate("Dialog", "Data from 30 minutes ago", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("Dialog", "Data from 20 minutes ago", None)
        )
        self.label_6.setText(
            QCoreApplication.translate("Dialog", "Data from 10 minutes ago", None)
        )
        self.label_7.setText(
            QCoreApplication.translate("Dialog", "Data at forecasting time", None)
        )
        self.checkBox.setText(
            QCoreApplication.translate("Dialog", "Add results to the map", None)
        )

        # 새로 추가된 위젯 텍스트 설정
        self.label_model_status.setText(
            QCoreApplication.translate("Dialog", "모델 상태: 확인 중...", None)
        )
        self.pushButton_download.setText(
            QCoreApplication.translate("Dialog", "모델 다운로드", None)
        )

    # retranslateUi
