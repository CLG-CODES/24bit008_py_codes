#CODE 1: Write a program to convert words present in a n list and convert thtme to uppercase
l=["hello","i","am","Parth"];
s=set();
for i in l:
    s.add(i.upper());
print(s);
#CODE 2: Make a code with 10 random numbers in a set in the range 15 to 45, count how many are less than 30, delete all which are more than 35
import random
s=set();
count=0;
while len(s)<10:
    s.add(random.randint(15,45));
s1=s
print(s);
for i in s:
    if i<30:
        count+=1;
for i in s.copy():
    if i>35:
        s.discard(i);
print(s);
print(count);

#CODE 3:Create a new empty set, add 5 names to set then modifiy one name and delete two names
s=set()
s1={"a","b","c","d","e"}
s.update(s1);
l1=list(s);
l1[0]="z";
l1.pop(1);
l1.pop(2);
s=set(l1);
print(s);

#CODE 4:A set has names starting with a or b, write a code to split into 2 sets, one from a and other from b
s={"aa","ab","ba","bb"}
s1=set();s2=set();
for i in s:
    if i[0]=="a":
        s1.add(i);
    else:
        s2.add(i)