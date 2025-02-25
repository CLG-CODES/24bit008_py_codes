#CODE1: Print all aplhabets in upper and in lower case
for i in range(65,91):
    print(chr(i));
for i in range(97,123):
    print(chr(i));

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
#CODE 4:Check if a number is prime,perfect,armstrong palindome and automorphic
inp=int(input("Pls give the number:"));
def prime(inp):
    for i in range(2,inp):
        if inp%i==0:
            print("Not prime!");
            break;
        elif i==inp-1:
            print("Prime!");
def perfect(inp):
    sum=0;
    for i in range(1,inp):
        if inp%i==0:
            sum+=i;
    if sum==inp:
        print("Perfect!");
    else:
        print("Not perfect!");
def armstrong(inp):
    sum=0;
    lenn=len(str(inp));
    num=inp;
    while inp>=1:
            rem=inp%10;
            rem=rem**lenn;
            sum=sum+rem;
            inp=inp//10;
    if sum==num:
        print("Is an Armstrong!");
    else:
        print("Isnt an Armstrong!");
def palindrome(inp):
    inp=str(inp);
    inp_rev=inp[::-1];
    if inp_rev==inp:
        print("Is a Palindrome!");
    else:
        print("Is not a palindrome!");
def automorphic(inp):
    inp_sq=inp**2;
    inp=str(inp);inp_sq=str(inp_sq);
    if inp in inp_sq:
        print("Is Automorphic");
    else:
        print("Is not an automorphic!");
prime(inp);
perfect(inp);
armstrong(inp);
palindrome(inp);
automorphic(inp);

#CODE5: Generate all pythogoras triplets with length less than 30
l=[]
for i in range(1,31):
    for j in range(1,31):
        k=(j**2+i**2)**0.5;
        if k.is_integer():
            l.append((i,j,int(k)));
print("in the format of (X,Y,Z) coordinates:",l)


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

#CODE9: Print N natural numbers in reverse order
num=int(input("input:"));
for i in range(0,num):
    print(num-i);

#CODE 10: Generate N numbers of the fibonnaci series
num=int(input("input:"));
int1=1
int2=1
l=[];k=0;
for i in range(1,num+1):
    print(int1,end=" ");
    int1,int2=int2,int1+int2;


