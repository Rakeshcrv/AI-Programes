
database=["croaks","sings"]
knowbase=["frog","canary"]
color=["green","yellow"]
def display(): 
    print("\nX is",end=" ")
    print("\n1.Frog\n2.Canary",end="")
    print("\nselect 1 or 2",end=" ")
def main(): 
    display()
    try:
        x=int(input())
        print("\n",end=" ")
        if x == 1:
            print("chance of eating flies",end=" ")
        elif x == 2:
            print("chance of shrimping",end=" ")
        else:
            print("invalid option selected\n",end=" ")
            return
        if x>=1 and x <= 2:
            print("\nX is", end="")
            print(knowbase[x-1],end=" ")
            print("\n1.green\n2.Yellow",end=" ")
            print("\n select 1 or 2:",end=" ")
            k=int(input())
            if k == 1 and x == 1:
                print("yes it is", end=" ")
                print(color[0],end=" ")
                print("color and will", end=" ")
                print(database[0],end=" ")
            elif k == 2 and x == 2:
                print("yes it is", end=" ")
                print(color[1], end=" ")
                print("color and will", end=" ")
                print(database[1], end=" ")
            else:
                print("invalid knowledge and database combination\n", end=" ")
    except ValueError:
        print("invalid input, please enter integer\n", end=" ")
if __name__ == "__main__":
    main()