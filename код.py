import tkinter as tk
import ast
import operator
import math

# Цвета
BG = "#1e1e2e"
DISPLAY_BG = "#313244"
TEXT = "#cdd6f4"
BUTTON_BG = "#45475a"
OPERATOR_BG = "#89b4fa"
EQUAL_BG = "#a6e3a1"
CLEAR_BG = "#f38ba8"

# Окно
root = tk.Tk()
root.title("Мой калькулятор")
root.geometry("340x480")
root.resizable(False, False)
root.configure(bg=BG)

expression = ""
just_calculated = False

display = tk.Entry(
    root,
    font=("Arial", 25),
    bg=DISPLAY_BG,
    fg=TEXT,
    insertbackground=TEXT,
    justify="right",
    bd=0,
    relief="flat"
)
display.pack(fill="x", padx=12, pady=18, ipady=18)

# Разрешённые математические операции
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
    ast.Mod: operator.mod,
}


def safe_calculate(text):
    """Вычисляет только разрешённые математические выражения."""

    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)

        if isinstance(node, ast.Constant):
            if type(node.value) in (int, float):
                return node.value
            raise ValueError("Недопустимое значение")

        if isinstance(node, ast.BinOp):
            operation = OPERATORS.get(type(node.op))
            if operation is None:
                raise ValueError("Недопустимая операция")

            left = evaluate(node.left)
            right = evaluate(node.right)

            if isinstance(node.op, ast.Pow) and abs(right) > 100:
                raise ValueError("Слишком большая степень")

            result = operation(left, right)

            if isinstance(result, complex):
                raise ValueError("Комплексный результат")

            if isinstance(result, float) and not math.isfinite(result):
                raise ValueError("Слишком большое число")

            return result

        if isinstance(node, ast.UnaryOp):
            operation = OPERATORS.get(type(node.op))
            if operation is None:
                raise ValueError("Недопустимая операция")
            return operation(evaluate(node.operand))

        raise ValueError("Недопустимое выражение")

    tree = ast.parse(text, mode="eval")
    return evaluate(tree)


def press(value):
    global expression, just_calculated

    if value == "C":
        expression = ""
        just_calculated = False
        display.delete(0, tk.END)
        return

    if value == "⌫":
        expression = expression[:-1]
        just_calculated = False

    elif value == "=":
        if not expression:
            return

        try:
            result = safe_calculate(expression)

            if isinstance(result, float) and result.is_integer():
                result = int(result)

            expression = str(result)
            just_calculated = True

        except (ValueError, SyntaxError, ZeroDivisionError,
                OverflowError, TypeError):
            expression = "Ошибка"
            just_calculated = True

    elif value == "+/-":
        if expression and expression != "Ошибка":
            if expression.startswith("-"):
                expression = expression[1:]
            else:
                expression = "-" + expression
        just_calculated = False

    elif value == "%":
        if expression and expression != "Ошибка":
            try:
                result = safe_calculate(expression) / 100
                expression = str(result)
            except (ValueError, SyntaxError, ZeroDivisionError,
                    OverflowError, TypeError):
                expression = "Ошибка"
        just_calculated = False

    else:
        if expression == "Ошибка":
            expression = ""

        if just_calculated:
            if value in "+-*/":
                just_calculated = False
            else:
                expression = ""
                just_calculated = False

        expression += value

    display.delete(0, tk.END)
    display.insert(0, expression)
# Кнопки калькулятора
buttons = [
    ["C", "+/-", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["⌫", "0", ".", "="],
]

frame = tk.Frame(root, bg=BG)
frame.pack(expand=True, fill="both", padx=8, pady=5)

for row_index, row in enumerate(buttons):
    frame.rowconfigure(row_index, weight=1)

    for col_index, value in enumerate(row):
        frame.columnconfigure(col_index, weight=1)

        color = BUTTON_BG

        if value in ("/", "*", "-", "+", "%"):
            color = OPERATOR_BG
        elif value == "=":
            color = EQUAL_BG
        elif value == "C":
            color = CLEAR_BG

        button = tk.Button(
            frame,
            text=value,
            font=("Arial", 16, "bold"),
            bg=color,
            fg=BG if color != BUTTON_BG else TEXT,
            activebackground="#b4befe",
            activeforeground=BG,
            relief="flat",
            bd=0,
            command=lambda v=value: press(v)
        )

        button.grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=4,
            pady=4
        )


# Управление с клавиатуры
def keyboard(event):
    char = event.char

    if char in "0123456789.+-*/%":
        press(char)
    elif event.keysym == "Return":
        press("=")
    elif event.keysym == "BackSpace":
        press("⌫")
    elif event.keysym == "Escape":
        press("C")


root.bind("<Key>", keyboard)

root.mainloop()