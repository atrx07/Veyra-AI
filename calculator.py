"""Provide safe calculator parsing and arithmetic for Veyra."""


SUPPORTED_OPERATORS = {"+", "-", "*", "/"}
USAGE_GUIDANCE = "Try: calculate 12 + 8"


def parse_expression(command):
    """Parse a space-delimited calculator command into two numbers and an operator."""
    parts = command.split()
    if len(parts) != 4 or parts[0] != "calculate":
        raise ValueError(USAGE_GUIDANCE)

    operator = parts[2]
    if operator not in SUPPORTED_OPERATORS:
        raise ValueError("I support only +, -, *, and / operators.")

    try:
        left = float(parts[1])
        right = float(parts[3])
    except ValueError as error:
        raise ValueError(
            "Please use numeric operands, such as: calculate 12 + 8"
        ) from error

    return left, operator, right


def calculate(left, operator, right):
    """Perform one of Veyra's four supported arithmetic operations."""
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("I can't divide by zero.")
        return left / right

    raise ValueError("I support only +, -, *, and / operators.")


def format_result(result):
    """Format whole-number results without an unnecessary decimal suffix."""
    if result.is_integer():
        return str(int(result))
    return str(result)


def get_calculation_response(command):
    """Return a calculator result or a friendly recoverable error message."""
    try:
        left, operator, right = parse_expression(command)
        result = calculate(left, operator, right)
    except (ValueError, ZeroDivisionError) as error:
        return f"Veyra: {error}"

    return f"Veyra: The result is {format_result(result)}."
