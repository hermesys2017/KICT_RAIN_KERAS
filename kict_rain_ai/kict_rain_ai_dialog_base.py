# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kict_rain_ai_dialog_base.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qgis.PyQt.QtCore import QCoreApplication, QMetaObject, QRect
from qgis.PyQt.QtWidgets import (
    QCheckBox,
    QComboBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QVBoxLayout,
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
        # 입력 데이터 그룹박스 생성
        self.groupBox_input = QGroupBox(Dialog)
        self.groupBox_input.setObjectName("groupBox_input")
        self.groupBox_input.setGeometry(QRect(20, 30, 590, 200))
        self.groupBox_input.setTitle("입력 데이터 파일")

        # 입력 데이터 레이아웃 설정
        self.verticalLayout_input = QVBoxLayout(self.groupBox_input)
        self.verticalLayout_input.setObjectName("verticalLayout_input")

        # 첫 번째 파일 선택 (30분 전 데이터)
        self.horizontalLayout_1 = QHBoxLayout()
        self.label_4 = QLabel(self.groupBox_input)
        self.label_4.setObjectName("label_4")
        self.label_4.setMinimumWidth(150)
        self.horizontalLayout_1.addWidget(self.label_4)

        self.comboBox = QComboBox(self.groupBox_input)
        self.comboBox.addItem("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setEditable(True)
        self.horizontalLayout_1.addWidget(self.comboBox)

        self.pushButton_file1 = QPushButton(self.groupBox_input)
        self.pushButton_file1.setObjectName("pushButton_file1")
        self.pushButton_file1.setText("...")
        self.pushButton_file1.setMaximumWidth(30)
        self.horizontalLayout_1.addWidget(self.pushButton_file1)

        self.verticalLayout_input.addLayout(self.horizontalLayout_1)

        # 두 번째 파일 선택 (20분 전 데이터)
        self.horizontalLayout_2 = QHBoxLayout()
        self.label_5 = QLabel(self.groupBox_input)
        self.label_5.setObjectName("label_5")
        self.label_5.setMinimumWidth(150)
        self.horizontalLayout_2.addWidget(self.label_5)

        self.comboBox_2 = QComboBox(self.groupBox_input)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setEditable(True)
        self.horizontalLayout_2.addWidget(self.comboBox_2)

        self.pushButton_file2 = QPushButton(self.groupBox_input)
        self.pushButton_file2.setObjectName("pushButton_file2")
        self.pushButton_file2.setText("...")
        self.pushButton_file2.setMaximumWidth(30)
        self.horizontalLayout_2.addWidget(self.pushButton_file2)

        self.verticalLayout_input.addLayout(self.horizontalLayout_2)

        # 세 번째 파일 선택 (10분 전 데이터)
        self.horizontalLayout_3 = QHBoxLayout()
        self.label_6 = QLabel(self.groupBox_input)
        self.label_6.setObjectName("label_6")
        self.label_6.setMinimumWidth(150)
        self.horizontalLayout_3.addWidget(self.label_6)

        self.comboBox_3 = QComboBox(self.groupBox_input)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.setEditable(True)
        self.horizontalLayout_3.addWidget(self.comboBox_3)

        self.pushButton_file3 = QPushButton(self.groupBox_input)
        self.pushButton_file3.setObjectName("pushButton_file3")
        self.pushButton_file3.setText("...")
        self.pushButton_file3.setMaximumWidth(30)
        self.horizontalLayout_3.addWidget(self.pushButton_file3)

        self.verticalLayout_input.addLayout(self.horizontalLayout_3)

        # 네 번째 파일 선택 (예측 시점 데이터)
        self.horizontalLayout_4 = QHBoxLayout()
        self.label_7 = QLabel(self.groupBox_input)
        self.label_7.setObjectName("label_7")
        self.label_7.setMinimumWidth(150)
        self.horizontalLayout_4.addWidget(self.label_7)

        self.comboBox_4 = QComboBox(self.groupBox_input)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.setEditable(True)
        self.horizontalLayout_4.addWidget(self.comboBox_4)

        self.pushButton_file4 = QPushButton(self.groupBox_input)
        self.pushButton_file4.setObjectName("pushButton_file4")
        self.pushButton_file4.setText("...")
        self.pushButton_file4.setMaximumWidth(30)
        self.horizontalLayout_4.addWidget(self.pushButton_file4)

        self.verticalLayout_input.addLayout(self.horizontalLayout_4)

        # 일괄 파일 선택 버튼
        self.horizontalLayout_batch = QHBoxLayout()
        self.pushButton_batch = QPushButton(self.groupBox_input)
        self.pushButton_batch.setObjectName("pushButton_batch")
        self.pushButton_batch.setText("일괄 파일 선택")
        self.horizontalLayout_batch.addWidget(self.pushButton_batch)
        self.verticalLayout_input.addLayout(self.horizontalLayout_batch)
        # 라벨들은 이제 각 horizontalLayout 내에서 생성됨
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
        self.label_3.setText(
            QCoreApplication.translate("Dialog", "Output Folder", None)
        )
        self.lineEdit_5.setText(
            QCoreApplication.translate("Dialog", "C:\\User\\Downloads", None)
        )
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", "...", None))
        self.pushButton_file1.setText(QCoreApplication.translate("Dialog", "...", None))
        self.pushButton_file2.setText(QCoreApplication.translate("Dialog", "...", None))
        self.pushButton_file3.setText(QCoreApplication.translate("Dialog", "...", None))
        self.pushButton_file4.setText(QCoreApplication.translate("Dialog", "...", None))
        self.pushButton_batch.setText(
            QCoreApplication.translate("Dialog", "일괄 파일 선택", None)
        )
        self.groupBox_input.setTitle(
            QCoreApplication.translate("Dialog", "입력 데이터 파일", None)
        )
        self.pushButton.setText(QCoreApplication.translate("Dialog", "&Predict", None))
        # if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("Dialog", "P", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", "&Cancel", None))
        # ComboBox 초기값을 빈 값으로 설정
        self.comboBox.clear()
        self.comboBox_2.clear()
        self.comboBox_3.clear()
        self.comboBox_4.clear()

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
