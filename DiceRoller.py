import random

#print(p)
x="y";
while(x == "y"):

    p=random.randint(1,6)
    
    if p==1:
        print("---------")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("---------")
        
    elif p==6:
        print("---------")
        print("| 0   0 |")
        print("| 0   0 |")
        print("| 0   0 |")
        print("---------")

    
    elif p==5:
        print("---------")
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |")
        print("---------")

    
    elif p==4:
        print("---------")
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |")
        print("---------")

    
    elif p==3:
        print("---------")
        print("|   0   |")
        print("|   0   |")
        print("|   0   |")
        print("---------")

    
    elif p==2:
        print("---------")
        print("|       |")
        print("| 0   0 |")
        print("|       |")
        print("---------")

    print("do you want to roll again? press y for yes and n for no")
    x=input()

