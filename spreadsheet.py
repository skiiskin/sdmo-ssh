
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value) -> None:
        self._cells[cell] = value

    def get(self, cell: str):
        return self._cells.get(cell, '')

    def evaluate(self, cell: str):
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
                elif value[1:] in self._cells:
                    return self.evaluate(value[1:])
        return "#ERROR"

