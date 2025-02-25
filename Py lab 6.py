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
l=[("rol1","name1","age2"),("rol2","name2","age2")]
l1=[];l2=[];l3=[]
for i in l:
    l1.append(i[0]);
    l2.append(i[1]);
    l3.append(i[2]);
print(l1,l2,l3,sep="\n")

#CODE 3:supppose a date is in the form of a tuple (d,m,y) find the amount of days between two loops
d1=(1,1,25);
d2=(1,1,24);

#CODE 4: Create a list of tuples containing a food item and its price. sort the tuples in descending order of price:
tup=[("pizza",100),("vadapav",15),("misal pav",50)];
lenn=len(tup);l1=list(tup);l2=[];l3=[];
for i in range(lenn):
    l2.append(l1[i][1]);
l2.sort(reverse=True);
for i in range(lenn):
    for j in range(lenn):
        if l2[i]==tup[j][1]:
            l3.append(tup[j]);
tup=tuple(l3);

#CODE 5: Remove empty tuples from a list of tuples
l1=[(0,1),(3,5),(12,1),()];
for i in l1:
    if len(i)==0:
        l1.remove(i);
print(l1);

#CODE 6: Modifiy an element in a tuple
tu=(0,1,2,3,5)
l1=list(tu);
l1[4]=4;
tu=tuple(l1);
print(tu);

#CODE 7: Delete an element in a tuple
tu=(0,1,2,3);
l1=list(tu);
l1.remove(l1[2]);
tu=tuple(l1);
print(tu);

