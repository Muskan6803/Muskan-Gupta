# Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
#   Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#   Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == 'add':
            return self.a + self.b
        elif self.operation == 'subtract':
            return self.a - self.b
        elif self.operation == 'multiply':
            return self.a * self.b
        elif self.operation == 'divide':
            if self.b == 0:
                return "Error: Cannot divide by zero"
            return self.a / self.b
        else:
            return "Error: Invalid operation"

# Example usage
calc1 = Calculator(10.0, 5.0, 'add')
print("Addition Result:", calc1.calculate())

calc2 = Calculator(10.0, 5.0, 'divide')
print("Division Result:", calc2.calculate())

calc3 = Calculator(10.0, 0.0, 'divide')
print("Division by Zero:", calc3.calculate())
