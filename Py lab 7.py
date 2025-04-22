#CODE1: Concatinate 3 dictionaries to create a 4th one
d1={"a":1,"b":2,"c":3};d2={"d":4};d3={"e":5};d4={};
d4.update(d1);d4.update(d2);d4.update(d3);
print(d4);

#CODE2: Write a code to check if a dictionary is empty
d1={"a":1};d2={}
def isempty(d):
    if len(d)==0: return True;
    return False;
print(isempty(d1));print(isempty(d2))

#CODE3: Find min and max department wise salary, dictionary has department,employee num and salary
dic = {1: {"Software": 30000},2: {"Software": 26000},3: {"HR": 14500},4: {"HR": 17650}}

soft_max = 0
soft_min = float('inf')
HR_max = 0
HR_min = float('inf')

for i in dic:
    for role, salary in dic[i].items():
        if role == "Software":
            if salary > soft_max:
                soft_max = salary
            if salary < soft_min:
                soft_min = salary
        elif role == "HR":
            if salary > HR_max:
                HR_max = salary
            if salary < HR_min:
                HR_min = salary

print("Software - Max:", soft_max, "Min:", soft_min)
print("HR - Max:", HR_max, "Min:", HR_min)

#CODE4: Count the frequency of each character in the string
i1=input("Type here:")
d={}
for i in i1:
    if i not in d: d[i]=1;
    else: d[i]+=1;
print(d)

#CODE5: Grocery items in first dictionary and amount purchased in second, find the total
items={"potato":50,"tomato":25};
purchased={"potato":2,"tomato":4};
sum=0;
for i in purchased:
    if i in items:
        sum+=items[i]*purchased[i];
print("BILL IS:",sum);

