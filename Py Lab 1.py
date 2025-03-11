# CODE1: ADD TWO NUMBERS
num1=int(input("Pls give the first number:"));
num2=int(input("Pls give the second number"));
numf=num1+num2;
print(numf);
# CODE2: SUBTRACT TWO NUMBERS
num1=int(input("Pls give the first number:"));
num2=int(input("Pls give the second number"));
numf=num1-num2;
print(numf);
# CODE3: MULTIPLY TWO NUMBERS
num1=int(input("Pls give the first number:"));
num2=int(input("Pls give the second number"));
numf=num1*num2;
print(numf);
# CODE4: DIVIDE TWO NUMBERS
num1=int(input("Pls give the first number:"));
num2=int(input("Pls give the second number"));
numf=num1/num2;
print(numf);
# CODE5: Add, multiply, subtract and divide two numbers
num1=int(input("Pls give the first number:"));
num2=int(input("Pls give the second number"));
numf1=num1+num2;print(numf1);
numf2=num1-num2;print(numf2);
numf3=num1*num2;print(numf3);
numf4=num1/num2;print(numf4);
# CODE6: Convert hours into minutes
hours=float(input("Pls give the hours:"));
mins=hours*60;
print(mins);
# CODE7: Convert minutes into hours
mins=float(input("Pls give the mins:"));
hours=mins/60;
print(hours);
# CODE8: Convert dollars into Rs. Where 1 $ = 48 Rs
USDINR=48;
USD=float(input("Pls give the amount of dollars:"));
INR=USD*USDINR;
print("INR amt is:",INR);
# CODE9: Convert Rs. into dollars where 1 $ = 48 Rs
USDINR=48;
INR=float(input("Pls give the amount of Rs:"));
USD=INR/USDINR;
print("USD amt is:",USD);
# CODE10: Convert dollars into pound where 1 $ = 48 Rs. And 1 pound = 70 Rs.
USDINR=48;
GBPINR=70;
Rs=float(input("How many dollars?:"));
Rs=Rs*USDINR;
GBP=Rs/GBPINR;
print(GBP);
# CODE11: Convert Grams to Kg
grams=float(input("Pls provide the amount in grams:"));
kg=grams/1000;
print(kg);
# CODE12: Convert Kg to Grams
kg=float(input("Pls provide the value  in kg:"));
g=kg*1000;
print(g);
# CODE13: Convert Bytes to Kb,Mb,Gb
B=float(input("Pls give the value of bytes:"));
Kb=B/1024;Mb=Kb/1024;Gb=Mb/1024;
print(Kb,Mb,Gb);
# CODE14: Convert celcius into Fahrenheit. F = (9/5 * C) + 32
C=float(input("Pls give the  value in C:"));
F=1.8*C+32;
print(F);
# CODE15: Convert Fahrenheit into celcius C=5/9*(F-32)
F=float(input("Pls give the value in Fahrenheit:"));
C=F-32;C=C*(5/9);
print(C);
# CODE16: Calculate interest where I = PRN/100.
P=float(input("Pls give value of Principle amount:"));
R=float(input("Pls give the value of the Rate:"));
N=float(input("Pls give the amount of time:"));
I=P*R*N;I=I/100;
print(I);
# CODE17: Calculate area & perimeter of a square. A = L^2, P = 4L
s=float(input("Pls give the length of one side:"));
print("Area is:",s*s,"Perimeter is:",4*s);
# CODE18: Calculate area & perimeter of a rectangle. A = L*B, P = 2 (L+B)
len=float(input("Pls give the length:"));
bre=float(input("Pls give the bre:"));
print("The Area is:",len*bre,"Peri is:",2*(len*bre));
# CODE19: Calculate area of a circle. A = 22/7 * R * R
r=float(input("Pls give the radius:"));
print("Area is:",r*r*(22/7));
# CODE20: Calculate area of a triangle. A = H*L/2
h=float(input("Pls give the Height:"));
l=float(input("Pls give the Length"));
print(h*l/2);
"""CODE21:Calculate net salary where net salary = gross salary + allowance - deduction.
   Allowances are 10% while deductions are 3% of gross salary."""
gross=float(input("Pls give the gross salary:"));
net=gross+0.1*gross-0.03*gross;
print(net);
# CODE22: Calculate net sales where net sales = gross sales – 10% discount of gross sales.
sale=float(input("Gross is:"));
net=0.9*sale;
print(net);
# CODE23: Calculate average of three subjects along with their total.
s1=float(input("Pls give the value of the first sub:"));
s2=float(input("Pls give the value of the second sub:"));
s3=float(input("Pls give the value of the third sub:"));
snet=s1+s2+s3;
print("The sum is:",snet);
avg=snet/3;
print("The avg is:",avg);
# CODE24: Swap two values
n1=float(input("Pls give the value of the first num:"));
n2=float(input("Pls give the value of the second num:"));
n1,n2=n2,n1;
print(n1,n2);












