# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(881, 527)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(340, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(400, 80, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.leibie = QtWidgets.QComboBox(Form)
        self.leibie.setGeometry(QtCore.QRect(500, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.leibie.setFont(font)
        self.leibie.setObjectName("leibie")
        self.leibie.addItem("")
        self.leibie.addItem("")
        self.leibie.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.key_line = QtWidgets.QLineEdit(Form)
        self.key_line.setGeometry(QtCore.QRect(120, 70, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.key_line.setFont(font)
        self.key_line.setObjectName("key_line")
        self.start_search = QtWidgets.QPushButton(Form)
        self.start_search.setGeometry(QtCore.QRect(694, 72, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.start_search.setFont(font)
        self.start_search.setObjectName("start_search")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(40, 130, 811, 381))
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setOpenLinks(True)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        self.start_search.clicked.connect(Form.search_file)
        self.leibie.currentTextChanged['QString'].connect(Form.change_leibie)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "CL资源搜索工具"))
        self.label_2.setText(_translate("Form", "选择板块："))
        self.leibie.setItemText(0, _translate("Form", "技术讨论区"))
        self.leibie.setItemText(1, _translate("Form", "达盖尔的旗帜"))
        self.leibie.setItemText(2, _translate("Form", "新时代的我们"))
        self.label_3.setText(_translate("Form", "关键词："))
        self.start_search.setText(_translate("Form", "开始搜索"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
