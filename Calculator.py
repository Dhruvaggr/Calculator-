#Calculator
#Calculator
from replit import clear
from art import logo
print(logo)
def add(n1,n2):
    return n1+n2

def subs(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


resume=True
while(resume):
    n1=float(input("What is first no: "))
    print("+\n -\n *\n /\n ")
    
    should_continue=True
    while(should_continue):
        pick_operation= input("pick_operation: ")
        n2=float(input("What is next no : "))
        if pick_operation=='+' :
           result= add(n1,n2)
        elif pick_operation=='-':
           result= subs(n1,n2)
        elif pick_operation=='*':
           result= multiply(n1,n2)
        else:
           result= divide(n1,n2)
        
        print(f"{n1}{pick_operation}{n2}={result}")
        response= input(f"Type Y to continue calculating with {result} or N to start new calculation")
        if response== 'Y' :
            n1=result
        else:
            should_continue=False
            clear()
    
    
        
