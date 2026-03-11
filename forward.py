database=['crocks','eat flies','shrimps','sings']
knowbase=['frog','canary','green','yellow']
def display():
    print("\nx is\n1.crocks\n2.eat flies\n3.shrimps\n4.sings",end="")
    print("\n select one option(1-4):",end="")
def main():
    print("\n forward chaining",end="")
    display()
    try:
        x=int(input())
        print("\n",end="")
        if x==1 or x==2:
            print("chance of frog\n",end="")
        elif x==3 or x==4:
            print("chance of canary\n",end="")
        else:
            print("invalid input",end="")
        if x>=1 and x<=4:
            print("\n x is",end="")
            print(database[x-1],end="")
            print("\n color is \n1.green\n2.yellow")
        print("\n select one option(1-2):",end="")
        k=int(input())
        if k==1 and (x==1 or x==2):
            print("yes it is",end="")
            print(knowbase[0],end="")
            print("and color is",end="")
            print(knowbase[2],end="")
        elif k==2 and (x==3 or x==4):
            print("yes it is",end="")
            print(knowbase[1],end="")
            print("and color is",end="")
            print(knowbase[3],end="")
        else:
            print("Invalid knowledge database combination",end="")
    except Exception as e:
        print("invalid input",end="")

if __name__=="__main__":
    main()