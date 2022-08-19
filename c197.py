Total = 0
customerName = input("enter your name!")
while(customerName):
    Quantity=int(input("Enter the quantity of item"))
    Items = int(input("Enter the no. of items"))
    Total = Quantity*Items
    repeat = input("DO YOU WANT TO REPEAT THIS PROCESS Y/y/N/n")
    if( repeat=="n" or repeat=="N"):
        break
print("_"*50)
print("GROCERY SHOP")
print("_"*50)
print("Name :",customerName)
print("Total Cost:",Total)  
print()
print("THANK YOU FOR SHOPPING")
print("_"*50)