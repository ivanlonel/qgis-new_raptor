# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\impact_table_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImpactTableDialog(object):
    def setupUi(self, ImpactTableDialog):
        ImpactTableDialog.setObjectName("ImpactTableDialog")
        ImpactTableDialog.resize(560, 315)
        self.verticalLayout = QtWidgets.QVBoxLayout(ImpactTableDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tbl_impacts = QtWidgets.QTableWidget(ImpactTableDialog)
        self.tbl_impacts.setAlternatingRowColors(True)
        self.tbl_impacts.setObjectName("tbl_impacts")
        self.tbl_impacts.setColumnCount(3)
        self.tbl_impacts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_impacts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_impacts.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_impacts.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tbl_impacts)

        self.retranslateUi(ImpactTableDialog)
        QtCore.QMetaObject.connectSlotsByName(ImpactTableDialog)

    def retranslateUi(self, ImpactTableDialog):
        _translate = QtCore.QCoreApplication.translate
        ImpactTableDialog.setWindowTitle(_translate("ImpactTableDialog", "Dialog"))
        self.tbl_impacts.setSortingEnabled(True)
        item = self.tbl_impacts.horizontalHeaderItem(0)
        item.setText(_translate("ImpactTableDialog", "Project"))
        item = self.tbl_impacts.horizontalHeaderItem(1)
        item.setText(_translate("ImpactTableDialog", "Type"))
        item = self.tbl_impacts.horizontalHeaderItem(2)
        item.setText(_translate("ImpactTableDialog", "Distance"))

