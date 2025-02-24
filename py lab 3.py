#CODE 1: Count how many vowels are there in string. Accept the string from the user
s1=input("");
s=s1.lower()
i=0
count=0;
for i in range (0,len(s)):
    if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
        count=count+1;
print(count)

#CODE 2: Write your own functions to covnvert lower to upper, upper to lower and toggle case
inp=input("input:");
def makeupper(inp):
    for i in inp:
        if ord(i)>=97 and ord(i)<=122:
            inp=inp.replace(i,chr(ord(i)-32));
    print(inp);
def makelower(inp):
    for i in inp:
        if ord(i)>=65 and ord(i)<=90:
            inp=inp.replace(i,chr(ord(i)+32));
    print(inp);
def maketoggle(inp):
    for i in inp:
        if ord(i)>97 and ord(i)<122:
            inp=inp.replace(i,chr(ord(i)-32));
        elif ord(i)>65 and ord(i)<90:
            inp=inp.replace(i,chr(ord(i)+32));
    print(inp);
makeupper(inp);
makelower(inp);
maketoggle(inp);
    

#CODE 3: Accept two strings, Check weather one string is in another string
s1=input();
s2=input();
b=True;
if s2 not in s1:
    if s1 not in s2:
        b=False;
print(b);

#CODE 4: Write a function that removes one string from another string
s1=input("Main String:");
s2=input("Remove this from Main String:");
s1=s1.replace(s2,"");
print(s1);
