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
