from qgis.PyQt import QtWidgets

from .impact_table_dialog import Ui_ImpactTableDialog


class ImpactTable(QtWidgets.QDialog, Ui_ImpactTableDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tbl_impacts.setColumnWidth(1, 300)
