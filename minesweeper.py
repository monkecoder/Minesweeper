"""Minesweeper game on PySide6."""

from pathlib import Path
from types import MappingProxyType

import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets

from gui.minesweeper_window_ui import Ui_MinesweeperWindow

BASE_PATH = Path(__file__).parent

CODE_COVERED = "c"              # cell is covered, default
CODE_COVERED_FLAG = "f"         # cell is covered, flag
CODE_UNCOVERED = "u"            # cell is uncovered, default
CODE_UNCOVERED_MINE = "m"       # cell is uncovered, bomb is here
CODE_UNCOVERED_MINE_OK = "o"    # cell is uncovered, bomb neutralized
CODE_UNCOVERED_MINE_BAD = "b"   # cell is uncovered, bom exploded

PICT_DICT = MappingProxyType({
    CODE_COVERED:            QtGui.QImage(BASE_PATH / "images" / "cell_white.png"),
    CODE_UNCOVERED:          QtGui.QImage(),
    CODE_COVERED_FLAG:       QtGui.QImage(BASE_PATH / "images" / "cell_flag_white.png"),
    CODE_UNCOVERED_MINE:     QtGui.QImage(BASE_PATH / "images" / "pig.png"),
    CODE_UNCOVERED_MINE_OK:  QtGui.QImage(BASE_PATH / "images" / "pig_ok.png"),
    CODE_UNCOVERED_MINE_BAD: QtGui.QImage(BASE_PATH / "images" / "pig_bad.png"),
})

GAME_NONE = 0
GAME_VICTORY = 1
GAME_DEFEAT = 2

# idk why, but pixmap crushes program execution (Process finished with exit code -1073741819 (0xC0000005))
# TEST_PIXMAP = QtGui.QPixmap()
# TEST_PIXMAP.load("BigFruit.png")
# TEST_PIXMAP.fromImage(PICT_DICT[CODE_COVERED])


class ItemDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent, table_widget):
        QtWidgets.QStyledItemDelegate.__init__(self, parent)
        self.table_widget = table_widget
        self.installEventFilter(self)

    def createEditor(self, parent, option, index):
        return None

    def paint(self, painter, option, index):
        painter.save()
        # if not self.failed:
        text = self.table_widget.item(index.row(), index.column()).text()
        painter.drawImage(option.rect, PICT_DICT[text[0]])
        # painter.drawPixmap(option.rect, TEST_PIXMAP)
        # else:
        #     painter.drawImage(self.table_widget.rect(), PICT_DICT[CODE_UNCOVERED_MINE])
        painter.restore()


class CustomLabel(QtWidgets.QLabel):

    signal_cell_left_btn = QtCore.Signal(int, int)
    signal_cell_right_btn = QtCore.Signal(int, int)

    def __init__(self, item, text=None):
        QtWidgets.QLabel.__init__(self, text)
        self.setAlignment(QtGui.Qt.AlignmentFlag.AlignCenter)
        self.setSizePolicy(QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding
        ))

        self.item = item
        if text:
            self.setText(text)
        self.mined = False
        self.installEventFilter(self)

    def row(self):
        return self.item.row()

    def column(self):
        return self.item.column()

    def eventFilter(self, watched, event):
        # if event.type() == QtCore.QEvent.Type.MouseButtonPress:
        #     print(event.position().toPoint())

        if event.type() == QtCore.QEvent.Type.MouseButtonRelease:
            # print(event.position().toPoint())

            if watched.rect().contains(event.position().toPoint()):
                event_button = event.button()
                if event_button == QtCore.Qt.MouseButton.LeftButton:
                    self.signal_cell_left_btn.emit(watched.row(), watched.column())
                elif event_button == QtCore.Qt.MouseButton.RightButton:
                    self.signal_cell_right_btn.emit(watched.row(), watched.column())

        return False

    def __repr__(self):
        return f"CustomLabel: row={self.row()}, column={self.column()}, mined={self.mined}, text={self.text()}"


class MinesweeperSettings(QtWidgets.QWidget):
    """Minesweeper settings window."""

    def __init__(self):
        pass


class MinesweeperWindow(QtWidgets.QMainWindow, Ui_MinesweeperWindow):
    """Minesweeper main window."""

    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        QtWidgets.QMainWindow.__init__(self, parent, flags)
        self.setupUi(self)
        self.setWindowTitle("Minesweeper")
        self.setWindowIcon(QtGui.QIcon(str(BASE_PATH / "images" / "pig.png")))

        # Settings
        self.settings_rows = 10  # default number of rows
        self.settings_cols = 10  # default number of columns
        self.settings_mines = 12  # default number of mines

        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.item_delegate = ItemDelegate(self.tableWidget.itemDelegate(), self.tableWidget)
        self.tableWidget.setItemDelegate(self.item_delegate)

        self.tableWidget.installEventFilter(self)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self._timer_job)

        self.action_startNewGame.triggered.connect(self.start_new_game)

        # Inits
        self._num_rows = 0
        self._num_cols = 0
        self._num_mines = 0
        self._mines_preset = None
        self._game_state = GAME_NONE
        self._uncovered_cells = 0
        self._flagged_cells = 0

        self._set_field()

    def _timer_job(self):
        time_obj = self.timeEdit_timer.time().addMSecs(self.timer.interval())
        self.timeEdit_timer.setTime(time_obj)

    def start_new_game(self):
        # ask only after game started
        if not self._uncovered_cells or QtWidgets.QMessageBox.question(
            self, "Confirm", "Are you sure you want to start a new game?",
            QtWidgets.QMessageBox.StandardButton.Yes, QtWidgets.QMessageBox.StandardButton.No
        ) == QtWidgets.QMessageBox.StandardButton.Yes:
            self._set_field()

    def _emit_uncovered_cells(self):
        self.lineEdit_cellsUncovered.setText(f"{self._uncovered_cells}/"
                                             f"{self._num_rows * self._num_cols - self._num_mines}")

    def _emit_flagged_cells(self):
        flagged_bombs = min(self._num_mines, self._flagged_cells)
        self.lineEdit_minesFlagged.setText(f"{flagged_bombs}/{self._num_mines}")

    def _set_field(self):
        """Set specified field size."""
        rows, cols, mines = self.settings_rows, self.settings_cols, self.settings_mines
        self._num_rows = rows
        self._num_cols = cols
        self._num_mines = mines
        self._game_state = GAME_NONE
        self._uncovered_cells = 0
        self._flagged_cells = 0
        self.timer.stop()
        self.timeEdit_timer.setTime(QtCore.QTime(0, 0, 0, 0))
        self._emit_uncovered_cells()
        self._emit_flagged_cells()

        table_widget = self.tableWidget
        table_widget.setRowCount(rows)
        table_widget.setColumnCount(cols)

        mines_preset = np.full(rows * cols, False)
        rand_choices = np.random.randint(rows * cols, size=mines)
        for choice in rand_choices:
            mines_preset[choice] = True
        mines_preset = mines_preset.reshape(rows, cols)
        self._mines_preset = mines_preset

        for i in range(rows):
            for j in range(cols):
                item = QtWidgets.QTableWidgetItem()
                item.setText(CODE_COVERED)
                table_widget.setItem(i, j, item)

                label = CustomLabel(item)
                label.signal_cell_left_btn.connect(self.cell_uncover)
                label.signal_cell_right_btn.connect(self.cell_toggle_flag)
                label.mined = mines_preset[i][j]
                table_widget.setCellWidget(i, j, label)

    def _recurse_uncover(self, row, col):
        table_widget = self.tableWidget
        this_label = table_widget.cellWidget(row, col)
        this_item = this_label.item
        if this_item.text() != CODE_COVERED:  # only covered cell can become uncovered
            return

        # call function for 3x3 area
        start_row = max(0, row - 1)
        end_row = min(self._num_rows - 1, row + 1)
        start_col = max(0, col - 1)
        end_col = min(self._num_cols - 1, col + 1)
        # print(f"rows: ({start_row}, {end_row})")
        # print(f"cols: ({start_col}, {end_col})")

        mines_in_area = 0
        coordinates = []
        for i in range(start_row, end_row + 1, 1):
            for j in range(start_col, end_col + 1, 1):
                if (i, j) != (row, col):
                    label = table_widget.cellWidget(i, j)
                    coordinates.append((label.row(), label.column()))
                    if label.mined:
                        mines_in_area += 1

        this_item.setText(CODE_UNCOVERED)
        self._uncovered_cells += 1
        self._emit_uncovered_cells()
        if mines_in_area:
            this_label.setText(str(mines_in_area))
        else:
            for i, j in coordinates:
                self._recurse_uncover(i, j)

    def cell_uncover(self, row, col):
        if self._game_state != GAME_NONE:
            return

        if not self._uncovered_cells:  # start timer only after first uncover
            self.timer.start(1000)

        item = self.tableWidget.item(row, col)
        label = self.tableWidget.cellWidget(row, col)
        item_text = item.text()
        if item_text in {CODE_UNCOVERED, CODE_COVERED_FLAG}:  # ignore if already uncovered or flag is set
            return
        if label.mined:
            item.setText(CODE_UNCOVERED_MINE)
            self._end_game(defeat=True)
        else:
            self._recurse_uncover(row, col)
            if self._num_rows * self._num_cols - self._uncovered_cells == self._num_mines:
                self._end_game(defeat=False)

    def cell_toggle_flag(self, row, col):
        if self._game_state != GAME_NONE:
            return

        item = self.tableWidget.item(row, col)
        item_text = item.text()
        if item_text == CODE_COVERED:
            item.setText(CODE_COVERED_FLAG)
            self._flagged_cells += 1
        elif item_text == CODE_COVERED_FLAG:
            item.setText(CODE_COVERED)
            self._flagged_cells -= 1
        else:
            return

        self._emit_flagged_cells()

    def _end_game(self, defeat):
        self.timer.stop()
        title = "Info"
        if defeat:
            self._game_state = GAME_DEFEAT
            text = "DEFEAT!"
            QtWidgets.QMessageBox.warning(self, title, text, QtWidgets.QMessageBox.StandardButton.Ok)
        else:
            self._game_state = GAME_VICTORY
            text = "VICTORY!"
            QtWidgets.QMessageBox.information(self, title, text, QtWidgets.QMessageBox.StandardButton.Ok)

    def closeEvent(self, event):
        if QtWidgets.QMessageBox.question(
                self, "Confirm", "Are you sure you want to exit the program?",
                QtWidgets.QMessageBox.StandardButton.Yes, QtWidgets.QMessageBox.StandardButton.No
        ) == QtWidgets.QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


def main(sys_argv):
    app = QtWidgets.QApplication(sys_argv)
    # app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    window = MinesweeperWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
