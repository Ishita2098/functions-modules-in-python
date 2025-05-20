def factorial(n):
    if n<2:
        return 1 
    else:
        return n * factorial(n-1)
num=int(input("Enter a number : "))
if num<0:
    print("this value is not define ")
else:
    print("factorial value is ",factorial(num))