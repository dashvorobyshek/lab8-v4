def calculate(left: float, right: float, operation: str) -> float:
    """Выполняет выбранную арифметическую операцию."""
    if operation == "+":
        return left + right
    if operation == "-":
        return left - right
    if operation == "*":
        return left * right
    if operation == "/":
        if right == 0:
            raise ZeroDivisionError("На ноль делить нельзя.")
        return left / right
    raise ValueError(f"Неизвестная операция: {operation}")
