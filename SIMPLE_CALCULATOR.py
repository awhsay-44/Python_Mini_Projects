def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def modulus(x, y):
    if y == 0:
        return "Cannot perform modulus with zero"
    return x % y

def exponentiate(x, y):
    return x ** y

print("Simple Calculator")
print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Exponentiation")

choice = input("Enter choice (1/2/3/4/5/6): ")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", modulus(num1, num2))
    elif choice == '6':
        print("Result:", exponentiate(num1, num2))
    else:
        print("Invalid operation choice")

except ValueError:
    print("Invalid number entered. Please enter numeric values.")
