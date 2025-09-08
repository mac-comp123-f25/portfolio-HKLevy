change=268 #give in cents
dollars=change//100
change=change-dollars*100
quarters=change//25
change=change-quarters*25
dimes=change//10
change=change-dimes*10
nickels=change//5
change=change-nickels*5
pennies=change
print('''Your change is given as:
''',dollars,'''dollars
''',quarters,'''quarters
''',dimes,'''dimes
''',nickels,'''nickels
''',pennies,'''pennies''')