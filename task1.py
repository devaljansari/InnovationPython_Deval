'''1. Create three variables in a single line and assign different values to them and
make sure their data types are invited differently. Like one is int, another one is float
and last one is string. a = 1; b = 2.01; c = 'string' '''

a, b, c = 1, 2.01, 'Deval'
print(a,b,c)


'''2. Create a variable of value type complex and swap it with another variable
whose value is an integer.'''

x = 2+8j
y = 14
print('Original Value: ', x, y)
x , y = y, x
x = x + y
y = x - y
print('Swap Value by method 1: ',x, y)
x = int((x-y).real)
print('Swap Value by method 2: ',x, y)

'''3. Swap two numbers using third variable as result name and do the same task
without using any third variable.'''
x = 10
y = 12
print('Original Value: ', x, y)
result = x
x = y
y = result
print('Swap Value using third variable: ',x, y)
x , y = y, x
print('Swap Value without using third variable: ',x, y)


'''4. Write a program to print the value given by the user by using both Python 2.x
and Python 3.x Version.'''
## Python 2
##x = int(raw_input("Enter an interger :"))

## Python 3
x = int (input("Enter an integer: "))


'''5. Write a program to complete the task given below:
Ask user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.
Use z for adding 30 into it and print the final result by using variable result.'''
x = int(input('Enter first no:'))
y = int(input('Enter second no:'))
z = x + y
z +=30
print('Result: ', z)

'''6. Write a program to check the data type of the entered values. HINT: Printed
output should say - The input value data type is : int/float/string/etc'''
x = int(input('Enter first number:'))
y = float(input('Enter second number:'))
print('Dtype of x: ', type(x))
print('Dtype of y: ', type(y))

'''7. Create Variable using CamelCase, LadderCase and UPPERCASE. (Refer:https://capitalizemytitle.com/
camel-case/)'''




'''8. If one data type value is assigned to ‘a’ variable and then a different data type
value is assigned to ‘a’ again. Will it change the value. If Yes then Why?'''
x = 5
print(type(x))

x = 5.5
print(type(x))

x = 'string'
print(type(x))

# datatype changes are it is a fresh re-assignment!