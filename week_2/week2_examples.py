# Week 2 Notes for CP1890
# Author: John Milley
# Date: Sept 20, 2021

print('Week 2 Notes')
print('------------')
print()

# Comments
print('Comments: Descriptive text in your source code that is not compiled/run')
# A block comment takes up an entire line.
# See the first statement below for an line comment

#Statements
print('Statements: pieces/units of code that perform a task')

print('I am a statement') # i am an inline comment
age = 27
total_cost = 9.99 * 1.15
print()

# Comments can also be used to 'comment out' lines of code
# print('I will not be printed')

# Functions
# format of a function: function_name([arguments])

# Data types and variables
# the basic data types are str, int, and float

print('Naming conventions for variables: ')
print('----------------------------------')
print('Varibles should be: \n'
      '- lowercase \n'
      '- begin with a letter \n'
      '- use no spaces, use underscores(_) instead \n'
      '- and, most importantly, meaningfully describe the data it stores')
print()

# Strings (str)
full_name = "Leylah Fernandez"
grade = 'A+'
tax_str = "0.15"

# Integers (int)

x = 1
y = 0
age = 91

# Floats (float)

tax = 0.15 # HST rate in NL
cost = 9.99
total_cost = round((tax + 1) * cost, 2)

print('Two ways to print strings and numbers: ')
print('---------------------------------------')
print(f'Total cost: ${total_cost}')
print('Total cost: $' + str(total_cost))
print()

# Arithmetic

print('Results of arithmetic expressions: ')
print('-----------------------------------')
print(1 + 3 - 2)    # Output: 2 
print(3 / 2)        # Output: 1.5
print(3 // 2)       # output: 1 (decimal is cut off)
print(5 * 2)        # Output: 10
print(5 * 2.5)      # Output: 12.5
print(10 ** 2)      # Output: 100
print()

print('Orders of operation (PEDMAS)')
print('Parentheses, Exponents, Division and Multiplication, Addition and Subtraction')
print('-----------------------------------------------------------------------------')
expression1 = 2 + 1 * 10 - 5
expression2 = (2 + 1) * 10 - 5
print('Are these expressions equal?')
print('2 + 1 * 10 - 5')
print('(2 + 1) * 10 - 5')
print(expression1 == expression2) # testing equality (later chapter)
print()

print('Concatenating Strings')
print('---------------------')
first_character = 'Ellie'
second_character = 'Joel'
# + and f-string
# characters = first_character + ' and ' + second_character
characters = f'{first_character} and {second_character}'
print(characters)
# f-string has the benefit of being able to easily include
# integers and floats in your strings
snow_amt = 107.8
year = 2021
month = 'February'
print(f'In {month}, {year} there was a total of {snow_amt}cm of snow.')
print()

print("Functions")
print("---------")
# This week we learn about a number of built-in python functions.
# Functions are small pieces of code that perform a specific action.
# In future weeks, we'll write our own custom functions
year_str = '2021'
avg_temp = '-2.4'
print(f'9/11 happened {int(year_str) - int(2001)} years ago.')
print(f'The rounded average temperature in January, '
      f'{year_str} was {round(float(avg_temp))}')  








