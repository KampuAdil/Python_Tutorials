# take three values from user
name = input("Enter Employee Name: ")
salary = input("Enter salary: ")
company = input("Enter Company name: ")

# Display all values on screen
print("\n")
print("Printing Employee Details")
print("Name", "Salary", "Company")
print(name, salary, company)


# Python 2 code
# raw_input() function
name = raw_input("Enter your name ")
print "Student Name is: ", name
print type(name)

age = raw_input("Enter your age ")
print "Student age is: ", age
print type(age)

#Get Multiple inputs From a User in One Line
name, age, marks = input("Enter your Name, Age, Percentage separated by space ").split()
print("\n")
print("User Details: ", name, age, marks)

#Command Line input
from sys import argv

print("Total argument passed :", len(argv))
print(type(argv))

print("All command line inputs")
for value in argv:
    print(value)
    
#In Python, by default, command-line arguments are available in string format.

add = int(argv[1]) + int(argv[2])
print('Addition is:', add)


name = input('Enter Name ')
zip_code = int(input('Enter zip code '))
street = input('Enter street name ')
house_number = int(input('Enter house number '))

# Display all values separated by hyphen
print(name, zip_code, street, house_number, sep="-")

#Output Formatting


name = input("Enter Name ")
marks = input("Enter marks ")

print("\n")
print('FirstName - {0}, LastName - {1}'.format('Ault', 'Kelly'))
print('{0} got {1}%'.format(name, marks))
print('Student: Name:  {firstName}, Marks: {percentage}%'.format(firstName=name, percentage=marks))

#sign
positive_number = float(input("Enter Positive Number "))
negative_number = float(input("Enter Negative Number "))

print("\n")
# sign '+' is for both positive and negative number
print('{:+f}; {:+f}'.format(positive_number, negative_number))

# sign '-' is only for negative number
print('{:f}; {:-f}'.format(positive_number, negative_number))


#display number in Various Formats

number = int(input("Enter number "))

print("\n")
# 'd' is for integer number formatting
print("The number is:{:d}".format(number))

# 'o' is for octal number formatting, binary and hexadecimal format
print('Output number in octal format : {0:o}'.format(number))

# 'b' is for binary number formatting
print('Output number in binary format: {0:b}'.format(number))

# 'x' is for hexadecimal format
print('Output number in hexadecimal format: {0:x}'.format(number))

# 'X' is for hexadecimal format
print('Output number in HEXADECIMAL: {0:X}'.format(number))

#float type 

number = float(input("Enter float Number "))

print("\n")
# 'f' is for float number arguments
print("Output Number in The float type :{:f}".format(number))

# padding for float numbers
print('padding for output float number{:5.2f}'.format(number))

# 'e' is for Exponent notation
print('Output Exponent notation{:e}'.format(number))

# 'E' is for Exponent notation in UPPER CASE
print('Output Exponent notation{:E}'.format(number))

#output String Alignment

text = input("Enter String ")

print("\n")
print("Left justification", text.ljust(60, "*"))
print("Right justification", text.rjust(60, "*"))
print("Center justification", text.center(60, "*"))
