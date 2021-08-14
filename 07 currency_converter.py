from os import write
with open("currencyData.txt" ) as f:
    x = f.readlines()

currencyDict = {}
for line in x:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

print("\t\tWELCOME TO PYTHON CURRENCY CONVERTER")
amount = int(input("Enter Amount: "))
print("enter the name of currency you want to convert to: ")
[print(item) for item in currencyDict.keys()]
currency = input("please enter the one of these values: ")
print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency}")
    

    
    
