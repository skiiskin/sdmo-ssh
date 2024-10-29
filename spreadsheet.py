
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value) -> None:
        self._cells[cell] = value

    def get(self, cell: str):
        return self._cells.get(cell, '')

    def evaluate(self, cell: str, visited=None):
        if visited is None:
            visited = set()
        
        if cell in visited:
            return "#Circular"
        
        visited.add(cell)
        
        value = self.get(cell)
        if isinstance(value, int):
            return value
        elif isinstance(value, str):
            if value.isdigit():
                return int(value)
            elif value.startswith("'") and value.endswith("'"):
                return value[1:-1]
            elif value.startswith("="):
                if value[1:].isdigit():
                    return int(value[1:])
                elif value.startswith("='") and value.endswith("'"):
                    return value[2:-1]
                elif value.startswith("='") and not value.endswith("'"):
                    return "#ERROR"
                elif value[1:] in self._cells:
                    return self.evaluate(value[1:], visited)
                else:
                    # Evaluate simple arithmetic expressions but don't allow calculating using float numbers
                    expression = value[1:]
                    try:
                        # Replace cell references in the expression with their evaluated values
                        for ref in self._cells:
                            if ref in expression:
                                ref_value = self.evaluate(ref, visited)
                                if isinstance(ref_value, int):
                                    expression = expression.replace(ref, str(ref_value))
                                else:
                                    return "#ERROR"
                        result = eval(expression)
                        if isinstance(result, int):
                            return result
                        else:
                            return "#ERROR"
                    except ZeroDivisionError:
                        return "#ERROR"
        return "#ERROR"

