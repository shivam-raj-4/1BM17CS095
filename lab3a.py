def div(num):
    for i in range(1,int(num/2+1)):
        if num%i==0:
            print(i,end=" ")
num=int(input("Enter a number"))
print("Divisor of",str(num),"are=")
div(num)
