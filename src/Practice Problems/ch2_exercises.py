'''
a place for me to do practice exercises from the book
I used triple quotes for questions I finished so that
I didn't have to go through all the questions every time
I ran the program
'''

#question 1 done in the book
#question 2 did not give needed information
#question 3 - hours for an alarm
'''time_now=int(input("What time is it now in whole hours? "))
hours_to_wait=int(input("How many whole hours should you wait for the alarm? "))
time_of_alarm=(time_now+hours_to_wait)%24
print("When the alarm goes off, it will be ",time_of_alarm)'''

#question 4 - days for a trip
'''start_day=int(input("What is the starting day's number? "))
trip_length=int(input("How long in whole days is the trip? "))
return_day=(start_day+trip_length)%7
print("When you return from the trip, it will be day",return_day)'''

#question 5 - joining strings together
'''w1="All "
w2="work "
w3="and "
w4="no "
w5="play "
w6="makes "
w7="Jack "
w8="a "
w9="dull "
w10="boy."
print(w1+w2+w3+w4+w5+w6+w7+w8+w9+w10)
print(w1,w2,w3,w4,w5,w6,w7,w8,w9,w10)
#using commas (line 29) added spaces, so I wouldn't need spaces in the variables
#not using commas (line 28) didn't add spaces, so I would need spaces in the variables'''

#question 6 - order of operations practice
'''print(6*1-2)
print(6*(1-2))'''

#question 7 - calculating compound interest
'''p=10000
n=12
r=0.08
t=int(input("How many whole years will this money be compounded for? "))
final_amount=p*(1+r/n)**(n*t)
print("After",t,"years, the final amount is",final_amount)'''

#question 8 - area of a circle
'''r=float(input("What is the radius of the circle? "))
area=3.14159*r**2 #3.14159 is pretty accurate. 3.14 is okay
print("The area of the circle is",area)'''

#question 9 - area of a rectangle
'''length=float(input("How long is the rectangle? "))
width=float(input("What is the width of the rectangle? "))
area=length*width
print("The area of the rectangle is",area)'''

#question 10 - miles/gal
'''miles_driven=float(input("How many miles were driven? "))
gallons_used=float(input("How many gallons were used? "))
mpg=miles_driven/gallons_used
print("You got",mpg,"miles per gallon")'''

#question 11/12 - temperature converter
celsius=float(input("What is the temperature in Celsius? "))
fahrenheit=(celsius*9/5)+32
print("The temperature in Fahrenheit is",fahrenheit)

fahrenheit=float(input("What is the temperature in Fahrenheit? "))
celsius=(fahrenheit-32)*5/9
print("The temperature in Celsius is",celsius)