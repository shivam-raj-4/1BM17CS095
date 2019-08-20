def rev(str1):
    l=str1.split(" ")
    l.reverse()
    a=" "
    s2=a.join(l)
    print(s2)

def rev1(str):
    l=str.split(" ")
    l2=""
    for i in l:
        l2+=i[::-1]
        l2+=" "
    print(l2)

str1=input("Enter the string")
rev(str1)
rev1(str1)
