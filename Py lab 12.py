#CODE1: Perform Complex arithmatics
class Complex:
    def __init__(self,real,comp):
        self.real=real;
        self.comp=comp;
    def add(self,others):
        rv=self.real+others.real;
        cv=self.comp+others.comp;
        return str(rv)+"+i"+str(cv);
    def sub(self,others):
        rv=self.real-others.real;
        cv=self.comp-others.comp;
        return str(rv)+str(cv)+"*i";        
obj1=Complex(1,2);
obj2=Complex(2,3);
print(Complex.add(obj1,obj2));
print(Complex.sub(obj1,obj2));

#CODE2:Matrix Addition,Multiplication,Transpose
class Matrix:
    def __init__(self,m1):
        self.m1=m1;
    def add(self,others):
        matrix=[[0,0,0],[0,0,0],[0,0,0]];
        for i in range(3):
            for j in range(3):
                matrix[i][j]=self.m1[i][j]+others.m1[i][j]
        return matrix;
    def multiply(self, other):
        result = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.m1[i][k] * other.m1[k][j]
        return result

    def transpose(self):
        result = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                result[i][j] = self.m1[j][i]
        return result

matrix1=Matrix([[1,0,0],[0,1,0],[0,0,1]]);
matrix2=Matrix([[2,0,0],[0,2,0],[0,0,2]]);
print(Matrix.add(matrix1,matrix2));
print(Matrix.multiply(matrix1,matrix2));
print(Matrix.transpose(matrix2))


#CODE3: Surface Area and Volume
class Q3:
    def choice(self):
        i1=int(input("PRESS 1 FOR SQUARE 2 FOR RECTANGLE AND 3 FOR CIRCLE:"));
        return i1;
    
    def  surfarea_and_vol(self,opt):
        if opt==1:
            s=float(input("Pls give length of side:"));
            print("SA:",6*s,"Vol:",s**3);
        elif opt==2:
            l=float(input("Pls give length of side:"));
            b=float(input("Pls give bredth of side:"));
            h=float(input("Pls give height:"))
            print("SA:",2*(l*b+b*h+h*l),"Vol:",l*b*h);
        elif opt==3:
            r=float(input("Pls give radius"));
            print("SA:",4*3.14159*(r**2),"Vol:",3.14159*(r**3)*(4/3));    
obj1=Q3()
obj1.surfarea_and_vol(obj1.choice())

#CODE 4: Circum of the input

class Q4:
    def choice(self):
        i1=int(input("PRESS 1 FOR SQUARE 2 FOR RECTANGLE AND 3 FOR CIRCLE:"));
        return i1;   
    def  circum(self,opt):
        if opt==1:
            s=float(input("Pls give length of side:"));
            print(6*s);
        elif opt==2:
            l=float(input("Pls give length of side:"));
            b=float(input("Pls give bredth of side:"));
            print(2*(l+b));
        elif opt==3:
            r=float(input("Pls give radius"));
            print(3.14159*r*2) 

obj1=Q4()   
obj1.circum(obj1.choice())

#CODE5:Write a program that creates and uses a Time class to perform various time arithmetic operations.
class Time:
    to_mins = lambda self: str((self.h)*60+self.m)+" mins";
    def __init__(self,h,m):
        self.h=h;self.m=m;
    timegap = lambda self,others: str(abs(self.h-others.h))+" hours "+str(abs(self.m-others.m))+" mins is the time difference";
    def convert(self):
        status="AM";
        if self.h>12: self.h,status=self.h-12,"PM";
        return str(self.h)+" "+str(self.m)+" "+status;
        
t1=Time(int(input("Give hour input(24H format) 1:  ")),int(input("Give minuite 1 input:  ")));
t2=Time(int(input("Give hour input(24H format) 2:  ")),int(input("Give minuite  2 input:  ")));
print("Time 1 in mins:" ,t1.to_mins());
print("Time 2 in mins:" ,t2.to_mins());
print("Time gap is:",Time.timegap(t1,t2));
print("Time 1 in 12H format",Time.convert(t1));
print("Time 2 in 12H format" ,Time.convert(t2));


#CODE6:Write a program to create a class Date that has a list containing day, month and year attributes. Define an overloaded == operator to compare two Date objects.
class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year];
    def __eq__(self, other):
        if isinstance(other, Date):return self.date == other.date;
        return False;
date1 = Date(13, 12, 2025);
date2 = Date(8, 7, 1458);
print(date1 == date2);

#CODE7:Create a class Weather that has a list containing weather parameters. Define an overloaded in operator that checks whether an item is present in the list. (Hint: define the function __contains__( )in a class.
class Weather:
    def __init__(self, temperature, wind):
        self.weather_params = [temperature, wind];

    def __contains__(self, item):
        return item in self.weather_params;

weather = Weather(25, True);
print(25 in weather); 

#CODE8:Implement a String class containing the following functions:a. Overloaded += operator function to perform string concatenationb. Method toLower() to convert upper case letters to lower case.c. Method toUpper() to convert lower case letters to upper case
class String:
    def __init__(self, stri=""):
        self.stri = stri;
    def __iadd__(self, other):
        if isinstance(other, String):
            self.stri += other.stri;
        else:
            self.stri += str(other);
        return self
    def toLower(self):
        self.stri = self.stri.lower(); return self.stri;   
    def toUpper(self):
        self.stri = self.stri.upper(); return self.stri;
s1=String("cAt");
print(s1.toUpper());


