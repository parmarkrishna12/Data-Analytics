#fibonacci series
a=0
b=1
print(a)
print(b)
n=int(input("Enter a number"))
if n==1:
    print(1)
else:
    print(a)
    print(b)
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)

#check if the number is prime or not
num = int(input("Enter a number to check it is prime or not:"))
if num<=1:
    print("The number is not prime")
else:
    for i in range(2,num):
        if num%i==0:
            print("The number is not prime")
            break
        else:
            print("The number is prime")
            break

#check the number is palindrome number
num = int(input("Enter a number to check it is palindrome number:"))
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if rev == temp:
        print("The number is palindrome")

else:
        print("The number is not palindrome")


