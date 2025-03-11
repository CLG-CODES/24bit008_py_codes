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
n=int(input("Here:"));


#CODE 4:write a function that returns total and average of 5 subjetcs
s1=1;s2=2;s3=3;s4=4;s5=5;
def sum_avg(s1,s2,s3,s4,s5):
    total=s1+s2+s3+s4+s5;
    avg=total/5;
    return (total,avg);
sum_avg(s1,s2,s3,s4,s5)
#CODE 5:Panagram checker
s=input();
def ispanagram(s):
    s=set(s);
    s1=set("qwertyuioplkjhgfdsamnbvcxz");
    if s1 in s:
        return True;
    else:
        return False;
print(ispanagram(s))

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
    


