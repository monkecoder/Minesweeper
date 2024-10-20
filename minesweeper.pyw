"""Minesweeper game based on PySide6."""

from configparser import ConfigParser
from pathlib import Path
from types import MappingProxyType

import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets, QtTest

from gui.minesweeper_settings_ui import Ui_MinesweeperSettings
from gui.minesweeper_window_ui import Ui_MinesweeperWindow
from gui.minesweeper_about_ui import Ui_MinesweeperAbout

BASE_PATH = Path(__file__).parent

CELL_COVERED = "c"              # cell is covered, default
CELL_COVERED_FLAG = "f"         # cell is covered, flag
CELL_UNCOVERED = "u"            # cell is uncovered, default
CELL_UNCOVERED_MINE = "m"       # cell is uncovered, mine
CELL_UNCOVERED_MINE_OK = "o"    # cell is uncovered, mine defused
CELL_UNCOVERED_MINE_BAD = "b"   # cell is uncovered, mine exploded

PICT_DICT = MappingProxyType({
    CELL_COVERED:            QtGui.QImage(BASE_PATH / "images" / "cell_white.png"),
    CELL_UNCOVERED:          QtGui.QImage(),
    CELL_COVERED_FLAG:       QtGui.QImage(BASE_PATH / "images" / "cell_flag_white.png"),
    CELL_UNCOVERED_MINE:     QtGui.QImage(BASE_PATH / "images" / "pig.png"),
    CELL_UNCOVERED_MINE_OK:  QtGui.QImage(BASE_PATH / "images" / "pig_ok.png"),
    CELL_UNCOVERED_MINE_BAD: QtGui.QImage(BASE_PATH / "images" / "pig_bad.png"),
})

GAME_BLOCK = 0
GAME_RUNNING = 1
GAME_VICTORY = 2
GAME_DEFEAT = 3

# idk why, but pixmap crushes program execution (Process finished with exit code -1073741819 (0xC0000005))
# TEST_PIXMAP = QtGui.QPixmap()
# TEST_PIXMAP.load("BigFruit.png")
# TEST_PIXMAP.fromImage(PICT_DICT[CELL_COVERED])

DEFAULT_CONFIG_PATH = BASE_PATH / "minesweeper.ini"
DEFAULT_ROW_COUNT = 10
DEFAULT_COL_COUNT = 10
DEFAULT_MINE_COUNT = 12
DEFAULT_ANIMATION_PERIOD = 75

MIN_ROWS = 4
MAX_ROWS = 30
MIN_COLS = 4
MAX_COLS = 30
MIN_ANIMATION_PERIOD = 0
MAX_ANIMATION_PERIOD = 250


class MinesweeperConfig:
    """Class for saving/loading minesweeper settings configuration."""

    def __init__(self):
        """Constructor."""
        self._config = ConfigParser()
        self._last_path = None

    @property
    def config(self):
        """Get dict representation of current config."""
        return {section: dict(self._config.items(section)) for section in self._config.sections()}

    @property
    def last_path(self):
        """Get last path of the config file."""
        return self._last_path

    def _create_section_if_not_exist(self, section):
        if not self._config.has_section(section):
            self._config.add_section(section)

    def _remove_section_if_empty(self, section):
        if self._config.has_section(section) and not self._config.options(section):
            self._config.remove_section(section)

    def _fix_mines_value(self):
        max_mines = self.rows * self.cols - 1
        if self.mines > max_mines:
            self.mines = max_mines

    def load_config(self, path=None):
        """Load config from .ini file."""
        if not path:
            path = self._last_path if self._last_path else DEFAULT_CONFIG_PATH

        self._config.read(path)
        rows, cols, mines, animation_period = self.rows, self.cols, self.mines, self.animation_period
        if not (MIN_ROWS <= rows <= MAX_ROWS):
            msg = f"Error in config file: rows must be between {MIN_ROWS} and {MAX_ROWS}"
            raise ValueError(msg)
        if not (MIN_ROWS <= cols <= MAX_ROWS):
            msg = f"Error in config file: cols must be between {MIN_COLS} and {MAX_COLS}"
            raise ValueError(msg)
        if not (MIN_ANIMATION_PERIOD <= animation_period <= MAX_ANIMATION_PERIOD):
            msg = (f"Error in config file: animation period must be between "
                   f"{MIN_ANIMATION_PERIOD} and {MAX_ANIMATION_PERIOD}")
            raise ValueError(msg)
        min_mines = 1
        max_mines = rows * cols - 1
        if not (min_mines <= mines <= max_mines):
            msg = f"Error in config file: mines must be between {min_mines} and {max_mines}"
            raise ValueError(msg)
        self._last_path = path

    def save_config(self, path=None):
        """Save config into .ini file."""
        if not path:
            path = self._last_path if self._last_path else DEFAULT_CONFIG_PATH

        with open(path, "w") as cfg_file:
            self._config.write(cfg_file)
        self._last_path = path

    @property
    def rows(self):
        """Get rows setting."""
        return self._config.getint("ALL", "rows", fallback=DEFAULT_ROW_COUNT)

    @rows.setter
    def rows(self, value: int):
        """Set rows setting."""
        if not (MIN_ROWS <= value <= MAX_ROWS):
            msg = f"Error while setting value: rows must be between {MIN_ROWS} and {MAX_ROWS}"
            raise ValueError(msg)
        self._create_section_if_not_exist("ALL")
        self._config.set("ALL", "rows", str(value))
        self._fix_mines_value()

    @rows.deleter
    def rows(self):
        """Restore rows setting to default."""
        self._config.remove_option("ALL", "rows")
        self._fix_mines_value()
        self._remove_section_if_empty("ALL")

    @property
    def cols(self):
        """Get cols setting."""
        return self._config.getint("ALL", "cols", fallback=DEFAULT_COL_COUNT)

    @cols.setter
    def cols(self, value: int):
        """Set cols setting."""
        if not (MIN_ROWS <= value <= MAX_ROWS):
            msg = f"Error while setting value: cols must be between {MIN_COLS} and {MAX_COLS}"
            raise ValueError(msg)
        self._create_section_if_not_exist("ALL")
        self._config.set("ALL", "cols", str(value))
        self._fix_mines_value()

    @cols.deleter
    def cols(self):
        """Restore cols setting to default."""
        self._config.remove_option("ALL", "cols")
        self._fix_mines_value()
        self._remove_section_if_empty("ALL")

    @property
    def mines(self):
        """Get mines setting."""
        return self._config.getint("ALL", "mines", fallback=DEFAULT_MINE_COUNT)

    @mines.setter
    def mines(self, value: int):
        """Set mines setting."""
        min_mines = 1
        max_mines = self.rows * self.cols - 1
        if not (min_mines <= value <= max_mines):
            msg = f"Error while setting value: mines must be between {min_mines} and {max_mines}"
            raise ValueError(msg)
        self._create_section_if_not_exist("ALL")
        self._config.set("ALL", "mines", str(value))

    @mines.deleter
    def mines(self):
        """Restore mines setting to default."""
        self._config.remove_option("ALL", "mines")
        self._remove_section_if_empty("ALL")

    @property
    def animation_period(self):
        """Get animation_period setting."""
        return self._config.getint("ALL", "animation_period", fallback=DEFAULT_ANIMATION_PERIOD)

    @animation_period.setter
    def animation_period(self, value: int):
        """Set animation_period setting."""
        if not (MIN_ANIMATION_PERIOD <= value <= MAX_ANIMATION_PERIOD):
            msg = (f"Error while setting value: animation period must be between "
                   f"{MIN_ANIMATION_PERIOD} and {MAX_ANIMATION_PERIOD}")
            raise ValueError(msg)
        self._create_section_if_not_exist("ALL")
        self._config.set("ALL", "animation_period", str(value))

    @animation_period.deleter
    def animation_period(self):
        """Restore animation_period setting to default."""
        self._config.remove_option("ALL", "animation_period")
        self._remove_section_if_empty("ALL")


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
    """Custom label for watching cell clicks, storing mines number and for other purposes."""

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
            if event_button == QtCore.Qt.MouseButton.RightButton:
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
        self.spinBox_rows.setMinimum(MIN_ROWS)
        self.spinBox_rows.setMaximum(MAX_ROWS)
        self.spinBox_cols.setMinimum(MIN_COLS)
        self.spinBox_cols.setMaximum(MAX_COLS)
        self.spinBox_mines.setMinimum(1)
        self.spinBox_animationPeriod.setMinimum(MIN_ANIMATION_PERIOD)
        self.spinBox_animationPeriod.setMaximum(MAX_ANIMATION_PERIOD)

        self.spinBox_rows.valueChanged.connect(self.check_max_mines)
        self.spinBox_cols.valueChanged.connect(self.check_max_mines)

    def check_max_mines(self):
        """Update spinBox_mines maximum value to fit the field size."""
        # at least 1 free cell for chance to win
        mines_max = self.spinBox_rows.value() * self.spinBox_cols.value() - 1
        self.spinBox_mines.setMaximum(mines_max)


class MinesweeperAbout(QtWidgets.QDialog, Ui_MinesweeperAbout):
    def __init__(self, parent):
        """Initialize minesweeper settings dialog."""
        QtWidgets.QDialog.__init__(self, parent, QtCore.Qt.WindowType.Dialog)
        self.setupUi(self)


class MinesweeperWindow(QtWidgets.QMainWindow, Ui_MinesweeperWindow):
    """Minesweeper main window."""

    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        """Initialize minesweeper main window."""
        QtWidgets.QMainWindow.__init__(self, parent, flags)
        self.settings_dialog = MinesweeperSettings(self)
        self.settings_dialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.settings_dialog.buttonBox.accepted.connect(self._update_settings)
        self.about_dialog = MinesweeperAbout(self)
        self.about_dialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        self.setupUi(self)
        self.setWindowTitle("Minesweeper")
        self.setWindowIcon(QtGui.QIcon(str(BASE_PATH / "images" / "pig.png")))

        # Settings
        self._config = MinesweeperConfig()
        self._config.load_config()
        self.settings_rows = self._config.rows  # default number of rows
        self.settings_cols = self._config.cols  # default number of columns
        self.settings_mines = self._config.mines  # default number of mines
        self.settings_animation_period = self._config.animation_period  # animation period

        # Init widgets
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.tableWidget.cellClicked.connect(self.cell_uncover)
        self.tableWidget.keyPressEvent = self.tableKeyPressEvent

        self.item_delegate = ItemDelegate(self.tableWidget.itemDelegate(), self.tableWidget)
        self.tableWidget.setItemDelegate(self.item_delegate)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self._timer_job)

        self.action_restartGame.triggered.connect(self.restart_game)
        self.action_settings.triggered.connect(self.show_settings_dialog)
        self.action_aboutProgram.triggered.connect(self.about_dialog.show)

        for widget in (self.lcdNumber_cellsUncovered, self.label_1, self.lcdNumber_cellsNotMined):
            widget.setToolTip("Uncovered cells / Not mined cells")
        for widget in (self.lcdNumber_cellsFlagged, self.label_2, self.lcdNumber_cellsMined):
            widget.setToolTip("Flagged cells / Mined cells")
        self.timeEdit_timer.setToolTip("Time elapsed since start (min:sec)")

        self.timeEdit_timer.lineEdit().installEventFilter(self)

        # Init shortcuts
        self.action_restartGame.setShortcut(QtGui.QKeySequence("Alt+R"))
        self.action_settings.setShortcut(QtGui.QKeySequence("Alt+S"))
        self.action_aboutProgram.setShortcut(QtGui.QKeySequence("Alt+H"))

        # Init minesweeper logic
        self._num_rows = 0
        self._num_cols = 0
        self._num_mines = 0
        self._mines_preset = None
        self._game_state = GAME_BLOCK
        self._uncovered_cells = 0
        self._flagged_cells = 0

        self._set_field()

    def _timer_job(self):
        """Update data for timeEdit_timer widget (executed by timer)."""
        time_obj = self.timeEdit_timer.time().addMSecs(self.timer.interval())
        self.timeEdit_timer.setTime(time_obj)

    def restart_game(self):
        """Start a new game."""
        if self._game_state == GAME_BLOCK:
            return
        # ask only after game started
        if not self._uncovered_cells or self._game_state != GAME_RUNNING or QtWidgets.QMessageBox.question(
            self, "Confirm", "Are you sure you want to restart the game?",
            QtWidgets.QMessageBox.StandardButton.Yes, QtWidgets.QMessageBox.StandardButton.No
        ) == QtWidgets.QMessageBox.StandardButton.Yes:
            self._set_field()

    def show_settings_dialog(self):
        """Show settings dialog."""
        self.settings_dialog.spinBox_rows.setValue(self.settings_rows)
        self.settings_dialog.spinBox_cols.setValue(self.settings_cols)
        self.settings_dialog.spinBox_mines.setValue(self.settings_mines)
        self.settings_dialog.spinBox_animationPeriod.setValue(self.settings_animation_period)
        self.settings_dialog.show()

    def _update_settings(self):
        """Update settings if settings dialog was accepted."""
        self.settings_rows = self.settings_dialog.spinBox_rows.value()
        self.settings_cols = self.settings_dialog.spinBox_cols.value()
        self.settings_mines = self.settings_dialog.spinBox_mines.value()
        self.settings_animation_period = self.settings_dialog.spinBox_animationPeriod.value()
        self._config.rows = self.settings_rows
        self._config.cols = self.settings_cols
        self._config.mines = self.settings_mines
        self._config.animation_period = self.settings_animation_period
        if not self._uncovered_cells or self._game_state != GAME_RUNNING:
            self._set_field()

    def _animation_sleep(self):
        QtTest.QTest.qWait(self.settings_animation_period)  # QTimer should be used, but this is much easier

    def _emit_uncovered_cells(self):
        """Update data for lineEdit_cellsUncovered widget."""
        self.lcdNumber_cellsUncovered.display(self._uncovered_cells)

    def _emit_flagged_cells(self):
        """Update data for lineEdit_cellsFlagged widget."""
        self.lcdNumber_cellsFlagged.display(self._flagged_cells)

    def _set_field(self):
        """Init field with size specified in settings (start a new game)."""
        rows, cols, mines = self.settings_rows, self.settings_cols, self.settings_mines
        self._num_rows = rows
        self._num_cols = cols
        self._num_mines = mines
        self._game_state = GAME_RUNNING
        self._uncovered_cells = 0
        self._flagged_cells = 0
        self.timer.stop()
        self.timeEdit_timer.setTime(QtCore.QTime(0, 0, 0, 0))
        self.lcdNumber_cellsNotMined.display(self._num_rows * self._num_cols - self._num_mines)
        self.lcdNumber_cellsMined.display(self._num_mines)
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
                item.setText(CELL_COVERED)
                table_widget.setItem(i, j, item)

                label = CustomLabel(item)
                label.signal_cell_right_btn.connect(self.cell_toggle_flag)
                label.mined = mines_preset[i][j]
                table_widget.setCellWidget(i, j, label)

    def _recurse_uncover(self, row, col):
        """Recursive uncover for cells in 3x3 area, stop if there are mines around."""
        table_widget = self.tableWidget
        this_label = table_widget.cellWidget(row, col)
        this_item = this_label.item
        if this_item.text() != CELL_COVERED:  # only covered cell can become uncovered
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

        this_item.setText(CELL_UNCOVERED)
        self._uncovered_cells += 1
        self._emit_uncovered_cells()
        if mines_in_area:
            this_label.setText(str(mines_in_area))
        else:
            for i, j in coordinates:
                self._recurse_uncover(i, j)

    def cell_uncover(self, row, col):
        """Uncover covered cell."""
        if self._game_state != GAME_RUNNING:
            return

        if not self._uncovered_cells:  # start timer only after first uncover
            self.timer.start(1000)

        item = self.tableWidget.item(row, col)
        label = self.tableWidget.cellWidget(row, col)
        item_text = item.text()
        if item_text != CELL_COVERED:  # ignore if not default covered cell
            return
        if label.mined:
            self._end_game(row, col, defeat=True)
        else:
            self._recurse_uncover(row, col)
            if self._num_rows * self._num_cols - self._uncovered_cells == self._num_mines:
                self._end_game(defeat=False)

    def cell_toggle_flag(self, row, col):
        """Toggle flag on covered cell."""
        if self._game_state != GAME_RUNNING:
            return

        item = self.tableWidget.item(row, col)
        item_text = item.text()
        if item_text == CELL_COVERED:
            item.setText(CELL_COVERED_FLAG)
            self._flagged_cells += 1
        elif item_text == CELL_COVERED_FLAG:
            item.setText(CELL_COVERED)
            self._flagged_cells -= 1
        else:
            return

        self._emit_flagged_cells()

    def _end_game(self, row=-1, col=-1, *, defeat):
        """Game end."""
        self._game_state = GAME_BLOCK
        self.timer.stop()
        title = "Info"
        if defeat:
            self._show_mines_explode(row, col)
            text = "DEFEAT!"
            QtWidgets.QMessageBox.warning(self, title, text, QtWidgets.QMessageBox.StandardButton.Ok)
            self._game_state = GAME_DEFEAT
        else:
            self._show_mines_defused()
            text = "VICTORY!"
            QtWidgets.QMessageBox.information(self, title, text, QtWidgets.QMessageBox.StandardButton.Ok)
            self._game_state = GAME_VICTORY

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

        if item := get_item(row, col):
            item.setText(CELL_UNCOVERED_MINE)
            self._animation_sleep()
            item.setText(CELL_UNCOVERED_MINE_BAD)
        if self._num_mines == mines_exploded:  # return if it was the only one
            return
        self._animation_sleep()

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
                    item.setText(CELL_UNCOVERED_MINE)
                self._animation_sleep()
                for item in square_items:
                    item.setText(CELL_UNCOVERED_MINE_BAD)

            if mines_exploded == self._num_mines:
                break
            if square_items:
                square_items.clear()
                self._animation_sleep()
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
                    label.item.setText(CELL_UNCOVERED_MINE_OK)
                    mines_defused += 1
            if mines_defused == self._num_mines or i == rows - 1:
                break
            if is_row_mined:
                self._animation_sleep()

    def tableKeyPressEvent(self, event):
        """Reimplementation of keyPressEvent for tableWidget, handles key pressing."""
        if event.key() in {QtCore.Qt.Key.Key_Space, QtCore.Qt.Key.Key_Return, QtCore.Qt.Key.Key_Enter}:
            item = self.tableWidget.currentItem()
            self.tableWidget.cellClicked.emit(item.row(), item.column())
        elif event.key() == QtCore.Qt.Key.Key_Backspace:
            table_widget = self.tableWidget
            row, col = table_widget.currentRow(), table_widget.currentColumn()
            label = table_widget.cellWidget(row, col)
            label.signal_cell_right_btn.emit(row, col)

        QtWidgets.QTableWidget.keyPressEvent(self.tableWidget, event)

    def eventFilter(self, watched, event):
        """Event filter for timeEdit_timer widget, ignore all mouse events."""
        if isinstance(event, QtGui.QMouseEvent):
            return True
        return False

    def closeEvent(self, event):
        """Catch close event and ask confirmation."""
        if QtWidgets.QMessageBox.question(
                self, "Confirm", "Are you sure you want to exit the program?",
                QtWidgets.QMessageBox.StandardButton.Yes, QtWidgets.QMessageBox.StandardButton.No
        ) == QtWidgets.QMessageBox.StandardButton.Yes:
            self._config.save_config()
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
