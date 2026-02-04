global N
N=4

def ps(boared):
    for i in range(N):
        for j in range(N):
            if boared[i][j]==True:
                print(" Q ",end="")
            else:
                print(" . ",end="")
        print()

def is_safe(boared,row,col):
    for i in range(col):
        if boared[row][i]==True:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if boared[i][j]==True:
            return False
    for i,j in zip(range(row,N,1),range(col,-1,-1)):
        if boared[i][j]==True:
            return False
    return True
    
def solve_nq_util(boared,col):
    if col>=N:
        return True
    for i in range(N):
        if is_safe(boared,i,col):
            boared[i][col]=1
            if solve_nq_util(boared,col+1)==True:
                return True
            boared[i][col]=0
    return False

def solve_nq():
    boared=[[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
    if solve_nq_util(boared,0)==False:
        print("Solution does not exist")
        return False
    ps(boared)
    return True
if __name__=="__main__":
    solve_nq()