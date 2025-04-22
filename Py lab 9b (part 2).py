#CODE1:If a positive integer is entered through the keyword, write a recursive function to obtain the prime factors of the number.
i1=int(input("Pls give the number:"));
l=[]
def primefax(i1,l,div):
    if i1==1: return l;
    if i1%div==0:
        l.append(div);
        return primefax(i1//div,l,div);
    else: primefax(i1,l,div+1)        
primefax(i1,l,2)
print(l)

#CODE2: A positive integer is entered through the keyboard. Write a function to find its binary equivalent of this number.
num=int(input("Pls give num:"));
s="";
def Convert_to_bin(num,s):
    if num==1:
        s+="1";
        return s[::-1];
    if num%2==0:
        s+="0";
        return Convert_to_bin(num//2,s);
    else:
        s+="1";
        return Convert_to_bin((num-1)//2,s);
print(Convert_to_bin(num,s));

#CODE3:A string is entered through the keyboard. Write a recursive function that counts the number of vowels in this string.
i1=input("Pls give input:");
def counter(i1,d):
    if i1=="": return d;
    if i1[0] in "aeiouAEIOU":
        return counter(i1[1:],d+1);
    return counter(i1[1:],d);   
print(counter(i1,0))

#CODE4:Write a recursive function that reverses the list of numbers that it receives
l1=[1,2,3,4,5];
l2=[];
def rev(l1,l2):
    if len(l1)==0: return l2;
    else: l2.append(l1[-1]); return rev(l1[:-1],l2);
print(rev(l1,l2))

#CODE5: Calculate a^b where a and b received through the keyword using recursion.   
a=int(input("Pls give the value of a:"));
b=int(input("Pls give the value of b:"));
def pow(a,b,product):
    if b==0: return product;
    return pow(a,b-1,product*a);
print(pow(a,b,product=1));

#CODE6: A list contains some negative and some positive values. Write a recursive function that sanitizes the list by replacing all negative numbers with 0.
l1=[1,-1,0,-2,6,-9,5]
def sanitizer(l1,i=0):
    if i==len(l1): return  l1;
    if l1[i]<0: l1[i]=0;
    return sanitizer(l1,i+1);
print(sanitizer(l1));

#CODE7: Write a recursive function to obtain average of all numbers present in a given list.
l=[1,2,3,4,5];
def avg(l,lenn,sum=0):
    if len(l)==0: return sum/lenn;
    return avg(l[1:],lenn,sum+l[0]);
print(avg(l,len(l)));

#CODE8:Write a recursive function to obtain length of a given string
i=input("Pls give a string:");
def lenn(i):
    if len(i)==0: return 0;
    return 1+lenn(i[1:]);
print(lenn(i));
