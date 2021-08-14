#---calculate the factorial of a number----------/
'''num = int(input("number = "))
fact = 1

for i in range (1,num+1):
    
    fact = fact*i
print(fact)'''

def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number * factorial(number-1)

def factorialTrailingZeros(number): # how many zeros in the factorial of a number
    fac = factorial(number)
    print(fac)
    count = 0
    while(fac%10==0):
        count = count +1
        fac =  fac/10
    return count


if __name__ == '__main__':
    number = int(input("enter a number: "))
    fac = factorial(number)
    print(f"the factorial of {number} is {fac}")
    print(f"{factorialTrailingZeros(number)}")
    
   