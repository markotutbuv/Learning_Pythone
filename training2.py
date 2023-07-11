#Example #1

value_a = float(input("Enter value a: "))
value_b = float(input("Enter value b: "))

value_x = -value_b/value_a

print(f"Result x equal: {value_x}")

#Example #2
from math import sqrt

katet_a = float(input("Enter katet a: "))
katet_b = float(input("Enter katet b: "))

hipotenusa = sqrt(katet_a**2 + katet_b**2)
area = (katet_a*katet_b)/2
print(f"Area of Triangles equals {area}")
print(f"Hipotenusa of Triangles eqals {hipotenusa}")

#Example #3
side_a = float(input("Enter leth of side A "))
perimeter = side_a*4
print(f"Perimeter of the squar equals to {perimeter}")

#Example #4
# Довжина кола - 2*Pi*R
# Площа кола - (Pi*R^2)/2
from math import pi

radius = float(input("Enter radius of a circle "))
lenght = round (2 * pi * radius,2)
area = round((pi * radius**2)/2,2)
print(f"Leght of a circle equals {lenght}",
       f"Area of a circle equals {area}")

#Example #5

number_1 = float(input("Enter your first number "))
number_2 = float(input("Enter your next number "))
number_3 = float(input("Enter your next number "))


sum = abs(number_1) + abs(number_3) +abs(number_2)

print(f"Sum of your number equals to {sum}")

#Example #6

x= float(input("Enter X value "))

equasion = 2*x*4 - 3*x*3 + 4*x*2 - 5*x+6

print(f"sum of equasion is {equasion}")

#Exaample #7

# Distance - sqrt((x2-x1)^2 + (y2-y1)^2)
from math import sqrt

coordinate_x1 = float(input("Enter your first x coordinate  "))
coordinate_x2 = float(input("Enter your second x coordinate "))
coordinate_y1 = float(input("Enter your first y coordinate  "))
coordinate_y2 = float(input("Enter your second y coordinate "))

distance = round(sqrt((coordinate_x2 - coordinate_x1)**2 +\
                (coordinate_y2 - coordinate_y1)**2 ),2)

print(f"result {distance}")

#Example #8
num = float(input("VVedit 4 znachne chislo: "))
num1 = (num // 1000) % 10
num2 = (num // 100) % 10
num3 = (num // 10) % 10
num4 = num % 10

result = (num1 + num2 + num3 + num4) / 4
print(result)

#Example #9

# Input - 123
# Output_one - 5
# Output_two - 4

number = float(input("Enter three digit number"))

number_1 = number//100
number_2 = (number//10) %10
number_3 = number % 10

output_one = number_3 + number_2
output_two = number_3 + number_1

print(f"Output one is - {output_one}, and Output two is {output_two}")


#Example #10
# Input - 971
# Otput - 791

number = int(input("Enter your three digit number "))
number_1 = number//100
number_2 = (number//10) % 10
number_3 = number % 10

output = str(number_2) + str(number_1) + str(number_3)

print(f"Output result is {output}")

#Example #11

search = int(input("Enter amaount of searches "))
MAX_RECORS = 10
pages = (search -1 ) // MAX_RECORS +1

print(f" You will have {pages} pages of materials ")


#Example #12

seconds = int(input("Enter your amount of seconds "))

hours = seconds// 3600
seconds = seconds - hours*3600
minutes = seconds// 60
seconds = seconds - minutes* 60

print(f" Your result is {hours} hours {minutes} minutes {seconds} seconds ")

#Example #13

price_1 = 34.34
price_2 = 12.01
price_3 = 17.42
price_4 = 4.93

total = price_1 + price_2 + price_3 + price_4

dollars = int(total//1 )
cents = int(total % 1 * 100)

print(f"Total amount {dollars} dollars and {cents} cents.")

#Example #14

apartment = int(input("Enter apartment number "))

building = (apartment// 20 + 1 )
floor = ((apartment % 20) //4 + 1 )

print(f" Your apartment is in {building} building and on the {floor} floor ")

# last example

croissants = int(input("Enter amount of Croissants "))
cups = int(input("Enter amount of cups "))
coffee = int(input("Enter amount of coffee "))

croissants_price = 1.04
cups_price = 0.34
coffee_price = 4.42

total_cost = (croissants * croissants_price) + (cups * cups_price) + (coffee_price * coffee)

dollars = int(total_cost)
cents = int(total_cost * 100)

print(f"Total amount of {dollars} dollars and total amount of {cents} cents.")

