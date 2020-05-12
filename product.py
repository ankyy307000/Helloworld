cp=float(input("Enter cost price of product:"))
sp=float(input("Enter selling price of product:"))
profit=sp-cp
print("Profit:",profit)
new_sp=(profit+105)/100*cp
print("The selling price in order to increase our current profit by 5%:",new_sp)