class Cell:
    def __init__(self, core):
        self.core = core

    def __add__(self, other):
        return self.core + other.core

    def __sub__(self, other):
        if self.core - other.core > 0:
            return self.core - other.core
        else:
            return 'Разность количества ячеек двух клеток меньше нуля!'

    def __mul__(self, other):
        common_cell = self.core * other.core
        return common_cell

    def __floordiv__(self, other):
        common_cell = self.core // other.core
        return common_cell

    def make_order(self, row):
        all_row = ''
        for i in range(self.core):
            if i % row != 0:
                all_row += '*'
            else:
                all_row += '\n*'
        return all_row


c_one = Cell(12)
c_two = Cell(3)
print(c_one + c_two)
print(c_one - c_two)
print(c_one * c_two)
print(c_one // c_two)
print(c_one.make_order(5))
