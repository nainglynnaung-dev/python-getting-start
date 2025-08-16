
try:
    input1 = int(input("Enter a number: "))
    input2 = int(input("Enter another number: "))
    result = input1 // input2
    print(result)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("You can't divide by any thing")
except ArithmeticError:
    print("You can't divide by any number")
else:
    print(result)
finally:
    print("The program will exit now")
