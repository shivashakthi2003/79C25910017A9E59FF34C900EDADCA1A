#Recursive Function-Factorial
def Factorial (n):
    if n==0:
       return 1
    else:
      return n*Factorial (n-1) #recirsive call
print(format ("FACTORIAL-RECURSIVE",'^40'))
n=int (input ("Enter number to find factorial:"))
print ("Factorial of ",n,"is :",Factorial (n))
