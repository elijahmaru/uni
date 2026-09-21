import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenuBar,
    QTextEdit,
    QFileDialog,
    QMessageBox,
    QAction,
    QToolBar,
    QLabel,
    QFontDialog,
    QColorDialog,
)
from PyQt5.QtGui import QFont


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.currentFile: str | None = None
        self.setWindowTitle("Текстовый редактор")
        self.setGeometry(200, 100, 900, 600)
        self.editor: QTextEdit = QTextEdit()
        self.editor.setFont(QFont("Geist Mono", 12))
        self.setCentralWidget(self.editor)
        self.editor.document().modificationChanged.connect(self.updateTitle)
        self.createMenu()
        self.createToolbar()
        self.createStatusbar()
        self.updateTitle()

    def updateTitle(self):
        filename = self.currentFile or "Без имени"
        if self.editor.document().isModified():
            filename += "*"
        self.setWindowTitle(f"{filename} — Текстовый редактор")

    def createMenu(self):
        menuBar:QMenuBar = self.menuBar()
        fileMenu = menuBar.addMenu("Файл")
        newAction = QAction("Создать", self)
        newAction.setShortcut("Ctrl+N")
        newAction.triggered.connect(self.newFile)
        fileMenu.addAction(newAction)
        openAction = QAction("Открыть", self)
        openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)
        saveAction = QAction("Сохранить", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.triggered.connect(self.saveFile)
        fileMenu.addAction(saveAction)
        saveAsAction = QAction("Сохранить как...", self)
        saveAsAction.triggered.connect(self.saveFileAs)
        fileMenu.addAction(saveAsAction)
        fileMenu.addSeparator()
        exitAction = QAction("Выход", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)
        editMenu = menuBar.addMenu("Правка")
        undoAction = QAction("Отменить", self)
        undoAction.setShortcut("Ctrl+Z")
        undoAction.triggered.connect(self.editor.undo)
        editMenu.addAction(undoAction)
        redoAction = QAction("Повторить", self)
        redoAction.setShortcut("Ctrl+Y")
        redoAction.triggered.connect(self.editor.redo)
        editMenu.addAction(redoAction)
        editMenu.addSeparator()
        cutAction = QAction("Вырезать", self)
        cutAction.setShortcut("Ctrl+X")
        cutAction.triggered.connect(self.editor.cut)
        editMenu.addAction(cutAction)
        copyAction = QAction("Копировать", self)
        copyAction.setShortcut("Ctrl+C")
        copyAction.triggered.connect(self.editor.copy)
        editMenu.addAction(copyAction)
        pasteAction = QAction("Вставить", self)
        pasteAction.setShortcut("Ctrl+V")
        pasteAction.triggered.connect(self.editor.paste)
        editMenu.addAction(pasteAction)
        selectAllAction = QAction("Выделить всё", self)
        selectAllAction.setShortcut("Ctrl+A")
        selectAllAction.triggered.connect(self.editor.selectAll)
        editMenu.addAction(selectAllAction)

        formatMenu = menuBar.addMenu("Формат")
        fontAction = QAction("Шрифт", self)
        fontAction.triggered.connect(self.chooseFont)
        formatMenu.addAction(fontAction)
        colorAction = QAction("Цвет текста", self)
        colorAction.triggered.connect(self.chooseColor)
        formatMenu.addAction(colorAction)
        helpMenu = menuBar.addMenu("Справка")
        aboutAction = QAction("О программе", self)
        aboutAction.triggered.connect(self.showAbout)
        helpMenu.addAction(aboutAction)

    def createToolbar(self):
        toolbar = QToolBar("Панель инструментов")
        self.addToolBar(toolbar)
        actions = [
            ("Новый", self.newFile),
            ("Открыть", self.openFile),
            ("Сохранить", self.saveFile),
            ("Отменить", self.editor.undo),
            ("Повторить", self.editor.redo),
            ("Копировать", self.editor.copy),
            ("Вставить", self.editor.paste),
        ]

        for name, function in actions:
            action = QAction(name, self)
            action.triggered.connect(function)
            toolbar.addAction(action)

    def createStatusbar(self):
        self.statusLabel = QLabel("Готово")
        self.statusBar().addWidget(self.statusLabel)
        self.editor.cursorPositionChanged.connect(self.updateCursorPosition)

    def updateCursorPosition(self):
        cursor = self.editor.textCursor()
        line = cursor.blockNumber() + 1
        column = cursor.columnNumber() + 1
        self.statusLabel.setText(f"Строка: {line} | Столбец: {column}")

    def newFile(self):
        if not self.confirmSave():
            return
        self.editor.clear()
        self.currentFile = None
        self.editor.document().setModified(False)
        self.updateTitle()

    def openFile(self):
        if not self.confirmSave():
            return
        filename, _ = QFileDialog.getOpenFileName(
            self, "Открыть файл", "", "Текстовые файлы (*.txt);;Все файлы (*)"
        )
        if not filename:
            return
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.editor.setPlainText(file.read())
            self.currentFile = filename
            self.editor.document().setModified(False)
            self.updateTitle()
        except Exception as error:
            QMessageBox.critical(self, "Ошибка", f"Не удалось открыть файл:\n{error}")

    def saveFile(self):
        if not self.currentFile:
            return self.saveFileAs()
        return self.writeFile(self.currentFile)

    def saveFileAs(self):
        filename, _ = QFileDialog.getSaveFileName(
            self, "Сохранить файл", "", "Текстовые файлы (*.txt);;Все файлы (*)"
        )
        if not filename:
            return False
        if not filename.lower().endswith(".txt"):
            filename += ".txt"
        if self.writeFile(filename):
            self.currentFile = filename
            self.updateTitle()
            return True
        return False

    def writeFile(self, filename: str):
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(self.editor.toPlainText())
            self.editor.document().setModified(False)
            self.statusLabel.setText("Файл сохранён")
            self.updateTitle()
            return True
        except Exception as error:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл:\n{error}")
            return False

    def confirmSave(self):
        if not self.editor.document().isModified():
            return True
        answer = QMessageBox.question(
            self,
            "Сохранение",
            "Документ был изменён. Сохранить изменения?",
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
        )
        if answer == QMessageBox.Yes:
            return self.saveFile()
        if answer == QMessageBox.Cancel:
            return False
        return True

    def closeEvent(self, event):
        if self.confirmSave():
            event.accept()
        else:
            event.ignore()

    def chooseFont(self):
        font, ok = QFontDialog.getFont(self.editor.currentFont(), self, "Выбор шрифта")
        if ok:
            self.editor.setCurrentFont(font)

    def chooseColor(self):
        color = QColorDialog.getColor(self.editor.textColor(), self, "Выбор цвета")
        if color.isValid():
            self.editor.setTextColor(color)

    def showAbout(self):
        QMessageBox.about(
            self,
            "О программе",
            "Текстовый редактор\n\n"
            "Разработан на Python с использованием PyQt5.\n"
            "Лабораторная работа №1.",
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec_())
