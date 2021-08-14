print("\t\t\tWELCOME TO PYTHON SUPER MARKET")
def salutaion():
    return print(f"Your Total Bill is Rs.{sum}\nThanks for visiting!\nplease come again")

try:
    sum = 0
    while(True):
        item = input("Enter item name: ")
        price = input("Enter the Item price or press 'q' to quits: ")
        if (price!="q"):
            sum = sum+int(price)
        else:
            salutaion()
            break
except ValueError as e:
    print("sorry sir!\nplease enter valid prices of your purchased items")
except Exception as e:
    print("there is some system error ")

