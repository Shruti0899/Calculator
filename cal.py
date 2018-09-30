
print("CALCULATOR\n")

class Mycalc:
    def __init__(self):
##        a=int(input("enter value of a:"))
##        b=int(input("enter value of b:\n"))
##        self.a=a;
##        self.b=b;
        self.menu();

    def ip(self):
        self.a = int(input("enter a"));
        self.b = int(input("enter b"));
        return self.a, self.b;
    
    def sum1(self):
        a,b = self.ip();
        print(a+b);
        self.menu()
        
    def diff(self):
        a,b = self.ip();

        print(a-b)
        self.menu()
        
    def mul(self):
        a,b = self.ip();

        print(a*b)
        self.menu()
        
    def div(self):
        a,b = self.ip();

        print(a/b)
        self.menu()
        
    def mod(self):
        a,b = self.ip();

        print(a%b)
        self.menu()
        
    def menu(self):
        print("Choose your op number from the following menu:\n")
        print("1.ADD\n2.SUBTRACT\n3.DIVIDE\n4.MUL\n5.MOD DIV\n6.EXIT")
        op=input()
        if op!="6":
            if op=='1':
                self.sum1()
            elif op=='2':
                self.diff()
            elif op=='4':
                self.mul()
            elif op=='3':
                self.div()
            elif op=='5':
                self.mod()
        elif op=="6":
            exit()
        else:
            print("invalid number");
            
myob=Mycalc()







    

    
