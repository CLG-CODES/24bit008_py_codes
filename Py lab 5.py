import random
#CODE1:
#CODE2:Generate 20 random numbers ans store them in a list, accept a number from the user and print all occurances of it
f_list = []
for i in range(20):
    f_list.append(random.randrange(1,100));
inp = int(input("number"));
position=[];
for index in range(len(f_list)):
    if f_list[index]==inp:
        position.append(index);
print(f_list);
if position:
    print(position);
  
#CODE3: Generate 50 random numbers between 1 to 30 and then remove all duplicates from the list
list=[random.randrange(1,30) for _ in range(50)];
uniquelist=[];
for num in list:
    if num not in uniquelist:
        uniquelist.append(num);
print(list);
print(uniquelist);

#CODE 4: Generate 30 numbers and put them in a list, make two more lists, one with only positive and second with only negative numbers
list=[random.randrange(-15,15) for _ in range(30)];
poslist=[];
neglist=[];
for num in list:
    if num >0:
        poslist.append(num);
    if num<0:
        neglist.append(num);
print(poslist);
print(neglist);

#CODE 5: A list contains five strings, convert all these strings to uppercase
strings = ["hello","cat","dog","cash","pepsi"];
ustrings = [_.upper() for _ in strings];
print (ustrings);

#CODE 6: Convert a list of temperatures  in fahrenight to celcius
fahrenheit = [32, 124, 19, 112, 71];
celsius = [(f - 32) * 5/9 for f in fahrenheit];
print(celsius);

#CODE 7: Stack
#CODE 8: Queue

#CODE 9:take two lists of nums, make a third list such that it has elements which are in the first list but not in the second(use list comprehension)
l1=[1,2,3,4];
l2=[2,3,7];
l3=[i for i in l1 if i not in l2];
print(l3);



