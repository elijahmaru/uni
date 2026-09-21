import sys
import math
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QTabWidget,
    QVBoxLayout,
    QFormLayout,
    QGroupBox,
    QMessageBox,
    QRadioButton,
    QTextEdit,
)
from PyQt5.QtGui import QFont


class CalcError(Exception):
    """Ошибка, которую показываем пользователю как есть."""


def parseNumber(text, kind=float):
    """Строка -> число (запятая допускается как десятичный разделитель)."""
    return kind(text.strip().replace(",", "."))


class BaseTaskWidget(QWidget):
    title = ""
    fields = []
    buttonText = "Вычислить"

    def __init__(self):
        super().__init__()
        self.edits = {}
        vbox = QVBoxLayout(self)

        if self.title:
            titleLabel = QLabel(self.title)
            titleLabel.setWordWrap(True)
            vbox.addWidget(titleLabel)

        if self.fields:
            form = QFormLayout()
            for name, label, default, kind in self.fields:
                edit = QLineEdit(default)
                form.addRow(label, edit)
                self.edits[name] = edit
            vbox.addLayout(form)

        self.setupExtra(vbox)

        btn = QPushButton(self.buttonText)
        btn.clicked.connect(self.run)
        vbox.addWidget(btn)

        self.out = self.makeOutput()
        vbox.addWidget(self.out)
        vbox.addStretch()

    def setupExtra(self, vbox):
        """Хук: добавить виджеты между полями ввода и кнопкой."""

    def makeOutput(self):
        lbl = QLabel("Результат: —")
        lbl.setFont(QFont("Consolas", 10))
        lbl.setWordWrap(True)
        return lbl

    def setOutput(self, text):
        self.out.setText(text)

    def calculate(self, values):
        """Возвращает строку результата или бросает исключение."""
        raise NotImplementedError

    def run(self):
        values = {}
        for name, label, _default, kind in self.fields:
            try:
                values[name] = parseNumber(self.edits[name].text(), kind)
            except ValueError:
                QMessageBox.critical(
                    self, "Ошибка", f"Некорректное значение поля «{label}»"
                )
                return
        try:
            self.setOutput(self.calculate(values))
        except CalcError as e:
            QMessageBox.critical(self, "Ошибка", str(e))
        except (ValueError, OverflowError, ZeroDivisionError) as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка вычисления: {e}")


class Task1Widget(BaseTaskWidget):
    title = (
        "Задача 1.\n"
        "f(x) = 3.5x³ + cos(x)/sin(2x) + eˣ,  x = 0.1\n"
        "Округлить f(x) к ближайшему целому и найти\n"
        "остаток от деления целой части на 5."
    )
    fields = [("x", "x =", "0.1", float)]

    def calculate(self, values):
        x = values["x"]
        try:
            f = 3.5 * x**3 + math.cos(x) / math.sin(2 * x) + math.exp(x)
        except ZeroDivisionError:
            raise CalcError("sin(2x) = 0 — деление на ноль!")
        whole = round(f)
        return (
            f"f(x) = {f:.6f}\n"
            f"Округлённое значение: {whole}\n"
            f"{whole} mod 5 = {whole % 5}"
        )


class Task2Widget(BaseTaskWidget):
    title = (
        "Задача 2.\nВвести три целых двузначных числа.\n"
        "Найти сумму первых цифр и вывести сообщение\n"
        "о чётности последних цифр данных чисел."
    )
    fields = [
        ("n1", "Число 1:", "12", int),
        ("n2", "Число 2:", "34", int),
        ("n3", "Число 3:", "57", int),
    ]

    def calculate(self, values):
        nums = []
        for i, key in enumerate(("n1", "n2", "n3"), start=1):
            n = values[key]
            if not 10 <= abs(n) <= 99:
                raise CalcError(f"Число {i} не является двузначным!")
            nums.append(n)

        first = [abs(n) // 10 for n in nums]
        lines = [
            "Сумма первых цифр: " + " + ".join(map(str, first)) + f" = {sum(first)}",
            "",
        ]
        for n in nums:
            last = abs(n) % 10
            par = "чётная" if last % 2 == 0 else "нечётная"
            lines.append(f"Число {n:4d}: последняя цифра {last} — {par}")
        return "\n".join(lines)


class Task3Widget(BaseTaskWidget):
    title = (
        "Задача 3.\nДля заданного года определить значение столетия.\n"
        "Примеры: 1900 → 19, 1901 → 20, −100 → −1, −101 → −2.\n"
        "Ошибка выдаётся только для года 0."
    )
    fields = [("year", "Год:", "1900", int)]

    @staticmethod
    def century(year):
        if year == 0:
            raise CalcError("Года 0 не существует!")
        sign = 1 if year > 0 else -1
        return sign * ((abs(year) + 99) // 100)

    def calculate(self, values):
        year = values["year"]
        return f"{year} год — {self.century(year)}-е столетие"


class Task4Widget(BaseTaskWidget):
    title = (
        "Задача 4. Вычислить y(x):\n"
        "  y = lg(x+3),        при −1 ≤ x < 1\n"
        "  y = x⁵ + √(x³+1),   при x > 15\n"
        "  y = 1/(x−5),        иначе"
    )
    fields = [("x", "x =", "0.5", float)]

    def calculate(self, values):
        x = values["x"]
        if -1 <= x < 1:
            return (
                f"Ветка: −1 ≤ x < 1 → y = lg(x+3)\n"
                f"y({x:g}) = {math.log10(x + 3):.6f}"
            )
        if x > 15:
            return (
                f"Ветка: x > 15 → y = x⁵ + √(x³+1)\n"
                f"y({x:g}) = {x ** 5 + math.sqrt(x ** 3 + 1):.6f}"
            )
        if x == 5:
            raise CalcError("x = 5 — деление на ноль!")
        return f"Ветка: иначе → y = 1/(x−5)\n" f"y({x:g}) = {1 / (x - 5):.6f}"


class Task5Widget(BaseTaskWidget):
    title = (
        "Задача 5 (вариант 3).\n"
        "v = (1 + sin²(x+y)) / |x − 2y/(1 + x²y²)| · x^|y| "
        "+ cos²(arctg(1/z))\n\n"
        "Контроль: x = 3.74·10⁻², y = −0.825, z = 16 → v = 1.0553"
    )
    fields = [
        ("x", "x =", "0.0374", float),
        ("y", "y =", "-0.825", float),
        ("z", "z =", "16", float),
    ]

    def calculate(self, values):
        x, y, z = values["x"], values["y"], values["z"]
        if z == 0:
            raise CalcError("z = 0 — arctg(1/z) не определён!")
        denom = abs(x - 2 * y / (1 + x**2 * y**2))
        if denom == 0:
            raise CalcError("Знаменатель равен нулю!")
        p = x ** abs(y)
        if isinstance(p, complex):
            raise CalcError("x^|y| не вещественно (x < 0)!")
        val = (1 + math.sin(x + y) ** 2) / denom * p + math.cos(math.atan(1 / z)) ** 2
        return f"v = {val:.4f}\n(контроль: 1.0553)"


class Task6Widget(BaseTaskWidget):
    title = (
        "Задача 6 (вариант 3). Вычислить c:\n"
        "  c = f(x)² + y² + sin(y),    при x − y = 0\n"
        "  c = (f(x) − y)² + cos(y),   при x − y > 0\n"
        "  c = (y − f(x))² + tg(y),    при x − y < 0"
    )
    fields = [("x", "x =", "2", float), ("y", "y =", "2", float)]

    def setupExtra(self, vbox):
        group = QGroupBox("Функция f(x):")
        g = QVBoxLayout(group)
        self.radioButton_sh = QRadioButton("sh(x)")
        self.radioButton_x2 = QRadioButton("x²")
        self.radioButtonex = QRadioButton("eˣ")
        self.radioButton_sh.setChecked(True)
        for rb in (self.radioButton_sh, self.radioButton_x2, self.radioButtonex):
            g.addWidget(rb)
        vbox.addWidget(group)

    def calculate(self, values):
        x, y = values["x"], values["y"]
        if self.radioButton_sh.isChecked():
            fname, f = "sh(x)", math.sinh
        elif self.radioButton_x2.isChecked():
            fname, f = "x²", lambda t: t**2
        else:
            fname, f = "eˣ", math.exp

        fx = f(x)
        if x == y:
            c, branch = fx**2 + y**2 + math.sin(y), "x − y = 0"
        elif x > y:
            c, branch = (fx - y) ** 2 + math.cos(y), "x − y > 0"
        else:
            c, branch = (y - fx) ** 2 + math.tan(y), "x − y < 0"
        return f"f(x) = {fname} = {fx:.6f}\n{branch} → c = {c:.6f}"


class Task7Widget(BaseTaskWidget):
    title = (
        "Задача 7 (вариант 3). Табулирование функции\n"
        "y = 10⁻¹ · a · x³ · tg(a − b·x)"
    )
    fields = [
        ("x0", "x₀ (начало):", "-0.5", float),
        ("xk", "xk (конец):", "2.5", float),
        ("dx", "dx (шаг):", "0.05", float),
        ("a", "a:", "10.2", float),
        ("b", "b:", "1.25", float),
    ]
    buttonText = "Табулировать"

    def makeOutput(self):
        te = QTextEdit()
        te.setReadOnly(True)
        te.setFont(QFont("Consolas", 10))
        return te

    def set_output(self, text):
        self.out.setPlainText(text)

    def calculate(self, values):
        x0, xk, dx, a, b = values["x0"], values["xk"], values["dx"], values["a"], values["b"]
        if dx == 0:
            raise CalcError("Шаг dx не может быть нулевым!")
        steps = int(round((xk - x0) / dx))
        if steps < 0 or steps > 100000:
            raise CalcError("Проверьте x₀, xk и dx!")

        rows = [f"{'x':>10}  {'y(x)':>16}", "-" * 28]
        for i in range(steps + 1):
            x = x0 + i * dx
            try:
                rows.append(
                    f"{x:10.2f}  " f"{0.1 * a * x ** 3 * math.tan(a - b * x):16.4f}"
                )
            except (ValueError, OverflowError, ZeroDivisionError):
                rows.append(f"{x:10.2f}  {'не определено':>16}")
        rows.append("-" * 28)
        rows.append(f"Точек: {steps + 1}")
        return "\n".join(rows)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("1.3 Разработка приложений — вариант 3")
        self.resize(680, 620)

        tabs = QTabWidget()
        tabs.addTab(Task1Widget(), "Задача 1")
        tabs.addTab(Task2Widget(), "Задача 2")
        tabs.addTab(Task3Widget(), "Задача 3")
        tabs.addTab(Task4Widget(), "Задача 4")
        tabs.addTab(Task5Widget(), "Задача 5 (в.3)")
        tabs.addTab(Task6Widget(), "Задача 6 (в.3)")
        tabs.addTab(Task7Widget(), "Задача 7 (в.3)")

        lay = QVBoxLayout(self)
        lay.addWidget(tabs)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
