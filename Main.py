def add(n1, n2):
    sum = n1 + n2
    print("sum of ",n1," and ",n2," is ",sum)

def sub(n1, n2):
    sum = n1 - n2
    print("div of ",n1," and ",n2," is ",sum)

def mul(n1, n2):
    sum = n1 * n2
    print("mul of ",n1," and ",n2," is ",sum)

def div(n1, n2):
    sum = n1 // n2
    print("div of ",n1," and ",n2," is ",sum)

#MAIN PROGRAM
while  True:
    print("\n"*20)
    print("1. Addition ")
    print("2. Substraction ")
    print("3. Multiplication ")
    print("4. Division ")
    print("0. EXIT")

    char = int(input("Enter your choice : "))
    print("\n"*20)
    if char==1:
        n1 = int(input("Enter you first No : "))
        n2 = int(input("Enter you Second No : "))
        add(n1, n2)
    elif char==2:
        n1 = int(input("Enter you first No : "))
        n2 = int(input("Enter you Second No : "))
        sub(n1, n2)
    elif char==3:
        n1 = int(input("Enter you first No : "))
        n2 = int(input("Enter you Second No : "))
        mul(n1, n2)
    elif char==4:
        n1 = int(input("Enter you first No : "))
        n2 = int(input("Enter you Second No : "))
        div(n1, n2)
    else:
        print("Thanks..... ")
        exit
    input("Press any key to continue..... ")
