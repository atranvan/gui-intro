from PyQt5 import QtCore, QtGui


class DataModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.headerdata = ['Date', 'Experiment Name', 'Result']
        self.arraydata = [['', '', '']]

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.arraydata)

    def columnCount(self, parent=None, *args, **kwargs):
        return len(self.arraydata[0])

    def data(self, QModelIndex, role=None):
        if not QModelIndex.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        return QtCore.QVariant(str(self.arraydata[QModelIndex.row()][QModelIndex.column()]))

    def headerData(self, p_int, Qt_Orientation, role=None):
        if Qt_Orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.headerdata[p_int])
        if Qt_Orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return int(p_int)
        return QtCore.QVariant()

    def add_entry(self, entry):
        if self.arraydata[0] == ['', '', '']:
            self.arraydata[0] = entry
        else:
            self.arraydata.append(entry)
        self.layoutChanged.emit()

    def remove_entry(self, row_i):
        self.arraydata.pop(row_i)
        self.layoutChanged.emit()