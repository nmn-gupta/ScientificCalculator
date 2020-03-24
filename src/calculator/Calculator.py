import cmath
import math

print("Welcome to the Naman's calculator")
print("Press 1 for Arithmetic calculations")
print("Press 2 for Trigonometry calculations")
print("Press 3 for Base conversion calculations")
print("Press 4 for complex number calculations")
choice = int(input("Enter the your choice:"))
if choice == 1:
    while True:
        num1 = int(input("Enter the number:"))
        s = input("Enter the operation:")

        if s == "+":
            num2 = int(input("Enter the number:"))
            print(num1 + num2)
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break
        if s == "*":
            num2 = int(input("Enter the number:"))
            print(num1 * num2)
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break

        if s == "/":
            num2 = int(input("Enter the number:"))
            print(int(num1 / num2))
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break
        if s == "%":
            print(num1 / 100)
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break
        if s == "-":
            num2 = int(input("Enter the number:"))
            print(num1 - num2)
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break
        if s == "^":
            num2 = int(input("Enter the number:"))
            print(pow(num1, num2))
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break
        if s == "sqrt":
            print(int(pow(num1, 0.5)))
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break

if choice == 2:
    while True:
        s = input("Enter the operation:")
        if s == "sine":
            x = eval(input("Enter the degree:"))
            if x == 90 or x == 0:
                print(int(math.ceil(math.sin(x))))
                u = input("Do you want to continue(y/n):")
                if u == "y":
                    pass
                else:
                    break
            else:
                print(round(math.sin(math.radians(x)), 4))
                u = input("Do you want to continue(y/n):")
                if u == "y":
                    pass
                else:
                    break

        if s == "cos":
            x = eval(input("Enter the degree:"))
            if x == 90 or x == 0:
                print(int(math.ceil(math.cos(x))))
                u = input("Do you want to continue(y/n):")
                if u == "y":
                    pass
                else:
                    break
            else:
                print(round(math.cos(math.radians(x)), 4))
                u = input("Do you want to continue(y/n):")
                if u == "y":
                    pass
                else:
                    break

        if s == "tan":
            x = eval(input("Enter the degree:"))
            if x == 45:
                print(int(math.floor(math.tan(x))))
                u = input("Do you want to continue(y/n):")
                if u == "y":
                    pass
                else:
                    break
            else:
                print(round(math.tan(math.radians(x)), 4))
                u = input("Do you want to continue(y/n):")
                if u == "y":
                    pass
                else:
                    break

        if s == "cos inverse":
            x = eval(input("Enter the value:"))
            if x == 1 or x == 0:
                print(int(math.degrees(math.acos(x))))
                u = input("Do you want to continue(y/n):")
                if u == "y":
                    pass
                else:
                    break
            else:
                print(math.floor(math.degrees(math.acos(x))))
                u = input("Do you want to continue(y/n):")
                if u == "y":
                    pass
                else:
                    break

        if s == "sine inverse":
            x = eval(input("Enter the value:"))
            if x == 1 or x == 0:
                print(int(math.degrees(math.asin(x))))
                u = input("Do you want to continue(y/n):")
                if u == "y":
                    pass
                else:
                    break
            else:
                print(math.floor(math.degrees(math.asin(x))))
                u = input("Do you want to continue(y/n):")
                if u == "y":
                    pass
                else:
                    break

        if s == "tan inverse":
            x = eval(input("Enter the value:"))
            if x == 1 or x == 0:
                print(int(math.degrees(math.atan(x))))
                u = input("Do you want to continue(y/n):")
                if u == "y":
                    pass
                else:
                    break
            else:
                print(math.floor(math.degrees(math.atan(x))))
                u = input("Do you want to continue(y/n):")
                if u == "y":
                    pass
                else:
                    break

if choice == 3:
    while True:
        fro = input("from (decimal/binary/octal/hexadecimal) :")
        num = input("Enter the number: ")
        to = input("to (decimal/binary/octal/hexadecimal) :")

        if fro == "decimal" and to == "binary":
            print(bin(int(num))[2:])
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break
        if fro == "decimal" and to == "octal":
            print(oct(int(num))[2:])
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break
        if fro == "decimal" and to == "hexadecimal":
            print(hex(int(num))[2:])
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break

        if fro == "octal" and to == "decimal":
            print(int(num, 8))
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break
        if fro == "octal" and to == "binary":
            print(bin(int(num, 8))[2:])
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break
        if fro == "octal" and to == "hexadecimal":
            print(hex(int(num, 8))[2:])
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break

        if fro == "binary" and to == "decimal":
            print(int(num, 2))
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break
        if fro == "binary" and to == "octal":
            print(oct(int(num, 2))[2:])
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break
        if fro == "binary" and to == "hexadecimal":
            print(hex(int(num, 2))[2:])
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break

        if fro == "hexadecimal" and to == "decimal":
            print(int(num, 16))
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break
        if fro == "hexadecimal" and to == "binary":
            print(bin(int(str(145), 16))[2:])
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break
        if fro == "hexadecimal" and to == "octal":
            print(oct(int(str(145), 16))[2:])
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break
if choice == 4:
    while True:
        num1 = eval(input("Enter the first number: "))
        num2 = eval(input("Enter the second number: "))
        z = complex(num1, num2)
        # print("Complex number :",z)
        # print("Phase( angle of the complex number is: ",cmath.phase(z))
        # print("Modulus : ", abs(z))
        # print("Real part :",z.real)
        # print("Imaginary part :",z.imag)
        fro = input("from (rectangular/polar): ")
        to = input("to (rectangular/polar): ")
        if fro == "polar" and to == "rectangular":
            print("Rectangular form: ", cmath.rect(abs(z), cmath.phase(z)))
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break
        if fro == "rectangular" and to == "polar":
            print("Polar coordinates: ", cmath.polar(z))
            u = input("Do you want to continue(y/n):")
            if u == "y":
                pass
            else:
                break
