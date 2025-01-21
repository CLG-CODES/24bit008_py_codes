import math
#CODE 1: Print largest and smallest values out of two
num1=float(input("Pls give the first value"));
num2=float(input("Pls give the second value"));
if num1>num2:
    print(num1,"is more than",num2);
else:
    print(num2,"is more than",num1);
    
#CODE 2: Print the largest and smallest value out of three
num1=float(input("Pls give the first value"));
num2=float(input("Pls give the second value"));
num3=float(input("Pls give the third value"));
if num1>num2 and num1>num3:
    print(num1,"is the greatest");
elif num2>num1 and num2>num3:
    print(num2,"is the greatest");
else:
    print(num3,"is the greatest");
    
if num1<num2 and num1<num3:
    print(num1,"is the smallest");
elif num2<num1 and num2<num3:
    print(num2,"is the smallest");
else:
    print(num3,"is the smallest");

#CODE 3: Check whether a number is even or odd
inp=int(input("pls give the value:"));
def checker():
    if inp%2==0:
        print("Is Even!");
    else:
        print("Is Odd!");
checker()

#CODE 4:Check whether a number is divisible by 10
num=int(input("pls give the value:"));
def checker():
    if num%10==0:
        print("Is divisible by 10!");
    else:
        print("Is not divisible by 10!");
checker()

#CODE 5:Accept a person's given age,if less than 18 print major else minor
age=int(input("pls give the value:"));
def checker():
    if age<18:
        print("Is A Minor");
    else:
        print("Is A Major");
checker()

#CODE 6:Accept a number from the user and print the amount of digits in it
num=int(input("pls give the value:"));
def checker(num):
    div=num;
    leng=0
    while div>1:
        div=div/10;
        leng=leng+1;
    return leng;
print(checker(num));

#CODE 7 :Accept a year value from the user, Check weather it is a leap year
year=int(input("pls give the value:"));
if year%400==0:
    if year%100==0:
        print("It is a leap year");
    else:
        print("It is not");
else:
    if year%4==0:
        print("It is a leap year");
    else:
        print("It is not");

#CODE 8 :Check weather a triangle is valid or not if all three angles are entered by the user
ang1=int(input("pls give the value:"));
ang2=int(input("pls give the value:"));
ang3=int(input("pls give the value:"));
def checker(ang1,ang2,ang3):
    if ang1+ang2+ang3=180:
        print("It is a triangle!");
    else:
        print("It is not!");
checker(ang1,ang2,ang3);

#CODE 9 : Print the absolute value given by the user
num = int(input("pls give the value:"));
def absfunc(x):
    if num<0:
        print(-x);
    else:
        print(x);
absfunc(num);

#CODE 10: Given the length and breadth find if the area of the retangle is more than the peremeter
a = int(input("pls give the value:"));
b = int(input("pls give the value:"));
area=a*b;
pere=2*(a+b);
if area>pere:
    print("area is more");
else:
    print("pere is more");

#CODE 11: given three points, check if the fall in the straight line
x1= int(input("pls give the value of first x:"));
y1=int(input("pls give the value of first y:"));
x2=int(input("pls give the value of second x:"));
y2=int(input("pls give the value of second y:"));
x3=int(input("pls give the value of third x:"));
y3=int(input("pls give the value of third y:"));
# if area of triangle is 0 then they are collinear, area is given by the determinant
determinant=x1*y2+x3*y1+x2*y3-x3*y2-x1*y3-y1*x2
def det(x):
    if x==0:
        print("They lie on the same line!");
    else:
        print("They do not lie on the same line!");
det(determinant);

#CODE12: If (x,y) is the centre and its radius is given, find if a point lies on/in or outside the circle
x1= int(input("pls give the value of x:"));
y1=int(input("pls give the value of y:"));
rad=int(input("pls give the value of radius:"));
x2= int(input("pls give the value of the point x:"));
y2=int(input("pls give the value of the point y:"));
val=math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
def checker(val,rad):
    if val-rad>0:
        print("Out");
    elif val-rad=0:
        print("On");
    else:
        print("In");
checker(val,rad);

#CODE13: Convert number 0 to 19 to words
list1=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fiften","sixteen","seventeen","eighteen","nineteen"]
num=int(input("Pls give the number:"));
print(list1[num]);

#CODE14: Accept Marks of three subjects. Print total and average along with wheater a candidate has passed or failed, if a student secures <=39 he has failed ans assign a grade
sub1=float(input("Pls give the marks of the first sub:"));
sub2=float(input("Pls give the marks of the second sub:"));
sub3=float(input("Pls give the marks of the third sub:"));
total=sub1+sub2+sub3;
print("The total is:",total);
print("The avg is:",total/3);
def grader(x):
    if x>0 and x<40:
        print("GRADE F");
    elif x>=40 and x<45:
        print("GRADE: P");
    elif x>=45 and x<50:
        print("GRADE: C");
    elif x>=50 and x<55:
        print("GRADE: B");
    elif x>=55 and x<60:
        print("GRADE: B+");
    elif x>=60 and x<70:
        print("GRADE: A");
    elif x>=70 and x<80:
        print("GRADE: A+");
    else:
        print("GRADE: O");
print("For the first subject,");
grader(sub1);
print("For the second subject,");
grader(sub2);
print("For the third subject,");
grader(sub3);
    





    


    

