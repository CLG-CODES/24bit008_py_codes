#CODE1: Print all aplhabets in upper and in lower case
#CODE2: Print a multiplication of a given number
num=int(input("Pls give the number:"));
i=1
for i in range (1,13):
    print(num,"times",i,"is",num*i);
#CODE3: Count no of alphabet and no of digits in any given in a string
str=input("Pls give the string:");
alphacount=0
intcount=0
for i in range(0,len(str)):
    if str[i].isalpha():
        alphacount = alphacount +1;
    if str[i].isdigit():
        intcount = intcount +1;
        
print(alphacount);
print(intcount);

#CODE7: Print N C R , N P R
n=int(input("pls give N:"));
r=int(input("pls give R:"));
def factorial(num):
    fact=1;
    for i in range(1,num+1):
        fact=fact*i
    return fact;
ncr=factorial(n)/(factorial(n-r)*factorial(r))
npr=factorial(n)/factorial(n-r)
print("ncr:",ncr,"npr",npr);
    
#CODE8: Print the factorial of a number
num=int(input("pls give:"));
fact=1;
for i in range(1,num+1):
    fact=fact*i
print(fact);
