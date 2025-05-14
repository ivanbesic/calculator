while True:
    
    def addition(a,b):
        return a + b

    def subtraction(a,b):
        return a - b

    def multiplication(a,b):
        return a * b

    def division(a,b):
        return a / b

    def square (a):
        return a ** 2

    def square_root(a):
        return a ** 0.5


    print("Choose an operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Square")
    print("6 - Square Root")

    choice = int(input('Choose your operation: '))

    choices = { 1 : addition, 2 : subtraction, 3 : multiplication, 4 : division, 5 : square, 6 : square_root}

    if choice in [1,2,3,4]:
        a = float(input('Enter the first number: '))
        b = float(input('Enter the second number: '))

        if choice == 4 and b == 0:
            print("Cannot divide by zero!")
            res = None
        else:
            res = choices[choice](a,b)
        
    elif choice in [5,6]:
        a = float(input('Enter the number: '))
        res = choices[choice](a)

    else:
        print('You picked non-existent option!')
        res = None


    print(f'Result: {res}')

    
    again = input('Do you want to continue again? (yes/no): ')
    if again.lower() != 'yes':
        break





