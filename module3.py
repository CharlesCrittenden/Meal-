#Charles Crittenden
#Meal Purchased at a Resturant



no1 = float(input('What was the total amount of your bill?\n'))
#no2 = input('What is your second nunmber?\n')
tip = float(no1)*.18
sales_tax = float(no1)*.07
total = float(no1 + tip + sales_tax)

print (f'Bill: ${no1:.2f}')
#print ('Bill: $%s. ' % round(no1,2))
#print ('Tip Amount: $%s. ' % round(tip,2))
print (f'Tip: ${tip:.2f}')
#print ('Sales Tax: $%s. ' % round(sales_tax,2))
print (f'Sales Tax: ${sales_tax:.2f}')
#print ('Total Bill: $%s. ' % round(total,2))
print (f'Total: ${total:.2f}')


name = input('done\n' )
