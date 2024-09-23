"""Minesweeper game based on PySide6."""

from pathlib import Path
from types import MappingProxyType

import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets, QtTest

from gui.minesweeper_settings_ui import Ui_MinesweeperSettings
from gui.minesweeper_window_ui import Ui_MinesweeperWindow

BASE_PATH = Path(__file__).parent

CODE_COVERED = "c"              # cell is covered, default
CODE_COVERED_FLAG = "f"         # cell is covered, flag
CODE_UNCOVERED = "u"            # cell is uncovered, default
CODE_UNCOVERED_MINE = "m"       # cell is uncovered, mine
CODE_UNCOVERED_MINE_OK = "o"    # cell is uncovered, mine defused
CODE_UNCOVERED_MINE_BAD = "b"   # cell is uncovered, mine exploded

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
    """Item delegate for drawing images in fields."""

    def __init__(self, parent, table_widget):
        """Initialize."""
        QtWidgets.QStyledItemDelegate.__init__(self, parent)
        self.table_widget = table_widget

    def createEditor(self, parent, option, index):
        """Prevent item text editing."""
        return None

    def paint(self, painter, option, index):
        """Paint picture based on code in item text."""
        painter.save()
        text = self.table_widget.item(index.row(), index.column()).text()
        painter.drawImage(option.rect, PICT_DICT[text])
        painter.restore()


class CustomLabel(QtWidgets.QLabel):
    """Custom label for watching button clicks, storing mines number and for other purposes."""

    signal_cell_left_btn = QtCore.Signal(int, int)
    signal_cell_right_btn = QtCore.Signal(int, int)

    def __init__(self, item, text=None):
        """Initialize."""
        QtWidgets.QLabel.__init__(self, text)
        self.setAlignment(QtGui.Qt.AlignmentFlag.AlignCenter)
        self.setSizePolicy(QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding
        ))

        self.item = item  # item in same cell of tableWidget
        if text:
            self.setText(text)
        self.mined = False
        self.installEventFilter(self)

    def row(self):
        """Get row of current cell in tableWidget."""
        return self.item.row()

    def column(self):
        """Get column of current cell in tableWidget."""
        return self.item.column()

    def eventFilter(self, watched, event):
        """Filter mouse button clicks (left for uncover, right for flag)."""
        if (event.type() == QtCore.QEvent.Type.MouseButtonRelease and
                watched.rect().contains(event.position().toPoint())):
            event_button = event.button()
            if event_button == QtCore.Qt.MouseButton.LeftButton:
                self.signal_cell_left_btn.emit(watched.row(), watched.column())
            elif event_button == QtCore.Qt.MouseButton.RightButton:
                self.signal_cell_right_btn.emit(watched.row(), watched.column())

        return False

    def __str__(self):
        """String object representation for convenience."""
        return f"CustomLabel: row={self.row()}, column={self.column()}, mined={self.mined}, text={self.text()}"


class MinesweeperSettings(QtWidgets.QDialog, Ui_MinesweeperSettings):
    """Minesweeper settings dialog."""

    def __init__(self, parent):
        """Initialize minesweeper settings dialog."""
        QtWidgets.QDialog.__init__(self, parent, QtCore.Qt.WindowType.Dialog)
        self.setupUi(self)
        self.spinBox_rows.setMinimum(4)
        self.spinBox_rows.setMaximum(50)
        self.spinBox_cols.setMinimum(4)
        self.spinBox_rows.setMaximum(50)
        self.spinBox_mines.setMinimum(1)

        self.spinBox_rows.valueChanged.connect(self.check_max_mines)
        self.spinBox_cols.valueChanged.connect(self.check_max_mines)

    def check_max_mines(self):
        """Update spinBox_mines maximum value to fit the field size."""
        # at least 1 free cell for chance to win
        mines_max = self.spinBox_rows.value() * self.spinBox_cols.value() - 1
        self.spinBox_mines.setMaximum(mines_max)


class MinesweeperWindow(QtWidgets.QMainWindow, Ui_MinesweeperWindow):
    """Minesweeper main window."""

    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        """Initialize minesweeper main window."""
        QtWidgets.QMainWindow.__init__(self, parent, flags)
        self.settings_dialog = MinesweeperSettings(self)
        self.settings_dialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.settings_dialog.buttonBox.accepted.connect(self._update_settings)

        self.setupUi(self)
        self.setWindowTitle("Minesweeper")
        self.setWindowIcon(QtGui.QIcon(str(BASE_PATH / "images" / "pig.png")))

        # Settings
        # ToDo: create settings storage (.ini file or smth)
        self.settings_rows = 10  # default number of rows
        self.settings_cols = 10  # default number of columns
        self.settings_mines = 12  # default number of mines

        # Init widgets
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.item_delegate = ItemDelegate(self.tableWidget.itemDelegate(), self.tableWidget)
        self.tableWidget.setItemDelegate(self.item_delegate)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self._timer_job)

        self.action_startNewGame.triggered.connect(self.start_new_game)
        self.action_settings.triggered.connect(self.show_settings_dialog)

        # Init minesweeper logic
        self._num_rows = 0
        self._num_cols = 0
        self._num_mines = 0
        self._mines_preset = None
        self._game_state = GAME_NONE
        self._uncovered_cells = 0
        self._flagged_cells = 0

        self._set_field()

    def _timer_job(self):
        """Update data for timeEdit_timer widget (executed by timer)."""
        time_obj = self.timeEdit_timer.time().addMSecs(self.timer.interval())
        self.timeEdit_timer.setTime(time_obj)

    def start_new_game(self):
        """Start a new game."""
        # ask only after game started
        if not self._uncovered_cells or self._game_state != GAME_NONE or QtWidgets.QMessageBox.question(
            self, "Confirm", "Are you sure you want to start a new game?",
            QtWidgets.QMessageBox.StandardButton.Yes, QtWidgets.QMessageBox.StandardButton.No
        ) == QtWidgets.QMessageBox.StandardButton.Yes:
            self._set_field()

    def show_settings_dialog(self):
        """Show settings dialog."""
        self.settings_dialog.spinBox_rows.setValue(self.settings_rows)
        self.settings_dialog.spinBox_cols.setValue(self.settings_cols)
        self.settings_dialog.spinBox_mines.setValue(self.settings_mines)
        self.settings_dialog.show()

    def _update_settings(self):
        """Update settings if settings dialog was accepted."""
        self.settings_rows = self.settings_dialog.spinBox_rows.value()
        self.settings_cols = self.settings_dialog.spinBox_cols.value()
        self.settings_mines = self.settings_dialog.spinBox_mines.value()

    def _emit_uncovered_cells(self):
        """Update data for lineEdit_cellsUncovered widget."""
        self.lineEdit_cellsUncovered.setText(f"{self._uncovered_cells}/"
                                             f"{self._num_rows * self._num_cols - self._num_mines}")

    def _emit_flagged_cells(self):
        """Update data for lineEdit_minesFlagged widget."""
        flagged_bombs = min(self._num_mines, self._flagged_cells)
        self.lineEdit_minesFlagged.setText(f"{flagged_bombs}/{self._num_mines}")

    def _set_field(self):
        """Init field with size specified in settings (start a new game)."""
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
        rand_choices = np.random.choice(range(rows * cols), size=mines, replace=False)
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
        """Recursive uncover for cells in 3x3 area, stop if there are bombs around."""
        table_widget = self.tableWidget
        this_label = table_widget.cellWidget(row, col)
        this_item = this_label.item
        if this_item.text() != CODE_COVERED:  # only covered cell can become uncovered
            return

        # Call function for 3x3 area
        start_row = max(0, row - 1)
        end_row = min(self._num_rows - 1, row + 1)
        start_col = max(0, col - 1)
        end_col = min(self._num_cols - 1, col + 1)

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
        """Uncover covered cell."""
        if self._game_state != GAME_NONE:
            return

        if not self._uncovered_cells:  # start timer only after first uncover
            self.timer.start(1000)

        item = self.tableWidget.item(row, col)
        label = self.tableWidget.cellWidget(row, col)
        item_text = item.text()
        if item_text != CODE_COVERED:  # ignore if not default covered cell
            return
        if label.mined:
            self._end_game(row, col, defeat=True)
        else:
            self._recurse_uncover(row, col)
            if self._num_rows * self._num_cols - self._uncovered_cells == self._num_mines:
                self._end_game(defeat=False)

    def cell_toggle_flag(self, row, col):
        """Toggle flag on covered cell."""
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

    def _end_game(self, row=-1, col=-1, *, defeat):
        """Game end."""
        self.timer.stop()
        title = "Info"
        if defeat:
            self._game_state = GAME_DEFEAT
            self._show_mines_explode(row, col)
            text = "DEFEAT!"
            QtWidgets.QMessageBox.warning(self, title, text, QtWidgets.QMessageBox.StandardButton.Ok)
        else:
            self._game_state = GAME_VICTORY
            self._show_mines_defused()
            text = "VICTORY!"
            QtWidgets.QMessageBox.information(self, title, text, QtWidgets.QMessageBox.StandardButton.Ok)

    def _show_mines_explode(self, row, col):
        """Shows all mines exploding."""
        # Serial explodes in increasing square
        table_widget = self.tableWidget

        rows, cols = table_widget.rowCount(), table_widget.columnCount()
        # Calc maximum distance from point to tabWidget border
        max_loops = max(row - 1, rows - row - 1, col - 1, cols - col - 1)

        mines_exploded = 0

        def get_item(_row, _col):
            label = table_widget.cellWidget(_row, _col)
            if label and label.mined:
                nonlocal mines_exploded
                mines_exploded += 1
                return label.item
            return None

        # Mine uncovered, wait to explode
        QtTest.QTest.qWait(100)  # QTimer should be used, but this is much easier
        if item := get_item(row, col):
            item.setText(CODE_UNCOVERED_MINE)
            QtTest.QTest.qWait(100)  # QTimer should be used, but this is much easier
            item.setText(CODE_UNCOVERED_MINE_BAD)
            QtTest.QTest.qWait(100)  # QTimer should be used, but this is much easier
        if self._num_mines == mines_exploded:  # return if it was the only one
            return
        QtTest.QTest.qWait(100)  # QTimer should be used, but this is much easier

        square_items = []
        bias = 1
        while bias <= max_loops:
            start_row, end_row = row - bias, row + bias
            start_col, end_col = col - bias, col + bias

            for i in range(start_row, end_row + 1, 1):
                if item := get_item(i, start_col):
                    square_items.append(item)
                if item := get_item(i, end_col):
                    square_items.append(item)

            for j in range(start_col + 1, end_col, 1):
                if item := get_item(start_row, j):
                    square_items.append(item)
                if item := get_item(end_row, j):
                    square_items.append(item)

            if square_items:
                for item in square_items:
                    item.setText(CODE_UNCOVERED_MINE)
                QtTest.QTest.qWait(100)  # QTimer should be used, but this is much easier
                for item in square_items:
                    item.setText(CODE_UNCOVERED_MINE_BAD)

            if mines_exploded == self._num_mines:
                break
            if square_items:
                square_items.clear()
                QtTest.QTest.qWait(100)  # QTimer should be used, but this is much easier
            bias += 1


    def _show_mines_defused(self):
        """Shows all mines being defused."""
        # Serial defuse from up to down
        table_widget = self.tableWidget
        rows, cols = table_widget.rowCount(), table_widget.columnCount()

        mines_defused = 0
        for i in range(rows):
            is_row_mined = False
            for j in range(cols):
                label = table_widget.cellWidget(i, j)
                if label.mined:
                    is_row_mined = True
                    label.item.setText(CODE_UNCOVERED_MINE_OK)
                    mines_defused += 1
            if mines_defused == self._num_mines or i == rows - 1:
                break
            if is_row_mined:
                QtTest.QTest.qWait(100)  # QTimer should be used, but this is much easier


    def closeEvent(self, event):
        """Catch close event and ask confirmation."""
        if QtWidgets.QMessageBox.question(
                self, "Confirm", "Are you sure you want to exit the program?",
                QtWidgets.QMessageBox.StandardButton.Yes, QtWidgets.QMessageBox.StandardButton.No
        ) == QtWidgets.QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


def main(sys_argv):
    """Start minesweeper application."""
    app = QtWidgets.QApplication(sys_argv)
    # app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    window = MinesweeperWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
