import sys
from PyQt5 import QtWidgets
from Designs import mainWindow
from Models import Data


# noinspection PyBroadException
class MainApp(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        # inherit from parent class, setup UI
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # set up data model
        self.dataModel = Data.DataModel(self)
        self.mainTableView.setModel(self.dataModel)

        # map button bindings
        self.addButton.clicked.connect(self.add_button)
        self.removeButton.clicked.connect(self.remove_button)

    def get_entry(self):
        # return an entry based on user UI input
        date = self.dateEdit.text()
        experiment_name = self.experimentNameEdit.text()
        result = self.resultEdit.text()

        return date, experiment_name, result

    def add_button(self):
        date, experiment_name, result = self.get_entry()
        self.dataModel.add_entry([date, experiment_name, result])

    def remove_button(self):
        try:
            selected_trial = self.mainTableView.selectionModel().selectedRows()[0].row()
            self.dataModel.remove_entry(selected_trial)
        except:
            print('No entry selected')
            pass


# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainApp()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()