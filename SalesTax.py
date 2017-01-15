#prompt the user for input
purchaseAmount = eval(raw_input('Enter purchase amount:'))

#compute sales tax
tax = purchaseAmount * 0.06

#Displaay tax amount with two digits after decimal point
print 'Sales tax is',int(tax*100)/100
