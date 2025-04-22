#CDOE 1: Write a program, which defines count_lower_upper which accepts a string and calculates the amount of lower and upper case alphabets, written the value as dicto
s=input()
def count_lower_upper(s):
    upper=0;
    lower=0;
    for i in s:
        val=ord(i);
        if val>=65 and val<=90: 
            upper+=1;
        if val>=97 and val<=122:
            lower+=1;
    d1={"upper":upper,"lower":lower}
    return d1;
print(count_lower_upper(s))

#CODE 2: Write a program that computes n+nn+nnn+nnnn where n is the digit given by user, test for 4 to 7
n=int(input("Here:"));
def compute(n):
    return n**1+n**2+n**3+n**4;
for i in range(4,8):
    print(compute(i));

#CODE 3: Write a code to create an array where first 3 are the dimensions of a 3d array and 4 is the value
x=int(input("pls give value of x:"));
y=int(input("pls give value of y:"));
z=int(input("pls give value of z:"));
n=int(input("Pls give value:"));
def create_array(n,x,y,z):
    l=[[[n for _ in range(x)] for _ in range(y)] for _ in range(z)];
    return l;
print(create_array(n,x,y,z));


#CODE 4:write a function that returns total and average of 5 subjetcs
s1=1;s2=2;s3=3;s4=4;s5=5;
def sum_avg(s1,s2,s3,s4,s5):
    total=s1+s2+s3+s4+s5;
    avg=total/5;
    return (total,avg);
sum_avg(s1,s2,s3,s4,s5
           
#CODE 5:Panagram checker
inp=input("Here:");
def panagram(inp):
    s="qwertyuiopasdghjklzxcvbnm";
    inp=inp.lower();
    for i in inp:
        if i in s: s=s.replace(i,"");
    if s=="": return  True;
    return False;
print(panagram(inp));

#CODE6 : return a list containing tuples inthe form of (x,x^2,x^3) for all values from 1 to end point given by user
n=int(input(""));
def lister(n):
    l1=[];
    for i in range(1,n+1):
        l1.append((i,i**2,i**3));
    return l1;
print(lister(n));

#CODE7: write a word that checks for palindromes ignore sapce and case
s=input();
def ispalindrome(s):
    s=s.lower()
    l=list(s);
    s=""
    for i in l:
        if i!=" ":
            s+=i;
    if s==s[::-1]:
        return True;
    return False;    
print(ispalindrome(s))

#CODE 8: Write a code which removes all duplicate words and sorts a string in alphanumeric format,return a string
inp=input("Pls give:");
l1=inp.split(" ");
s1=set(l1);
l1=list(s1);
l1.sort();
s=" ".join(l1);
print("Sorted by 1)numbers,2)capital letters,3)small letters",s)


#CODE9 : Count the amount of alphabets and digits in a string, return a dictonary
inp=input("Pls provide the string:");
def counter(inp):
    al_count=0;di_count=0;
    for i in inp:
        if i.isalpha(): al_count+=1;
        elif i.isdigit(): di_count+=1;
    return {"alphabet count":al_count,"digit count":di_count};
print(counter(inp));

#CODE10: write a function to find the frequency of words in a sentance, return the frequency in a sorted manner
inp=input("Pls give:");
def  frequency(inp):
    l1=inp.split();d={};
    for i in l1:
        if i not in d: d.update({i:1});
        else: d[i]+=1;
    d=sorted(d.items());
    return d;
print(frequency(inp))   

#CODE11: Write a code create_list() which returns an intersection of two lists
l1=[1,2,3];
l2=[2,3,4];
def create_list(l1,l2):
    l3=[i for i in l1 if i in l2];
    return(l3);
print(create_list(l1,l2));


    


