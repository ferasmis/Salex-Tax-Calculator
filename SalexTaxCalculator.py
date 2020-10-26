## Author: Feras Isied
## Problem: A program that calculates the cost after sale tax for an item,
##   given the item price and the state sale tax
##Formula: The cost after tax = the item cost + (cost * state sale tax)

# user input parsed to a float
itemCost = float(input('Please enter the Item Cost: \n $'))
saleTaxPercentage = float(input('Please enter the percentage of State Sale Tax: \n %'))

# formula: Cost of item + (cost of item * sale tax percentage/100)
totalAfterTax = itemCost + (itemCost * saleTaxPercentage/100)

# print the total after tax
print('The total after State Tax Sale: \n $' + str(totalAfterTax))
