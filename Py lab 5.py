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
print("Welcome to the Stack!");l=[];
def choice():
    print("="*50);print("What would you like to do?");
    print("press 1 for making a stack");print("press 2 for adding a new element");
    print("press 3 for popping an element");print("press 4 for clearing the stack");
    print("press 5 for printing the stack");return int(input("Type here:"));
while True:
    decision=choice()
    if decision==1:
        for _ in range(int(input("How many numbers do u want to have in the stack?"))):
            l.append(input("Please give the value:"));      
    elif decision==2:l.append(input("Please give the value!")) 
    elif decision==3:l.remove(l[-1]);
    elif decision==4:del l;l=[];
    elif decision==5:
        for i in l: print(i);
    else:
        print("Give input in the valid range only.")
    print("Do you want to do anything else?");
    print("Press 1 for yes 0 for no");
    inp=int(input("Pls type here:"));
    if inp==1: continue;
    else: break;

#CODE 8: Queue
print("Welcome to the Queue!");
q = [];
def choice():
    print("="*50);print("What would you like to do?");
    print("Press 1 to create a queue");print("Press 2 to add a new element");
    print("Press 3 to remove an element");print("Press 4 to clear the queue");
    print("Press 5 to print the queue");return int(input("Type here: "));
while True:
    decision = choice();
    if decision == 1:
        for _ in range(int(input("How many numbers do you want to have in the queue?"))):
            q.append(input("Please give the value:"));      
    elif decision == 2:
        q.append(input("Please give the value!"));
    elif decision == 3: q.pop(0);
    elif decision == 4:del q;q = [];
    elif decision == 5:
        for i in q:print(i);
    else:
        print("Give input in the valid range only.");
    print("Do you want to do anything else?");
    print("Press 1 for yes, 0 for no");
    inp = int(input("Pls type here: "));
    if inp == 1:
        continue;
    else:
        break;


#CODE 9:take two lists of nums, make a third list such that it has elements which are in the first list but not in the second(use list comprehension)
l1=[1,2,3,4];
l2=[2,3,7];
l3=[i for i in l1 if i not in l2];
print(l3);



