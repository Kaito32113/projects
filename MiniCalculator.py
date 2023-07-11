#A mini calculator to calculate all simple and different calculations

num1 = float(input('Enter the first number:'))
num2 = float(input('Enter the second number'))
#num3 = float(input('Enter the third number'))
#num4 = float(input('Enter the fourth nunber'))

print ('Press 1 for addition \nPress 2 for subtraction \nPress 3 for multiplication \nPress 4 for division')

choice = int(input('Enter your choice from 1-4:'))

if choice == 1:
    print('The addition of the given numbers is', num1 + num2)
elif choice == 2:
    print('The subtraction of the given numbers is', num1 - num2 )
elif choice == 3:
    print('The product of the given numbers is', num1 * num2 )
elif choice == 4:
    print('The division of of the two numbers is', num1 / num2)
else:
    print('Invalid Input')