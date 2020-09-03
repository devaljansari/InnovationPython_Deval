## 1.
# x = int(input('Enter number: '))
# if x%3 == 0 and x%5 == 0:
#     print('ConsultAdd Python Training')
# elif x%3 == 0:
#     print('ConsultAdd')
# elif x%5 == 0:
#     print('c')
# else:
#     print('not divisible by 3, 5 or both')

##2

# x = int(input('Enter first number: '))
# y = int(input('Enter second number: '))
# o = int(input('Which operation do you want to perform?: '))
# if o ==1 :
#   z = x + y
#   print('Addition: ', z)
# elif o == 2:
#   z = x - y
#   print('Subtraction: ', z)
# elif o == 3 :
#   z = x / y
#   print('Division: ', z)
# elif o == 4:
#   z = x * y
#   print('Multiplication: ', z)
# elif o == 5:
#   a = int(input('Enter first number: '))
#   b = int(input('Enter second number: '))
#   z = (a + b)/2
#   print('Average: ', z)
# if z < 0:
#   print ("NEGATIVE")

##3. Write a program in Python to implement the given flowchart:
# a = int(input('Enter 1st value: '))
# b = int(input('Enter 2nd value: '))
# c = int(input('Enter 3rd value: '))
# avg = (a + b + c)/3
# print("Avg =", avg)
# if avg > a and avg > b and avg > c:
#   print('Avg is more than a , b, c')
# elif avg > a and avg > b:
#   print('Avg is more than a , b')
# elif avg > a and avg > c:
#   print('Avg is more than a , c')
# elif avg > b and avg > c:
#   print('Avg is more than b , c')
# elif avg > a:
#   print('Avg is just higher than a')
# elif avg > b:
#   print('Avg is just higher than b')
# elif avg > c:
#   print('Avg is just higher than c')

#4. Write a program in Python to break and continue if the following cases occurs:
# ● If user enters a negative number just break the loop and print “It’s Over”
# ● If user enters a positive number just continue in the loop and print “Good Going”
# x = int(input('Enter value: '))
# if x < 0:
#   print("It's over!")
# else:
#   print('Good Going!')

'''5. Write a program in Python which will find all such numbers which are divisible by 7 but are 
not a multiple of 5, between 2000 and 3200.'''
# values = []
# for i in range(2000, 3201):
#   if i%7 == 0 and i%5 != 0:
#     values.append(i)
# print(values)

'''6. What is the output of the following code examples?'''
# x = 123
# for i in x:
#   print(i)

# i = 0
# while i < 5:
#   print(i)
#   i += 1
#   if i == 3:
#     break
#   else:
#     print("error")

# count = 0
# while True:
#   print(count)
#   count += 1
#   if count >= 5:
#     break

'''7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
Expected output: 0 1 2 4 5 Note: Use ‘continue’ statement'''
# for i in range(0,7):
#   if i == 3 or i == 6:
#     continue
#   else:
#     print(i)

'''8. Write a program that accepts a string as an input from user and calculate the
number of digits and letters. Expected output: consul12  Letters 6  Digits 2'''
x = input('Enter an aphanumeric text: ')
digits = 0
letters = 0
for i in x:
  if i.isdigit():
    digits += 1
  elif i.isalpha():
    letters += 1
print('Digits: ', digits)
print('Letters: ', letters)

'''9. Read the two parts of the question below:
● Write a program such that it asks users to “guess the lucky number”. If the correct number is 
guessed the program stops, otherwise it continues forever.
● Modify the program so that it asks users whether they want to guess again each time. Use two 
variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue 
guessing. The program stops if the user guesses the correct number or answers “no”. ( The program 
continues as long as a user has not answered “no” and has not guessed the correct number)'''





'''10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
such as
counter=1
While counter <= 5:
print(“Type in the”, counter, “number”
counter=counter+1

The program asks for five guesses (no matter whether the correct number was guessed or not). If the 
correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. 
After the fifth guess it stops and prints “Game over!”.'''




'''11. In the previous question, insert “break” after the “Good guess!” print statement. “break” will 
terminate the while loop so that users do not have to continue guessing after they found the number. 
If the user does not guess the number at all, print “Sorry but that was not very successful”.'''