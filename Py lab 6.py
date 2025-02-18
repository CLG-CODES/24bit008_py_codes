#CODE 1: A list contains the names of boys ans girls as its elements. Boy's name is in the form of a tuple, find amount of boys ans girls in the list
l=["g1","g2",("b1","b2"),"g3",("b3",)]
boy_c=0;
girl_c=0;
lenn=0;
for i in l:
    if type(i)==tuple:
        lenn=len(i)
        boy_c=boy_c+lenn;
    else:
        girl_c=girl_c+1;
print(boy_c,girl_c);

#CODE 2:A list contains tuples which has roll no, name and age of student use a python code to get 3 lists of no,name and age
l=[(1,2,3),("parth","maan","pizza"),(17,18,19)];
l1=list(l[0]);
l2=list(l[1]);
l2=list(l[2]);

#CODE 3:supppose a date is in the form of a tuple (d,m,y) find the amount of days between two loops
d1=(1,1,25);
d2=(1,1,24);

#CODE 4: Create a list of tuples containing a food item and its price. sort the tuples in descending order of price:
l=[("pizza",100),("vadapav",20),("misal",40)]
print(l[1])


