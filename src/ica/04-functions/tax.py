def add_tax(price,tax_rate):
    print("Inputs: ",price,tax_rate)
    tax_amt = round(price * tax_rate,2)
    print("Amount added for tax: ",tax_amt)
    return price + tax_amt

print(add_tax(25.99,0.0725))
'''
price = 25.99
tax_rate = 0.0725 (7.25%)

tax_amt = 25.99*0.0725 = 1.88
price + tax_amt = 25.99 + 1.88 = 27.87
'''