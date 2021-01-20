while True:
    calculator = int(input("Press #1 To sum \nPress #2 To Sub \nPress #3 To division \nPress #4 To Multi \nPress #5 To Exit"))

    if calculator == 1:
        num1 = float(input("Enter the first number: "))
        num2 =float(input("Enter the second number: "))
        num3 = num1 + num2
        print(num3)
    
    elif calculator == 2:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        number3 = number1 - number2
        print(number3)
    
    elif calculator == 3:
        numb1 = float(input("Enter the first number: "))
        numb2 = float(input("Enter the second number: "))
        numb3 = numb1 / numb2
        print(numb3)

    elif calculator == 4:
        nu1 = float(input("Enter the first number: "))
        nu2 = float(input("Enter the second number: "))
        nu3 = nu1 * nu2
        print(nu3)
    
    elif calculator == 5:
        break
    else:
        print("Enter the choice number !")



        