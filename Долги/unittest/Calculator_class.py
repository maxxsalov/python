class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def division(self):
        try:
            result = self.x / self.y
        except ZeroDivisionError:
            return print("На ноль делить нельзя!")
        else:
            return result