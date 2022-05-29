"""
Calculations
"""

class Series:

    def __init__(self, expresion) -> None:
        self.epsilon = 10**-8
        self.times = 10000
        self.expression = expresion

    # def simple_calc(self):
    #     res = 0.0
    #     for x in range(1, self.times):
    #         res += eval(self.expression)
    #     return res

    def calc(self):
        """Limit of partial series sum if exists"""
        current = 0.0
        x = 1
        while x < self.times:
            previous = current
            current += eval(self.expression)
            x += 1
            if current - previous < self.epsilon:
                return current
        return 'Divergence'

    def __str__(self) -> str:
        return str(self.expression)

if __name__ == '__main__':
    #series1 = Series('1/3**x')
    series1 = Series('1/((3*x-2)*(3*x+1))')
    #series1 = Series('1/x**2')
    print(series1.calc())
