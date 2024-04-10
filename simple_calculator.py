while True:
    
    print("MENU\n 1. Add \n 2. subtract \n 3. times \n 4. divide \n 5. Modulus")

    menu = int(input("Choose menu (1/2/3/4/5): "))
    number1 = float(input("Input first number: "))
    number2 = float(input("Input second number: "))

    if menu == 1:
        print(number1 + number2)
    elif menu == 2:
        print(number1 - number2)
    elif menu == 3:
        print(number1 * number2)
    elif menu == 4:
        if number2 == 0:
            print("Invalid number!")
        else:
            print(number1 / number2)
    elif menu == 5:
        print(number1 % number2)

    choose = input("would you like to continue? (Y/N): ")
    if choose == "N":
        print("Finish")
        break
    elif choose == "Y":
        continue 