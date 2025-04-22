#CODE1: write three functions fun,disp,msg store them in a list and then call them in a loop
def fun():
    print('This is the first one!');
def disp():
    print("This is the second one!");
def msg():
    print("This is the third one!");
l=[fun,disp,msg];
for i in l: i();

#CODE2: Suppose there are two lists, one containing numbers from 1 to 6, and other containing numbers from 6 to 1. Write a program to obtain a list that contains elements obtained by adding
l1=[i for i in range(1,7)];l2=l1[::-1];
mapped=list(map(lambda x,y:x+y,l1,l2));
print(mapped);

#CODE3: Generate the list of 10 different random numbers between -15 and 15. Create a new list by obtaining square of all numbers in a list
import random;
l=[];
for i in range(10):l.append(random.randrange(-15,15));
squarer = lambda x:x**2;
l2=[squarer(i) for i in l];
print(l2);

#CODE4: Consider the following list:lst = ['madam','Python',"malayalam",12321]Write a program to print those strings which are palindromes
lst = ['madam','Python',"malayalam",12321];
palindrome_checker= lambda i: True if str(i)[::-1]==str(i) else False;
for i in lst:
    if palindrome_checker(i): print(i);

#CODE5: A list contains names of Faculty Members. Write a program to filter out those names whose length is more than 8 characters
l=["aaaaaaaaaaaaa","bbbb","cccccc","dddddddddddd"];
len_checker= lambda i: True if len(i)>8 else False;
list_more_than_8=[i for i in l if len_checker(i)];
print(list_more_than_8);
 